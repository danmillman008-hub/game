/* Headless MD runner with decompression capture.
   usage: mdcap rom frames outdir [events.txt] */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "libretro.h"

extern uint8_t vram[0x10000];
extern uint16_t cram[0x80];
extern uint16_t sat[0x400];
extern unsigned md_vdp_reg(int i);
extern unsigned md_vdp_status(void);
extern unsigned md_vsram(int i);
extern uint8_t work_ram[0x10000];
extern uint8_t *md_capture_ptr;
extern int md_capture_active;

void set_cpu_hook(void(*hook)(int,int,unsigned,unsigned));
void capture_hook(int,int,unsigned,unsigned);
extern unsigned g_frame; extern FILE *g_cap; extern unsigned g_hits;

static int16_t fb[720*576]; static unsigned W=320,H=224; static int PITCH=0;

#define MAXEV 512
static struct { int frame; unsigned id; int down; } ev[MAXEV]; static int nev=0;

static bool env(unsigned c, void *d){
  switch(c){
    case RETRO_ENVIRONMENT_SET_PIXEL_FORMAT: return true;
    case RETRO_ENVIRONMENT_GET_VARIABLE: ((struct retro_variable*)d)->value=NULL; return false;
    case RETRO_ENVIRONMENT_GET_VARIABLE_UPDATE: *(bool*)d=false; return true;
    case RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY:
    case RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY: *(const char**)d="."; return true;
    default: return false;
  }
}
static void vid(const void*d,unsigned w,unsigned h,size_t p){W=w;H=h;PITCH=(int)p;if(d)memcpy(fb,d,p*h);}
static void aud(int16_t l,int16_t r){(void)l;(void)r;}
static size_t audb(const int16_t*d,size_t f){(void)d;return f;}
static void ipoll(void){}
static int16_t istate(unsigned port,unsigned dev,unsigned idx,unsigned id){
  (void)dev;(void)idx; if(port) return 0;
  for(int i=0;i<nev;i++) if(ev[i].id==id&&ev[i].down) return 1;
  return 0;
}
static unsigned btn_id(const char*s){
  if(!strcmp(s,"UP"))return RETRO_DEVICE_ID_JOYPAD_UP;
  if(!strcmp(s,"DOWN"))return RETRO_DEVICE_ID_JOYPAD_DOWN;
  if(!strcmp(s,"LEFT"))return RETRO_DEVICE_ID_JOYPAD_LEFT;
  if(!strcmp(s,"RIGHT"))return RETRO_DEVICE_ID_JOYPAD_RIGHT;
  if(!strcmp(s,"A"))return RETRO_DEVICE_ID_JOYPAD_A;
  if(!strcmp(s,"B"))return RETRO_DEVICE_ID_JOYPAD_B;
  if(!strcmp(s,"C"))return RETRO_DEVICE_ID_JOYPAD_Y;
  if(!strcmp(s,"START"))return RETRO_DEVICE_ID_JOYPAD_START;
  return 0;
}
static void dump_ppm(const char*path){
  FILE*o=fopen(path,"wb"); fprintf(o,"P6\n%u %u\n255\n",W,H);
  for(unsigned y=0;y<H;y++)for(unsigned x=0;x<W;x++){
    uint16_t c=((uint16_t*)fb)[y*(PITCH/2)+x];
    unsigned char px[3]={(unsigned char)(((c>>11)&0x1f)*255/31),(unsigned char)(((c>>5)&0x3f)*255/63),(unsigned char)((c&0x1f)*255/31)};
    fwrite(px,1,3,o);}
  fclose(o);
}
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage: %s rom frames outdir [events] [--state-in F] [--state-out F --state-at N]\n",argv[0]);return 2;}
  int frames=atoi(argv[2]); const char *dir=argv[3];
  static int ev_end[MAXEV];
  if(argc>4){ FILE*e=fopen(argv[4],"r"); char line[128];
    while(e&&fgets(line,sizeof line,e)&&nev<MAXEV-8){
      int fr,en=-1; char b[64]; b[0]=0;
      int k=sscanf(line,"%d %63s %d",&fr,b,&en);
      if(k<2) continue;
      ev[nev].frame=fr; ev[nev].id=btn_id(b); ev[nev].down=1;
      ev_end[nev]=(k>=3)?en:fr+3;
      nev++;
    }
    if(e)fclose(e);
    int n=nev;
    for(int i=0;i<n;i++){ ev[nev].frame=ev_end[i]+1; ev[nev].id=ev[i].id; ev[nev].down=0; ev_end[nev]=ev_end[i]; nev++; } }

  /* save-state options: --state-in loads a machine snapshot as frame 0, so a run
     always starts from identical initial conditions; --state-out/--state-at
     writes one after the given frame. */
  const char *state_in=NULL, *state_out=NULL; int state_at=-1;
  /* Dumping 128 KB of RAM+VRAM every frame is only affordable for short runs.
     --dump-from N skips the per-frame state logs before frame N, so a long
     boot-and-navigate run can record just the gameplay window. */
  long dump_from=0;
  for(int i=4;i<argc;i++){
    if(!strcmp(argv[i],"--state-in") && i+1<argc) state_in=argv[++i];
    else if(!strcmp(argv[i],"--state-out") && i+1<argc) state_out=argv[++i];
    else if(!strcmp(argv[i],"--state-at") && i+1<argc) state_at=atoi(argv[++i]);
    else if(!strcmp(argv[i],"--dump-from") && i+1<argc) dump_from=atol(argv[++i]);
  }

  retro_set_environment(env); retro_set_video_refresh(vid);
  retro_set_audio_sample(aud); retro_set_audio_sample_batch(audb);
  retro_set_input_poll(ipoll); retro_set_input_state(istate);
  retro_init();
  FILE*f=fopen(argv[1],"rb"); fseek(f,0,SEEK_END); long sz=ftell(f); fseek(f,0,SEEK_SET);
  uint8_t*rom=malloc(sz); if(fread(rom,1,sz,f)!=(size_t)sz)return 3; fclose(f);
  struct retro_game_info gi={argv[1],rom,(size_t)sz,NULL};
  if(!retro_load_game(&gi)){fprintf(stderr,"load failed\n");return 4;}

  char p[512];
  if(state_in){
    FILE *sf=fopen(state_in,"rb");
    if(!sf){fprintf(stderr,"cannot open state %s\n",state_in);return 5;}
    fseek(sf,0,SEEK_END); long ssz=ftell(sf); fseek(sf,0,SEEK_SET);
    void *sbuf=malloc(ssz);
    if(fread(sbuf,1,ssz,sf)!=(size_t)ssz){fprintf(stderr,"short state read\n");return 6;}
    fclose(sf);
    if(!retro_unserialize(sbuf,(size_t)ssz)){fprintf(stderr,"unserialize failed\n");return 7;}
    free(sbuf);
    fprintf(stderr,"loaded state %s (%ld bytes), frame counter reset to 0\n",state_in,ssz);
  }
  snprintf(p,sizeof p,"%s/decomp.bin",dir); g_cap=fopen(p,"wb");
  set_cpu_hook((void(*)(int,int,unsigned,unsigned))capture_hook);

  /* per-frame state log: frame, 80 SAT entries, regs, VSRAM, and a 64 KB RAM image */
  snprintf(p,sizeof p,"%s/frames.bin",dir); FILE *flog=fopen(p,"wb");
  snprintf(p,sizeof p,"%s/ram.bin",dir); FILE *rlog=fopen(p,"wb");
  snprintf(p,sizeof p,"%s/vram.bin",dir); FILE *vlog=fopen(p,"wb");

  for(int fr=0;fr<frames;fr++){
    g_frame=(unsigned)fr;
    for(int i=0;i<nev;i++) ev[i].down=(fr>=ev[i].frame);
    retro_run();
    if(flog && (long)fr>=dump_from){
      unsigned char hdr[4]={(unsigned char)(fr>>24),(unsigned char)(fr>>16),(unsigned char)(fr>>8),(unsigned char)fr};
      fwrite(hdr,1,4,flog);
      fwrite(sat,1,640,flog);
      unsigned char mr[26]; for(int i=0;i<24;i++) mr[i]=(unsigned char)md_vdp_reg(i);
      unsigned st=md_vdp_status(); mr[24]=(unsigned char)(st>>8); mr[25]=(unsigned char)st;
      fwrite(mr,1,26,flog);
      unsigned char vs[80]; for(int i=0;i<40;i++){ unsigned v=md_vsram(i); vs[i*2]=(unsigned char)(v>>8); vs[i*2+1]=(unsigned char)v; }
      fwrite(vs,1,80,flog);
      fwrite(cram,1,128,flog);
    }
    if(rlog && (long)fr>=dump_from) fwrite(work_ram,1,0x10000,rlog);
    if(vlog && (long)fr>=dump_from) fwrite(vram,1,0x10000,vlog);
    if((fr%50)==49){
      snprintf(p,sizeof p,"%s/f%04d.ppm",dir,fr); dump_ppm(p);
      snprintf(p,sizeof p,"%s/f%04d.vram",dir,fr); FILE*o=fopen(p,"wb"); fwrite(vram,1,0x10000,o); fclose(o);
      snprintf(p,sizeof p,"%s/f%04d.cram",dir,fr); o=fopen(p,"wb"); fwrite(cram,2,0x80,o); fclose(o);
      snprintf(p,sizeof p,"%s/f%04d.vdp",dir,fr); o=fopen(p,"wb");
      { unsigned char r[24]; for(int i=0;i<24;i++) r[i]=(unsigned char)md_vdp_reg(i);
        unsigned st=md_vdp_status(); unsigned char sb[2]={(unsigned char)(st>>8),(unsigned char)st};
        fwrite(r,1,24,o); fwrite(sb,1,2,o);
        { unsigned char vs[128]; for(int i=0;i<64;i++){ unsigned v=md_vsram(i); vs[i*2]=(unsigned char)(v>>8); vs[i*2+1]=(unsigned char)v; }
          fwrite(vs,1,128,o); } }
      fclose(o);
    }
    if(state_out && fr==state_at){
      size_t n=retro_serialize_size(); void *sb=malloc(n);
      if(sb && retro_serialize(sb,n)){
        FILE *sf=fopen(state_out,"wb"); if(sf){fwrite(sb,1,n,sf);fclose(sf);}
        fprintf(stderr,"wrote state %s (%zu bytes) at frame %d\n",state_out,n,fr);
      }
      free(sb);
    }
  }
  snprintf(p,sizeof p,"%s/final.ppm",dir); dump_ppm(p);
  snprintf(p,sizeof p,"%s/final.vram",dir); FILE*o=fopen(p,"wb"); fwrite(vram,1,0x10000,o); fclose(o);
  snprintf(p,sizeof p,"%s/final.cram",dir); o=fopen(p,"wb"); fwrite(cram,2,0x80,o); fclose(o);
  if(vlog) fclose(vlog);
  if(flog) fclose(flog);
  if(rlog) fclose(rlog);
  if(g_cap){fclose(g_cap);g_cap=0;}
  printf("decompression captures: %u\n", g_hits);
  return 0;
}
