# Architectural Diagrams
### Streets of Rage / Bare Knuckle (Mega Drive, 1991)

All diagrams are derived from the disassembly; the source address of each block is given so the diagram can be re-verified.

---

## D1. Boot / reset timeline
```
 reset ─► $000208  ┌ TMSS off ($A14000 = $00)
                   ├ read $A10001 (version) → if ≥1, write 'SEGA' to $A14000
                   ├ 24 × (byte → $C00004)          ; VDP registers from $0002A4
                   ├ Z80: $A11100=0100, $A11200=0100, copy stub, release
                   ├ clear 64 KiB RAM / CRAM / VSRAM
                   ├ PSG mute (4 × $11(a3))
                   └ bra $000308
                     │
          $000308  ┌─ $FF44 = $A10001 & $C0
                   ├─ if ($A1000D bit6 == 0): sum16($200..$7FFFF) vs $018E
                   │      mismatch ─► $000412: CRAM[0] = $000E (RED), halt
                   ├─ $007FB8  VDP+DMA+Z80 reset, VRAM clear ($8F01/$93FF/$94FF)
                   ├─ $00804C  Z80 RAM clear
                   ├─ $00805A  Z80 driver install
                   ├─ $01061C  Kosinski($0795A2) → $FF7000 → Z80 $0000 (7,861 B)
                   ├─ $010526  scroll buffers = $FF00
                   ├─ $FF00 = 0
                   └─ jmp $0003A2
```

## D2. Main loop and frame ownership
```
        ┌──────────────────────────── MAIN LOOP  $0003A2 ────────────────────────────┐
        │  d1 = ($FF00)                                                              │
        │  target = ($03BA + d1)                                                     │
        │  jsr (target)                    ← one of 22 master states                 │
        │  jsr $010502                     ← WAIT FOR FRAME                         │
        └───────────────────────────────────┬────────────────────────────────────────┘
                                            │  $FA00 = 1 ; sr = $2500
        ┌───────────────────────────────────▼────────────────────────────────────────┐
        │  V-BLANK ISR  $019D16                                                     │
        │   if ($FA00 == 0) → lag branch $01A088 (sprites only)                     │
        │   VSRAM ← camera Y ($E00E / $E10E)                                        │
        │   if ($FA01 bit0): BUSREQ; DMA $F400 → CRAM; release                      │
        │   switch ($FF06) { 0,1,2,3,4,5 }  ; VDP register programs                 │
        │   $FB06-- ; $FB08++                                                       │
        │   pads → $FC04/$FC05         ($00810C)                                    │
        │   SAT $F600 → VDP            ($008510)                                    │
        │   sound tick                 ($072914)                                    │
        │   $FA00 = 0 ; rte                                                         │
        └───────────────────────────────────────────────────────────────────────────┘
```

## D3. Gameplay frame pipeline (`$01087A`) — literal order
```
 ① $011A36  pause debounce ($FB52)                 ─┐
 ② $010D2E  pause / round-end trigger              │  may short-circuit
 ③ $010C88  background columns + H-scroll (90-tick)│  the whole frame
 ④ $0115CC  2P scroll arbitration + palette        │
 ⑤ $011B4C  spawn script ($FC14) ──► actor pool    │
 ⑥ $0117FC  life/wave tile stream                  │
 ⑦ $0112F2  per-round dispatch ($FF02 0..7)        │
 ⑧ $011210  palette cycle → $F400                  │
 ⑨ $00AD8E  ACTOR PASS  ◄── see D4                 │
 ⑩ $011346  parallax / sky columns                 │
 ⑪ $017FC2  scripted FX (palette/DMA swap)         │
 ⑫ $0084BA  SAT stream kickoff                     │
 ⑬ $000436  police special subsystem               ─┘
```

## D4. Actor pass internals (`$00AD8E`)
```
 $B800 (P1) ─┐
 $B880 (P2) ─┴─► handler(type) ─► activation test ($00B132) ─► bucket insert ($00AE4C)
                                   │                                 │
                                   │                                 ▼
                                   │                     $E200..$E9DF (64 × $20)
                                   │                     15 entries max / bucket
 $B900 (32 slots) ─► handler ─► activation ─► bucket insert
 $C900 (24 slots) ─► handler ─► (exempt)  ─► bucket insert
                                   │
 $010514  ◄── one extra frame wait ┘
                                   │
                                   ▼
                 walk $E9E0 → $E200 ; per bucket insertion-sort on (+$14, +$01 bit7)
                                   │
                                   ▼
                 sprite builder $00AF46 ─► 8-byte SAT records → $F600
                                            budget 79 ($FA03), cull by screen Y
                                   │
                                   ▼
                 $0084BA → $008510 → VDP SAT (chunked $A0 bytes)
```

