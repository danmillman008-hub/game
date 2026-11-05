# Ghidra / REA chain — corrected run

- run 41939776550 / commit 5faa971ccbd5816d99a89400a71810e84ff27f43 / 2026-11-05T00:15:55Z
- Ghidra fetch: success; coverage: success; auto analysis: success; REA doctor: success
- corrections applied: ALL 12 DEX imported (not 3); Auto Analysis ENABLED (no -noanalysis); full JDK 21 for REA separate from JDK 25 for Ghidra

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
```

## run.log tail
```
    Android DEX/CDEX Switch Table Markup       4.461 secs
-----------------------------------------------------
     Total Time   60 secs
-----------------------------------------------------
 (AutoAnalysisManager)  
INFO  REPORT: Analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes.dex (HeadlessAnalyzer)  
INFO  REPORT: Execute script: MimoControlFlow.java  (HeadlessAnalyzer)  
ERROR MimoControlFlow.java:30: error: method getFunctionCount in interface ghidra.program.model.listing.FunctionManager cannot be applied to given types;
        int funcs = fm.getFunctionCount(true);
                      ^
  required: no arguments
  found:    boolean
  reason: actual and formal argument lists differ in length
skipping /home/runner/work/game/game/ANALYSIS/_TOOLCHAIN/ghidra_scripts/MimoControlFlow.java
 (HeadlessAnalyzer)  
ERROR REPORT SCRIPT ERROR: MimoControlFlow.java : The class could not be found. It must be the public class of the .java file: MimoControlFlow not found by 5014f706 [1] (HeadlessAnalyzer) ghidra.app.script.GhidraScriptLoadException: The class could not be found. It must be the public class of the .java file: MimoControlFlow not found by 5014f706 [1]
	at ghidra.app.script.JavaScriptProvider.getScriptInstance(JavaScriptProvider.java:114)
	at ghidra.app.util.headless.HeadlessAnalyzer.runScriptsList(HeadlessAnalyzer.java:929)
	at ghidra.app.util.headless.HeadlessAnalyzer.analyzeProgram(HeadlessAnalyzer.java:1107)
	at ghidra.app.util.headless.HeadlessAnalyzer.processFileWithImport(HeadlessAnalyzer.java:1606)
	at ghidra.app.util.headless.HeadlessAnalyzer.processWithLoader(HeadlessAnalyzer.java:1770)
	at ghidra.app.util.headless.HeadlessAnalyzer.processWithImport(HeadlessAnalyzer.java:1705)
	at ghidra.app.util.headless.HeadlessAnalyzer.processWithImport(HeadlessAnalyzer.java:1795)
	at ghidra.app.util.headless.HeadlessAnalyzer.processLocal(HeadlessAnalyzer.java:464)
	at ghidra.app.util.headless.AnalyzeHeadless.launch(AnalyzeHeadless.java:211)
	at ghidra.GhidraLauncher.launch(GhidraLauncher.java:78)
	at ghidra.Ghidra.main(Ghidra.java:41)
Caused by: java.lang.ClassNotFoundException: MimoControlFlow not found by 5014f706 [1]
	at org.apache.felix.framework.BundleWiringImpl.findClassOrResourceByDelegation(BundleWiringImpl.java:1591)
	at org.apache.felix.framework.BundleWiringImpl.access$300(BundleWiringImpl.java:79)
	at org.apache.felix.framework.BundleWiringImpl$BundleClassLoader.loadClass(BundleWiringImpl.java:1976)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:490)
	at org.apache.felix.framework.Felix.loadBundleClass(Felix.java:2116)
	at org.apache.felix.framework.BundleImpl.loadClass(BundleImpl.java:986)
	at ghidra.app.script.JavaScriptProvider.loadClass(JavaScriptProvider.java:166)
	at ghidra.app.script.JavaScriptProvider.getScriptInstance(JavaScriptProvider.java:97)
	... 10 more
 
INFO  ANALYZING changes made by post scripts: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes.dex (HeadlessAnalyzer)  
INFO  REPORT: Post-analysis succeeded for file: file:///home/runner/work/game/game/ANALYSIS/_INPUT/classes.dex (HeadlessAnalyzer)  
INFO  /classes.dex: file created (runner) (LocalFileSystem)  
INFO  REPORT: Save succeeded for: /classes.dex (Mimo935Analysis:/classes.dex) (HeadlessAnalyzer)  
INFO  REPORT: Import succeeded (HeadlessAnalyzer)  
auto_headless_exit=0
JAVA_HOME(REA)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/21.0.13-9/x64
JDK25_HOME(Ghidra)=/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/25.0.5-8/x64
java --list-modules | grep jdk.compiler:
jdk.compiler@21.0.13
rea_doctor_exit=0
{"healthy":true,"environment_healthy":false,"scope":{"mode":"explicit","clients":[],"providers":["jadx"],"skill":false,"target":null},"scope_checks":[{"name":"node","ok":true,"classification":"healthy","detail":"22.23.4","details":{"runtime":"node","version":"22.23.4"}},{"name":"jadx","ok":true,"classification":"healthy","detail":"JADX MCP bridge JAR validated at /home/runner/work/_temp/jadx-headless-mcp.jar; its path is recorded for agent registrations. This checks configuration, not whether a selected APK fits in the worker's memory.","details":{"operation_timeout_ms":120000}}],"informational_checks":[{"name":"host","ok":true,"classification":"healthy","detail":"ubuntu 24.04"},{"name":"hopper","ok":false,"classification":"missing_analysis_engine","remediation":"Run rea setup to install Hopper, or set HOPPER_LAUNCHER_PATH."},{"name":"ghidra","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC"},{"name":"ghidra-platform","ok":true,"classification":"healthy","detail":"linux"},{"name":"ghidra-architecture","ok":true,"classification":"healthy","detail":"x64"},{"name":"ghidra-installation","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/application.properties"},{"name":"ghidra-version","ok":false,"classification":"config_drift","detail":"12.2; accepted releases are 12.1.x (verified build 12.1.4)","remediation":"Install a Ghidra 12.1.x release (verified with 12.1.4), or update REA for another Ghidra line."},{"name":"ghidra-headless","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/support/analyzeHeadless"},{"name":"ghidra-native_decompiler","ok":true,"classification":"healthy","detail":"/home/runner/work/_temp/ghidra_dist/ghidra_12.2_PUBLIC/Ghidra/Features/Decompiler/os/linux_x86_64/decompile reports elf x86_64, which matches linux/x64"},{"name":"ghidra-java","ok":false,"classification":"config_drift","detail"```
