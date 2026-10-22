/* Headless MD frontend with VDP write capture.
   usage: mdrun2 rom frames outprefix [events.txt]
   events.txt lines: <frame> <button-or-key>   e.g. "600 START", "700 RIGHT+" ... */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "libretro.h"

extern uint16_t vram[0x8000];
extern uint16_t cram[0x80];
extern uint16_t sat[0x400];
extern uint8_t work_ram[0x10000];

static int16_t fb[720*576];
static unsigned fb_w=320, fb_h=224; static int fb_pitch=0, fb_fmt=0;

#define MAXEV 512
static struct { int frame; unsigned id; int down; } ev[MAXEV];
static int nev=0;

static bool env(unsigned cmd, void *data) {
  switch (cmd) {
    case RETRO_ENVIRONMENT_SET_PIXEL_FORMAT: fb_fmt=*(const int*)data; return true;
    case RETRO_ENVIRONMENT_GET_VARIABLE: { struct retro_variable *v=data; v->value=NULL; return false; }
    case RETRO_ENVIRONMENT_GET_VARIABLE_UPDATE: *(bool*)data=false; return true;
    case RETRO_ENVIRONMENT_SET_VARIABLES: return true;
    case RETRO_ENVIRONMENT_GET_LOG_INTERFACE: return false;
    case RETRO_ENVIRONMENT_SET_SYSTEM_AV_INFO: return true;
    case RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY:
    case RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY: *(const char**)data="."; return true;
    default: return false;
  }
}
static void video_cb(const void *d, unsigned w, unsigned h, size_t p){ fb_w=w; fb_h=h; fb_pitch=(int)p; if(d) memcpy(fb,d,p*h); }
static void audio_cb(int16_t l,int16_t r){(void)l;(void)r;}
static size_t audio_batch_cb(const int16_t *d,size_t f){(void)d;return f;}
static void input_poll_cb(void){}
static int16_t input_state_cb(unsigned port,unsigned dev,unsigned idx,unsigned id){
  (void)dev;(void)idx; if(port) return 0;
  for(int i=0;i<nev;i++) if(ev[i].id==id && ev[i].down) return 1;
  return 0;
}
static void (*input_state2)(unsigned,unsigned,unsigned,unsigned);

static unsigned btn_id(const char *s){
  if(!strcmp(s,"UP")) return RETRO_DEVICE_ID_JOYPAD_UP;
  if(!strcmp(s,"DOWN")) return RETRO_DEVICE_ID_JOYPAD_DOWN;
  if(!strcmp(s,"LEFT")) return RETRO_DEVICE_ID_JOYPAD_LEFT;
  if(!strcmp(s,"RIGHT")) return RETRO_DEVICE_ID_JOYPAD_RIGHT;
  if(!strcmp(s,"A")) return RETRO_DEVICE_ID_JOYPAD_A;
  if(!strcmp(s,"B")) return RETRO_DEVICE_ID_JOYPAD_B;
  if(!strcmp(s,"C")) return RETRO_DEVICE_ID_JOYPAD_Y;
  if(!strcmp(s,"START")) return RETRO_DEVICE_ID_JOYPAD_START;
  if(!strcmp(s,"X")) return RETRO_DEVICE_ID_JOYPAD_X;
  return 0;
}

