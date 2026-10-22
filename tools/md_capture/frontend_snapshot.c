/* Headless Mega Drive frontend: runs N frames, dumps framebuffer + VRAM + CRAM + SAT. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "libretro.h"

/* globals from vdp_ctrl.c / vdp_render.c */
extern uint16_t vram[0x8000];
extern uint16_t cram[0x80];
extern uint16_t sat[0x400];
extern uint8_t work_ram[0x10000];
extern uint16_t *pixel;
extern int vdp_pixels;

static int16_t fb[720*576];
static unsigned fb_w=320, fb_h=224;
static int fb_pitch=0;
static int fb_fmt=0;

static bool env(unsigned cmd, void *data) {
  switch (cmd) {
    case RETRO_ENVIRONMENT_SET_PIXEL_FORMAT: fb_fmt = *(const int*)data; return true;
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
static void video_cb(const void *data, unsigned w, unsigned h, size_t pitch) {
  fb_w=w; fb_h=h; fb_pitch=(int)pitch;
  if (data) memcpy(fb, data, pitch*h);
}
static void audio_cb(int16_t l, int16_t r){(void)l;(void)r;}
static size_t audio_batch_cb(const int16_t *d, size_t f){(void)d; return f;}
static void input_poll_cb(void){}
static int16_t input_state_cb(unsigned p, unsigned d, unsigned i, unsigned id){(void)p;(void)d;(void)i;(void)id;return 0;}
static void dummy(void){}

static void put_png_pixels(const char *path); /* fwd */

int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr,"usage: %s rom.bin frames [outprefix]\n", argv[0]); return 2; }
  int frames = atoi(argv[2]);
  const char *prefix = argc>3 ? argv[3] : "frame";

  retro_set_environment(env);
  retro_set_video_refresh(video_cb);
  retro_set_audio_sample(audio_cb);
  retro_set_audio_sample_batch(audio_batch_cb);
  retro_set_input_poll(input_poll_cb);
  retro_set_input_state(input_state_cb);
  retro_init();

  FILE *f = fopen(argv[1],"rb"); fseek(f,0,SEEK_END); long sz=ftell(f); fseek(f,0,SEEK_SET);
  uint8_t *rom = malloc(sz); if (fread(rom,1,sz,f)!=(size_t)sz) { fprintf(stderr,"read fail\n"); return 3; }
  fclose(f);
  struct retro_game_info gi = { argv[1], rom, (size_t)sz, NULL };
  if (!retro_load_game(&gi)) { fprintf(stderr,"load_game failed\n"); return 4; }
  retro_run(); /* first frame after reset */

  for (int i=0;i<frames;i++) retro_run();

  char p[512];
  snprintf(p,sizeof p,"%s.ppm", prefix);
  FILE *o=fopen(p,"wb");
  fprintf(o,"P6\n%u %u\n255\n", fb_w, fb_h);
  for (unsigned y=0;y<fb_h;y++) for (unsigned x=0;x<fb_w;x++) {
    uint16_t c = ((uint16_t*)fb)[y*(fb_pitch/2)+x];
    /* RGB565 -> RGB888 */
    unsigned r=(c>>11)&0x1f, g=(c>>5)&0x3f, b=c&0x1f;
    unsigned char px[3] = { (unsigned char)(r*255/31), (unsigned char)(g*255/63), (unsigned char)(b*255/31) };
    fwrite(px,1,3,o);
  }
  fclose(o);

  snprintf(p,sizeof p,"%s.vram", prefix);
  o=fopen(p,"wb"); fwrite(vram,2,0x8000,o); fclose(o);
  snprintf(p,sizeof p,"%s.cram", prefix);
  o=fopen(p,"wb"); fwrite(cram,2,0x80,o); fclose(o);
  snprintf(p,sizeof p,"%s.sat", prefix);
  o=fopen(p,"wb"); fwrite(sat,2,0x400,o); fclose(o);
  snprintf(p,sizeof p,"%s.ram", prefix);
  o=fopen(p,"wb"); fwrite(work_ram,1,0x10000,o); fclose(o);

  printf("dumped %s  %ux%u fmt=%d\n", p, fb_w, fb_h, fb_fmt);
  retro_unload_game(); retro_deinit();
  return 0;
}
