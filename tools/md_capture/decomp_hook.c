#include <stdio.h>
#include <stdint.h>
#include "cpuhook.h"
#include "m68k.h"

extern unsigned int m68k_get_reg(m68k_register_t reg);
extern int md_capture_active;
extern unsigned char *md_capture_ptr;
extern unsigned md_capture_len;

#define ENTRY0 0x008192
#define ENTRY1 0x0081A4

static int armed = 0;
static uint8_t buf[0x8000];
unsigned g_frame = 0;
FILE *g_cap = 0;
unsigned g_hits = 0;

void capture_hook(hook_type_t type, int width, unsigned address, unsigned value)
{
  (void)width; (void)value;
  if (type != HOOK_M68K_E) return;
  if (address == ENTRY0 || address == ENTRY1) {
    armed = 1;
    md_capture_ptr = buf; md_capture_len = 0; md_capture_active = 1;
    return;
  }
  if (armed && (address < 0x008192 || address > 0x0083FF)) {
    armed = 0; md_capture_active = 0;
    if (md_capture_len > 64 && g_cap) {
      uint32_t hdr[3] = { g_frame, (uint32_t)m68k_get_reg(M68K_REG_A0), md_capture_len };
      fwrite(hdr, 4, 3, g_cap);
      fwrite(buf, 1, md_capture_len, g_cap);
      g_hits++;
    }
  }
}

void (*cpu_hook)(hook_type_t type, int width, unsigned int address, unsigned int value) = 0;
void set_cpu_hook(void(*hook)(hook_type_t type, int width, unsigned int address, unsigned int value))
{ cpu_hook = hook; }
