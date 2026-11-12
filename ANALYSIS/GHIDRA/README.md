# Ghidra / REA chain — corrected run

- run 43239869814 / commit de65c4a8f8a93716404b16b214293043af21c08e / 2026-11-12T14:45:44Z
- Ghidra fetch: success; coverage: success; auto analysis: success; REA doctor: success
- corrections applied: ALL 12 DEX imported (not 3); Auto Analysis ENABLED on ALL 12 DEX (no -noanalysis); full JDK 21 for REA separate from JDK 25 for Ghidra

## All-12 DEX coverage
```
DEX classes.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=36707 functions=0 image_base=00000000
DEX classes10.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes11.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes12.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=451 functions=0 image_base=00000000
DEX classes2.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=41371 functions=0 image_base=00000000
DEX classes3.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=12170 functions=0 image_base=00000000
DEX classes4.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes5.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes6.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes7.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes8.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
DEX classes9.dex language=Dalvik:LE:32:DEX_KitKat memory_blocks=3 symbols=10 functions=0 image_base=00000000
```

## Control flow / function report
```
=== PROGRAM classes.dex language=Dalvik:LE:32:DEX_KitKat functions=54530 symbols=681976 memory_blocks=3 ===
-- DEX string cross references (field names -> owning functions) --
  STR string_data::_physicalPixelDisplaySizeRatio=1.0_rotation=0_offsetX=0_offsetY=0_scale=1.0} @000019e8
    [xrefs_shown=0]
  STR string_data::_scrollPosition= @00001a50
    [xrefs_shown=0]
  STR string_data::_scrollPositionX= @00001a54
    [xrefs_shown=0]
  STR string_data::()Lcom/getmimo/ui/common/SpringAnimatingProgressBar; @0000250c
    [xrefs_shown=0]
  STR string_data::(Landroid/view/View;Lapp/rive/semantics/SemanticTreeModel;Lo70/m;Lo70/j;Lo70/j;Lkotlin/jvm/functions/Function0;Lapp/rive/semantics/AndroidVirtualNodeIdRegistry;)V @00002bcc
    [xrefs_shown=0]
  STR string_data::(Lapp/rive/semantics/AndroidVirtualNodeIdAllocator;)V @00002f08
    [xrefs_shown=0]
  STR string_data::(Lc5/g;Landroid/view/View;ILapp/rive/semantics/ProjectedSemanticHierarchy;Lapp/rive/semantics/AndroidVirtualNodeIdRegistry;)Z @00002fa4
    [xrefs_shown=0]
  STR string_data::(offset: @000038f0
    [xrefs_shown=0]
  STR string_data::)_offset_is_outside_of_text_region_ @000039bc
    [xrefs_shown=0]
  STR string_data::,_activeModalNodeId= @00003b54
    [xrefs_shown=0]
  STR string_data::,_activeNodeIds= @00003b58
    [xrefs_shown=0]
  STR string_data::,_ancestorNodeIds= @00003bc0
    [xrefs_shown=0]
  STR string_data::,_borderCornerOffset= @00003d00
    [xrefs_shown=0]
  STR string_data::,_chapterIndex= @00003e30
    [xrefs_shown=0]
  STR string_data::,_chapterIndexInSection= @00003e34
    [xrefs_shown=0]
  STR string_data::,_childrenByNodeId= @00003e54
    [xrefs_shown=0]
  STR string_data::,_columnCount= @00003ed0
    [xrefs_shown=0]
  STR string_data::,_correctLessons= @00003f98
    [xrefs_shown=0]
  STR string_data::,_correctLessonsFirstTry= @00003f9c
    [xrefs_shown=0]
  STR string_data::,_crossAxisArrangementSpacing= @00003fe0
    [xrefs_shown=0]
  STR string_data::,_currentNodeId= @00004004
    [xrefs_shown=0]
  STR string_data::,_currentSectionEstimatedCompletionAt= @00004014
    [xrefs_shown=0]
  STR string_data::,_cursorOffset= @00004038
    [xrefs_shown=0]
  STR string_data::,_dataOffset= @0000406c
    [xrefs_shown=0]
  STR string_data::,_dotRadius= @0000413c
    [xrefs_shown=0]
  STR string_data::,_estimatedCompletionAt= @00004208
    [xrefs_shown=0]
  STR string_data::,_groupOffset= @000043ac
    [xrefs_shown=0]
  STR string_data::,_instructionsScrollOffset= @00004580
    [xrefs_shown=0]
  STR string_data::,_isPassword=false,_offsetMapping= @000046cc
    [xrefs_shown=0]
```

