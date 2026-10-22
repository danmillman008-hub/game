#!/bin/sh
# Build the headless Mega Drive capture harness.
#
#   ./build.sh [/path/to/Genesis-Plus-GX]
#
# If no source tree is given, Genesis Plus GX is downloaded (needs network once)
# into build/gpgx and patched by patches/gpgx_capture_hooks.py.
# Produces: build/mdcap  (and build/mdrun for plain snapshots)
#
# The emulator is used ONLY as a measuring instrument: it runs the unmodified
# ROM so that the ROM's own decompressor can be observed. No emulator code or
# output is shipped with the reconstruction.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
BUILD="$HERE/build"
mkdir -p "$BUILD"

if [ -n "$1" ]; then
  SRC="$1"
else
  SRC="$BUILD/gpgx/Genesis-Plus-GX-master"
  if [ ! -d "$SRC" ]; then
    mkdir -p "$BUILD/gpgx"
    echo "downloading Genesis Plus GX..."
    curl -sL https://codeload.github.com/libretro/Genesis-Plus-GX/tar.gz/refs/heads/master \
      -o "$BUILD/gpgx/src.tgz"
    tar xzf "$BUILD/gpgx/src.tgz" -C "$BUILD/gpgx"
  fi
fi

python3 "$HERE/patches/gpgx_capture_hooks.py" "$SRC"

CFLAGS="-O2 -DLSB_FIRST -DBYTE_ORDER=LITTLE_ENDIAN -DMAXROMSIZE=33554432 \
 -DUSE_16BPP_RENDERING -DFRONTEND_SUPPORTS_RGB565 -D__LIBRETRO__ -DUSE_LIBRETRO_VFS \
 -DHAVE_YM3438_CORE -DHAVE_OPLL_CORE -I$SRC/libretro/deps/libchdr/include \
 -I$SRC/libretro/deps/lzma-19.00/include -I$SRC/libretro/deps/zlib-1.2.11 \
 -I$SRC/libretro/deps/zstd/lib -I$SRC/core -I$SRC/core/z80 -I$SRC/core/m68k \
 -I$SRC/core/ntsc -I$SRC/core/sound -I$SRC/core/input_hw -I$SRC/core/cd_hw \
 -I$SRC/core/cart_hw -I$SRC/core/cart_hw/svp -I$SRC/libretro \
 -I$SRC/libretro/libretro-common/include"

if [ ! -f "$SRC/genesis_plus_gx_libretro.so" ]; then
  ( cd "$SRC" && make -f Makefile.libretro -j"$(nproc 2>/dev/null || echo 2)" >/dev/null )
fi

# The instruction hook is a compile-time option; rebuild the two objects that use it.
HOOKFLAGS="-DHOOK_CPU -I$SRC/core/debug"
for f in "$SRC/core/m68k/m68kcpu.c" "$SRC/core/vdp_ctrl.c"; do
  cc $CFLAGS $HOOKFLAGS -c "$f" -o "${f%.c}.o"
done

OBJS=$(ls "$SRC"/core/*.o "$SRC"/core/z80/*.o "$SRC"/core/m68k/*.o "$SRC"/core/ntsc/*.o \
  "$SRC"/core/sound/*.o "$SRC"/core/sound/tremor/*.o "$SRC"/core/input_hw/*.o \
  "$SRC"/core/cart_hw/*.o "$SRC"/core/cart_hw/svp/*.o "$SRC"/core/cd_hw/*.o \
  "$SRC"/libretro/libretro.o "$SRC"/libretro/deps/libchdr/src/*.o \
  "$SRC"/libretro/deps/lzma-19.00/src/*.o "$SRC"/libretro/deps/zlib-1.2.11/*.o \
  "$SRC"/libretro/deps/zstd/lib/common/*.o "$SRC"/libretro/deps/zstd/lib/decompress/*.o \
  "$SRC"/libretro/libretro-common/streams/*.o "$SRC"/libretro/libretro-common/compat/*.o \
  "$SRC"/libretro/libretro-common/encodings/*.o "$SRC"/libretro/libretro-common/file/*.o \
  "$SRC"/libretro/libretro-common/lists/*.o "$SRC"/libretro/libretro-common/memmap/*.o \
  "$SRC"/libretro/libretro-common/string/*.o "$SRC"/libretro/libretro-common/vfs/*.o \
  "$SRC"/libretro/libretro-common/cdrom/*.o)

cc -O2 -I"$SRC/libretro" -I"$SRC/libretro/libretro-common/include" \
   -I"$SRC/core" -I"$SRC/core/debug" -I"$SRC/core/m68k" \
   -c "$HERE/frontend.c" -o "$BUILD/frontend.o"
cc -O2 -I"$SRC/libretro/libretro-common/include" -I"$SRC/core/debug" -I"$SRC/core" \
   -I"$SRC/core/m68k" -c "$HERE/decomp_hook.c" -o "$BUILD/decomp_hook.o"
cc -o "$BUILD/mdcap" "$BUILD/frontend.o" "$BUILD/decomp_hook.o" \
   $OBJS -lm
echo "built $BUILD/mdcap"
