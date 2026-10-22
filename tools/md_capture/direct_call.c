/* Run the ROM's own graphics decompressor inside the emulated 68000.
   usage: mdcall rom src_hex [variant 0|1] [outprefix]  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "libretro.h"
#include "m68k.h"

extern uint8_t vram[0x10000];
extern uint8_t work_ram[0x10000];
extern void vdp_68k_ctrl_w(unsigned int data);
extern int md_capture_active; extern uint8_t *md_capture_ptr; extern unsigned md_capture_len;
static uint8_t capbuf[0x4000];

static int16_t fb[720*576]; static unsigned W=320,H=224; static int PITCH=0;
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
static int16_t istate(unsigned a,unsigned b,unsigned c,unsigned d){(void)a;(void)b;(void)c;(void)d;return 0;}

int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: %s rom src_hex [variant] [out]\n",argv[0]);return 2;}
  unsigned src=strtoul(argv[2],0,16);
  int variant = argc>3?atoi(argv[3]):0;
  const char *out = argc>4?argv[4]:"/tmp/call";
  retro_set_environment(env); retro_set_video_refresh(vid);
  retro_set_audio_sample(aud); retro_set_audio_sample_batch(audb);
  retro_set_input_poll(ipoll); retro_set_input_state(istate);
  retro_init();
  FILE *f=fopen(argv[1],"rb"); fseek(f,0,SEEK_END); long sz=ftell(f); fseek(f,0,SEEK_SET);
  uint8_t *rom=malloc(sz); if(fread(rom,1,sz,f)!=(size_t)sz)return 3; fclose(f);
  /* ROM is left untouched; the decompressor's output is captured at the
     VDP data port by a hook in vdp_ctrl.c. */
  fprintf(stderr,"[dbg] rom=%ld bytes, patched lea-c00000 sites\n",sz);
  struct retro_game_info gi={argv[1],rom,(size_t)sz,NULL};
  if(!retro_load_game(&gi)){fprintf(stderr,"load failed\n");return 4;}
  for(int i=0;i<20;i++) retro_run();   /* let the system settle */
  fprintf(stderr,"[dbg] settled, PC=$%06X\n", m68k_get_reg(M68K_REG_PC));

  const unsigned DEST = 0x8000;        /* RAM scratch (patched target) */
  const unsigned SENT = 0x00FFF000;
  work_ram[0xF000]=0x60; work_ram[0xF001]=0xFE;   /* bra.s * = park here */
  work_ram[0xFFFC]=0x00; work_ram[0xFFFD]=0xFF; work_ram[0xFFFE]=0xF0; work_ram[0xFFFF]=0x00;
  /* return address on stack */
  /* return address ($FFF000) pushed at the top of our stack */

  memset(&work_ram[DEST], 0, 0x4000);
  memset(capbuf, 0, sizeof capbuf);
  md_capture_ptr = capbuf; md_capture_len = 0; md_capture_active = 1;

  m68k_set_reg(M68K_REG_SR, 0x2700);
  m68k_set_reg(M68K_REG_A0, src);
  m68k_set_reg(M68K_REG_A7, 0x00FFF000);
  m68k_set_reg(M68K_REG_PC, variant ? 0x0081A4 : 0x008192);

  fprintf(stderr,"[dbg] regs set, entering loop\n");
  long steps=0; int dbg = getenv("DBG")!=NULL; unsigned ring[24]; int ri=0;
  unsigned stopat = getenv("STOPAT") ? strtoul(getenv("STOPAT"),0,16) : 0;
  unsigned cyc = (unsigned)m68k_cycles() + 1000;
  while(m68k_get_reg(M68K_REG_PC)!=SENT && (!stopat || m68k_get_reg(M68K_REG_PC)!=stopat) && steps<3000000){ cyc += 16; m68k_run(cyc); steps++; ring[ri++ & 23] = m68k_get_reg(M68K_REG_PC);
  if (dbg && (steps % 200000)==0) fprintf(stderr,"  step %ld PC=$%06X A0=$%06X A4=$%06X\n",steps,m68k_get_reg(M68K_REG_PC),m68k_get_reg(M68K_REG_A0),m68k_get_reg(M68K_REG_A4)); }
  printf("stopped after %ld steps, PC=$%06X\n", steps, m68k_get_reg(M68K_REG_PC));

  if (dbg) { printf("last PCs:"); for(int i=0;i<24;i++) printf(" $%06X", ring[(ri+i)&23]); printf("\n"); }
  printf("A0 now $%06X D6=$%04X\n", m68k_get_reg(M68K_REG_A0), m68k_get_reg(M68K_REG_D6));
  md_capture_active = 0;
  fprintf(stderr,"[dbg] loop done, captured %u bytes\n", md_capture_len);
  char p[512];
  snprintf(p,sizeof p,"%s.vram",out); FILE *o=fopen(p,"wb"); fwrite(vram,1,0x10000,o); fclose(o);
  snprintf(p,sizeof p,"%s.ram",out); o=fopen(p,"wb"); fwrite(work_ram,1,0x10000,o); fclose(o);
  snprintf(p,sizeof p,"%s.tiles",out); o=fopen(p,"wb"); fwrite(capbuf,1,md_capture_len,o); fclose(o);
  /* how much of VRAM scratch was touched: report last non-zero word from DEST */
  printf("captured %u bytes\n", md_capture_len);
  return 0;
}