## run.log tail
```
INFO  IMPORTING: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  Using Loader: Dalvik Executable (DEX) (ProgramLoader)  
INFO  Using Language/Compiler: Dalvik:LE:32:DEX_KitKat:default (ProgramLoader)  
INFO  Using Library Search Path: [., /bin, /lib, /lib64, /lib/x86_64-linux-gnu, /lib/aarch64-linux-gnu, /usr/bin, /usr/lib, /usr/X11R6/bin, /usr/X11R6/lib, /usr/java/packages/lib, /usr/lib64] (ProgramLoader)  
INFO  IMPORTING: Loaded 0 additional files (HeadlessAnalyzer)  
WARN  Analyzer 'Apply Data Archives' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Basic Constant Reference Analyzer' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Data Reference' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call Convention ID' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Decompiler Switch Analysis' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Embedded Media' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Non-Returning Functions - Discovered' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Demangler GNU' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Reference' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Source Language Support' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Create Address Tables' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Call-Fixup Installer' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Disassemble Entry Points' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'External Entry References' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Subroutine References' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Shared Return Calls' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Stack' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'ASCII Strings' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Variadic Function Signature Override' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
WARN  Analyzer 'Function ID' for classes9.dex disabled by PSPEC file override (AnalysisScheduler)  
INFO  ANALYZING all memory and code: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  REPORT: Analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  REPORT: Execute script: MimoControlFlow.java  (HeadlessAnalyzer)  
INFO  SCRIPT: /home/runner/work/game/game/ANALYSIS/_TOOLCHAIN/ghidra_scripts/MimoControlFlow.java (HeadlessAnalyzer)  
INFO  MimoControlFlow.java> === PROGRAM classes9.dex language=Dalvik:LE:32:DEX_KitKat functions=3 symbols=69 memory_blocks=3 ===
-- DEX string cross references (field names -> owning functions) --
  [geometry_strings_examined=0]
-- target function Dalvik instructions --
SCANNED_FUNCS=3 BRANCH_INSNS_FIRST_8000=0 INVOKE_INSNS_FIRST_8000=3 PATH_MAP_FUNCS=0 SCORING_FUNCS=0 INSTRUCTIONS_SHOWN=0
 (GhidraScript)  
INFO  ANALYZING changes made by post scripts: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  REPORT: Post-analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes9.dex (HeadlessAnalyzer)  
INFO  /classes9.dex: file created (runner) (LocalFileSystem)  
INFO  REPORT: Save succeeded for: /classes9.dex (Mimo935Analysis:/classes9.dex) (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded (HeadlessAnalyzer)  
auto_headless_exit=0
JAVA_HOME(REA)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-9/x64
JDK25_HOME(Ghidra)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/25.0.5-8/x64
java --list-modules | grep jdk.compiler:
jdk.compiler@21.0.13
rea_doctor_exit=0
{"healthy":true,"environment_healthy":false,"scope":{"mode":"explicit","clients":[],"providers":["jadx"],"skill":false,"target":null},"scope_checks":[{"name":"node","ok":true,"classification":"healthy","detail":"24.22.2","details":{"runtime":"node","version":"24.22.2"}},{"name":"jadx","ok":true,"classification":"healthy","detail":"JADX MCP bridge JAR validated at /home/runner/work/_temp/jadx-headless-mcp.jar; its path is recorded for agent registrations. This checks configuration, not whether a selected APK fits in the worker's memory.","details":{"operation_timeout_ms":120000}}],"informational_checks":[{"name":"host","ok":true,"classification":"healthy","detail":"ubuntu 26.04"},{"name":"hopper","ok":false,"classification":"missing_analysis_engine","remediation":"Run rea setup to install Hopper, or set HOPPER_LAUNCHER_PATH."},{"name":"ghidra","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC"},{"name":"ghidra-platform","ok":true,"classification":"healthy","detail":"linux"},{"name":"ghidra-architecture","ok":true,"classification":"healthy","detail":"x64"},{"name":"ghidra-installation","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/application.properties"},{"name":"ghidra-version","ok":false,"classification":"config_drift","detail":"12.2; accepted releases are 12.1.x (verified build 12.1.4)","remediation":"Install a Ghidra 12.1.x release (verified with 12.1.4), or update REA for another Ghidra line."},{"name":"ghidra-headless","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/support/analyzeHeadless"},{"name":"ghidra-native_decompiler","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/Features/Decompiler/os/linux_x86_64/decompile reports elf x86_64, which matches linux/x64"},{"name":"ghidra-java","ok":false,"classification":"config_drift","detail"```
