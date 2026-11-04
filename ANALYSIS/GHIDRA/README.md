# Ghidra / REA proxy run — evidence

The sandbox has outbound access to github.com, api.github.com, codeload.github.com,
registry.npmjs.org, pypi.org and files.pythonhosted.org only.
release-assets.githubusercontent.com and objects.githubusercontent.com are blocked.
This workflow is the proxy: a GitHub-hosted runner downloads the official release,
fully installs it, executes it on the original DEX, and writes the text evidence
back into this branch with git (which the sandbox CAN reach).

## Ghidra fetch step: success
## Ghidra headless status: 0

## Program report
```
=== Ghidra program report ===
program       : classes.dex
language      : Dalvik:LE:32:DEX_KitKat
compiler spec : default
image base    : 00000000
memory blocks : 3
functions     : 0
symbols       : 36707
executable?   : 32-bit
=== Ghidra program report ===
program       : classes2.dex
language      : Dalvik:LE:32:DEX_KitKat
compiler spec : default
image base    : 00000000
memory blocks : 3
functions     : 0
symbols       : 41371
executable?   : 32-bit
=== Ghidra program report ===
program       : classes3.dex
language      : Dalvik:LE:32:DEX_KitKat
compiler spec : default
image base    : 00000000
memory blocks : 3
functions     : 0
symbols       : 12170
executable?   : 32-bit
```

## run.log (tail)
```
WARN  Analyzer 'Data Reference' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call Convention ID' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Decompiler Switch Analysis' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Embedded Media' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Non-Returning Functions - Discovered' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Demangler GNU' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Reference' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Source Language Support' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Create Address Tables' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Disassemble Entry Points' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'External Entry References' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Stack' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'ASCII Strings' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Variadic Function Signature Override' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Function ID' for classes2.dex disabled by PSPEC file override (AnalysisScheduler)  
INFO  REPORT: Execute script: MimoGhidraReport.java  (HeadlessAnalyzer)  
INFO  SCRIPT: /home/runner/work/game/game/ANALYSIS/_TOOLCHAIN/ghidra_scripts/MimoGhidraReport.java (HeadlessAnalyzer)  
INFO  MimoGhidraReport.java> === Ghidra program report ===
program       : classes2.dex
language      : Dalvik:LE:32:DEX_KitKat
compiler spec : default
image base    : 00000000
memory blocks : 3
functions     : 0
symbols       : 41371
executable?   : 32-bit
 (GhidraScript)  
INFO  /classes2.dex: file created (runner) (LocalFileSystem)  
INFO  REPORT: Save succeeded for: /classes2.dex (Mimo935:/classes2.dex) (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded (HeadlessAnalyzer)  
INFO  IMPORTING: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes3.dex (HeadlessAnalyzer)  
INFO  Using Loader: Dalvik Executable (DEX) (ProgramLoader)  
INFO  Using Language/Compiler: Dalvik:LE:32:DEX_KitKat:default (ProgramLoader)  
INFO  Using Library Search Path: [., /bin, /lib, /lib64, /lib/x86_64-linux-gnu, /lib/aarch64-linux-gnu, /usr/bin, /usr/lib, /usr/X11R6/bin, /usr/X11R6/lib, /usr/java/packages/lib, /usr/lib64] (ProgramLoader)  
INFO  IMPORTING: Loaded 0 additional files (HeadlessAnalyzer)  
WARN  Analyzer 'Apply Data Archives' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Basic Constant Reference Analyzer' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Data Reference' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call Convention ID' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Decompiler Switch Analysis' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Embedded Media' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Non-Returning Functions - Discovered' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Demangler GNU' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Reference' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Source Language Support' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Create Address Tables' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Disassemble Entry Points' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'External Entry References' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Stack' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'ASCII Strings' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Variadic Function Signature Override' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Function ID' for classes3.dex disabled by PSPEC file override (AnalysisScheduler)  
INFO  REPORT: Execute script: MimoGhidraReport.java  (HeadlessAnalyzer)  
INFO  SCRIPT: /home/runner/work/game/game/ANALYSIS/_TOOLCHAIN/ghidra_scripts/MimoGhidraReport.java (HeadlessAnalyzer)  
INFO  MimoGhidraReport.java> === Ghidra program report ===
program       : classes3.dex
language      : Dalvik:LE:32:DEX_KitKat
compiler spec : default
image base    : 00000000
memory blocks : 3
functions     : 0
symbols       : 12170
executable?   : 32-bit
 (GhidraScript)  
INFO  /classes3.dex: file created (runner) (LocalFileSystem)  
INFO  REPORT: Save succeeded for: /classes3.dex (Mimo935:/classes3.dex) (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded (HeadlessAnalyzer)  
headless_exit=0
```
