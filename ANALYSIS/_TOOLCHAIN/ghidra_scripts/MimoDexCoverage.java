//@category Mimo.Analysis
// Coverage proof for ALL 12 DEX files imported into Ghidra.

import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Program;
import java.io.FileWriter;
import java.io.PrintWriter;

public class MimoDexCoverage extends GhidraScript {

    @Override
    public void run() throws Exception {
        Program p = currentProgram;
        String line = "DEX " + p.getName()
                + " language=" + p.getLanguage().getLanguageID().getIdAsString()
                + " memory_blocks=" + p.getMemory().getBlocks().length
                + " symbols=" + p.getSymbolTable().getNumSymbols()
                + " functions=" + p.getFunctionManager().getFunctionCount()
                + " image_base=" + p.getImageBase();
        String ws = System.getenv("GITHUB_WORKSPACE");
        if (ws != null) {
            try (PrintWriter w = new PrintWriter(new FileWriter(
                    ws + "/ANALYSIS/GHIDRA/DEX_COVERAGE.txt", true))) {
                w.println(line);
            }
        }
        println(line);
    }
}
