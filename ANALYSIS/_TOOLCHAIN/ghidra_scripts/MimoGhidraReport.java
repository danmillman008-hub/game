//@category Mimo.Analysis
// Temporary analysis toolchain only. Runs inside a GitHub Actions runner that has
// the OFFICIAL Ghidra 12.2 release fully installed (the sandbox cannot download it).

import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Program;
import java.io.FileWriter;
import java.io.PrintWriter;

public class MimoGhidraReport extends GhidraScript {

    @Override
    public void run() throws Exception {
        Program p = currentProgram;
        StringBuilder s = new StringBuilder();
        s.append("=== Ghidra program report ===\n");
        s.append("program       : ").append(p.getName()).append('\n');
        s.append("language      : ").append(p.getLanguage().getLanguageID().getIdAsString()).append('\n');
        s.append("compiler spec : ").append(p.getCompilerSpec().getCompilerSpecID().getIdAsString()).append('\n');
        s.append("image base    : ").append(p.getImageBase()).append('\n');
        s.append("memory blocks : ").append(p.getMemory().getBlocks().length).append('\n');
        s.append("functions     : ").append(p.getFunctionManager().getFunctionCount()).append('\n');
        s.append("symbols       : ").append(p.getSymbolTable().getNumSymbols()).append('\n');
        s.append("executable?   : ").append(p.getLanguage().getLanguageDescription().getSize()).append("-bit\n");

        String ws = System.getenv("GITHUB_WORKSPACE");
        if (ws != null) {
            String out = ws + "/ANALYSIS/GHIDRA/GHIDRA_PROGRAM_REPORT.txt";
            try (PrintWriter w = new PrintWriter(new FileWriter(out, true))) {
                w.print(s.toString());
            }
        }
        println(s.toString());
    }
}