int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage: %s rom frames outprefix [events]\n",argv[0]);return 2;}
  int frames=atoi(argv[2]); const char *pfx=argv[3];
  if(argc>4){
    FILE *e=fopen(argv[4],"r"); char b[64]; int fr;
    while(e && fscanf(e,"%d %63s",&fr,b)==2){
      if(nev>=MAXEV) break;
      ev[nev].frame=fr; ev[nev].id=btn_id(b); ev[nev].down=1; nev++;
    }
    if(e) fclose(e);
    /* each press lasts 4 frames */
    for(int i=nev-1;i>=0;i--){ if(nev<MAXEV){ ev[nev]=ev[i]; ev[nev].frame=ev[i].frame+4; ev[nev].down=0; nev++; } }
  }
  retro_set_environment(env); retro_set_video_refresh(video_cb);
  retro_set_audio_sample(audio_cb); retro_set_audio_sample_batch(audio_batch_cb);
  retro_set_input_poll(input_poll_cb); retro_set_input_state(input_state_cb);
  retro_init();
  FILE *f=fopen(argv[1],"rb"); fseek(f,0,SEEK_END); long sz=ftell(f); fseek(f,0,SEEK_SET);
  uint8_t *rom=malloc(sz); if(fread(rom,1,sz,f)!=(size_t)sz) return 3; fclose(f);
  struct retro_game_info gi={argv[1],rom,(size_t)sz,NULL};
  if(!retro_load_game(&gi)){fprintf(stderr,"load_game failed\n");return 4;}

  static uint16_t pvram[0x8000], pcram[0x80], psat[0x400];
  char p[512];
  snprintf(p,sizeof p,"%s.vlog",pfx); FILE *vlog=fopen(p,"wb");
  snprintf(p,sizeof p,"%s.clog",pfx); FILE *clog=fopen(p,"wb");
  int nv=0, nc=0;
  retro_run();
  memcpy(pvram,vram,sizeof vram); memcpy(pcram,cram,sizeof cram); memcpy(psat,sat,sizeof sat);

  for(int fr=0; fr<frames; fr++){
    for(int i=0;i<nev;i++) ev[i].down = (fr>=ev[i].frame);
    retro_run();
    for(int a=0;a<0x8000;a++) if(vram[a]!=pvram[a]){
      uint32_t r=((uint32_t)fr<<16)|(uint32_t)a; fwrite(&r,4,1,vlog); fwrite(&vram[a],2,1,vlog); pvram[a]=vram[a]; nv++;
    }
    for(int a=0;a<0x80;a++) if(cram[a]!=pcram[a]){
      uint32_t r=((uint32_t)fr<<16)|(uint32_t)a; fwrite(&r,4,1,clog); fwrite(&cram[a],2,1,clog); pcram[a]=cram[a]; nc++;
    }
    memcpy(psat,sat,sizeof sat);
    /* periodic framebuffer dumps */
    if(frames>0 && (fr%150)==149){
      snprintf(p,sizeof p,"%s.f%04d.ppm",pfx,fr);
      FILE *o=fopen(p,"wb"); fprintf(o,"P6\n%u %u\n255\n",fb_w,fb_h);
      for(unsigned y=0;y<fb_h;y++) for(unsigned x=0;x<fb_w;x++){
        uint16_t c=((uint16_t*)fb)[y*(fb_pitch/2)+x];
        unsigned char px[3]={(unsigned char)(((c>>11)&0x1f)*255/31),(unsigned char)(((c>>5)&0x3f)*255/63),(unsigned char)((c&0x1f)*255/31)};
        fwrite(px,1,3,o);
      }
      fclose(o);
    }
  }
  fclose(vlog); fclose(clog);
  snprintf(p,sizeof p,"%s.final.ppm",pfx);
  FILE *o=fopen(p,"wb"); fprintf(o,"P6\n%u %u\n255\n",fb_w,fb_h);
  for(unsigned y=0;y<fb_h;y++) for(unsigned x=0;x<fb_w;x++){
    uint16_t c=((uint16_t*)fb)[y*(fb_pitch/2)+x];
    unsigned char px[3]={(unsigned char)(((c>>11)&0x1f)*255/31),(unsigned char)(((c>>5)&0x3f)*255/63),(unsigned char)((c&0x1f)*255/31)};
    fwrite(px,1,3,o);
  }
  fclose(o);
  snprintf(p,sizeof p,"%s.final.vram",pfx); o=fopen(p,"wb"); fwrite(vram,2,0x8000,o); fclose(o);
  snprintf(p,sizeof p,"%s.final.cram",pfx); o=fopen(p,"wb"); fwrite(cram,2,0x80,o); fclose(o);
  snprintf(p,sizeof p,"%s.final.sat",pfx); o=fopen(p,"wb"); fwrite(sat,2,0x400,o); fclose(o);
  snprintf(p,sizeof p,"%s.final.ram",pfx); o=fopen(p,"wb"); fwrite(work_ram,1,0x10000,o); fclose(o);
  printf("%s: %d frames, %d vram writes, %d cram writes\n",pfx,frames,nv,nc);
  return 0;
}
