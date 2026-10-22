/* Headless MD runner with decompression capture.
   usage: mdcap rom frames outdir [events.txt] */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "libretro.h"

extern uint8_t vram[0x10000];
extern uint16_t cram[0x80];
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
  if(argc<4){fprintf(stderr,"usage: %s rom frames outdir [events]\n",argv[0]);return 2;}
  int frames=atoi(argv[2]); const char *dir=argv[3];
  if(argc>4){ FILE*e=fopen(argv[4],"r"); char b[64]; int fr;
    while(e&&fscanf(e,"%d %63s",&fr,b)==2&&nev<MAXEV-8){ ev[nev].frame=fr; ev[nev].id=btn_id(b); ev[nev].down=1; nev++; }
    if(e)fclose(e);
    int n=nev; for(int i=0;i<n;i++){ ev[nev].frame=ev[i].frame+4; ev[nev].id=ev[i].id; ev[nev].down=0; nev++; } }

  retro_set_environment(env); retro_set_video_refresh(vid);
  retro_set_audio_sample(aud); retro_set_audio_sample_batch(audb);
  retro_set_input_poll(ipoll); retro_set_input_state(istate);
  retro_init();
  FILE*f=fopen(argv[1],"rb"); fseek(f,0,SEEK_END); long sz=ftell(f); fseek(f,0,SEEK_SET);
  uint8_t*rom=malloc(sz); if(fread(rom,1,sz,f)!=(size_t)sz)return 3; fclose(f);
  struct retro_game_info gi={argv[1],rom,(size_t)sz,NULL};
  if(!retro_load_game(&gi)){fprintf(stderr,"load failed\n");return 4;}

  char p[512];
  snprintf(p,sizeof p,"%s/decomp.bin",dir); g_cap=fopen(p,"wb");
  set_cpu_hook((void(*)(int,int,unsigned,unsigned))capture_hook);

  for(int fr=0;fr<frames;fr++){
    g_frame=(unsigned)fr;
    for(int i=0;i<nev;i++) ev[i].down=(fr>=ev[i].frame && fr<ev[i].frame+4);
    retro_run();
    if((fr%100)==99){
      snprintf(p,sizeof p,"%s/f%04d.ppm",dir,fr); dump_ppm(p);
      snprintf(p,sizeof p,"%s/f%04d.vram",dir,fr); FILE*o=fopen(p,"wb"); fwrite(vram,1,0x10000,o); fclose(o);
      snprintf(p,sizeof p,"%s/f%04d.cram",dir,fr); o=fopen(p,"wb"); fwrite(cram,2,0x80,o); fclose(o);
    }
  }
  snprintf(p,sizeof p,"%s/final.ppm",dir); dump_ppm(p);
  snprintf(p,sizeof p,"%s/final.vram",dir); FILE*o=fopen(p,"wb"); fwrite(vram,1,0x10000,o); fclose(o);
  snprintf(p,sizeof p,"%s/final.cram",dir); o=fopen(p,"wb"); fwrite(cram,2,0x80,o); fclose(o);
  if(g_cap){fclose(g_cap);g_cap=0;}
  printf("decompression captures: %u\n", g_hits);
  return 0;
}