## D5. Actor lifecycle
```
 spawn req ($007EBE/$007E92/$007EEA/$0082D6)
        │ free slot found (type == 0)
        ▼
 [ALLOC] +$00=type, +$04=anim bank, +$10/+$14/+$18 = pos
        │
        ▼
 [ACTIVE] ── handler each frame ──► physics ──► boxes ──► damage ──► reaction
        │                                                          │
        │ camera cull                                              │ HP ≤ 0
        ▼                                                          ▼
 [DESPAWN $00B17A]  unlink + 32-long wipe          [DEATH $009CFC..] census--, score+=, wipe
```

## D6. Memory map (work RAM)
```
 $FF0000 ████ master state / round / VBlank mode / player mask
 $FF0020 ████ lives (BCD) · police stock · pause request
 $FF0040 ████ PRNG state                $FF0044 region latch
 $FF004A ████ high-score table (10 × 12 B)
 $FF00C4 ████ name-entry codes P1/P2 ($FF0C / $FF14)
 $FF1A   ████ police style · $FF20/23 lives · $FF35 bonus index
 $DE00   ████ round/wave script state (44 B)
 $DD80   ████ palette-stream state
 $DCD0   ████ SAT stream state
 $E000   ████ CAMERA A   (256 B)          $E100 ████ CAMERA B
 $E200   ████ Y-SORT (64 × 32 B = 2 KiB)  $EA00 ████ plane A sub-structs
 $EB20   ████ plane B sub-structs         $EC40/$ECE0 scroll cursors
 $EE00   ████ palette-cycle table (5 × 14 B)
 $F000   ████ sound requests ($F00A–$F00C = 3 SFX slots)
 $F040   ████ 5 × FM channel ($30 each)   $F130 DAC · $F160 3 × PSG
 $F400   ████ CRAM shadow A (64 W)        $F480 CRAM shadow B
 $F500   ████ wave/stream state · $F502/$F508 active attacker ptrs
 $F600   ████ SAT SHADOW (80 × 8 B)       $F9FF
 $FA00   ████ frame handshake · flags · timers · census ($FA60..)
 $FB00   ████ scroll/HUD state · attacker list ($FB22) · $FB56 scratch
 $FC00   ████ VDP cmd pair · pads · script PC · terrain tables ($FC34/$FC38)
 $FC40   ████ HUD digit buffers
 $FF5000 ████ H-scroll table (built by $0190E0)
 $FF7000 ████ decompression staging (Z80 driver)
 $FF8000 ████ sprite patches / timer digits
 $FF9000 ████ round-timer digits
 $FFA000 ████ TERRAIN plane (2 × 4-bit tiles per byte)
 $FFFF00 ████ initial stack top (globals live below $FFFFFF… above the stack)
```

## D7. Audio signal path
```
 game code ──► $01069E (SFX request, 3 slots at $F00A)
                      │
                      ▼
              $072D08  command arbiter (priority table $072824)
                      │  winner → $F009
        ┌─────────────┼──────────────┬──────────────────┐
        ▼             ▼              ▼                  ▼
   $81–$91 DAC   $A0–$CF chan    $E0–$E3 transport   ≥$E4 dropped
        │             │              │
        └─────────────┴──────────────┘
                      ▼
              $072914  per-frame sequencer (68k!)
                 · per-channel stream pointer (+$04)
                 · duration countdown (+$0E), note decode, pitch/LFO
                 · computes final register bytes
                      │  BUSREQ on
                      ▼
              write to Z80 RAM $1FF0–$1FFF  ($A01FFx)
                      │  BUSREQ off
                      ▼
              Z80 driver (7,936 B)  ──► YM2612 ($4000/$4001)
                                    ──► SN76489 ($7F11)
                                    ──► Δ-PCM DAC (companded 4-bit)
```

## D8. Data-flow / dependency graph
(see `DOSSIER §24.1` for the annotated version)

## D9. State-machine summary
```
 MASTER ($FF00, 22 states)
   ├─ $00 boot ─► $02 attract ─┬─► $04 reset ─► $06 start ─► $08/$0A select timer
   │                           └─► (demo loop)
   ├─ $10 char-select init ─► $12 char select
   ├─ $14 round load ─► $16 GAMEPLAY ─┬─► $18/$1A round clear ─► $14 (next)
   │                                  ├─► $0C round intro
   │                                  └─► $1C/$1E game over / continue
   ├─ $20/$22 name entry ─► $24/$26 ending ─► $28 reset ─► $2A transition ─► $14
   └─ (all transitions are $FF00 ± 2)
```
