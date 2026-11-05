//@category Mimo.Analysis
// Runs AFTER Ghidra Auto Analysis (no -noanalysis) on the original Mimo DEX.
// Extracts the function inventory and real Dalvik instructions (branch / call
// evidence) for the two analysis targets: learning-path geometry and the
// lesson-end scoring / completion engine.

import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.listing.Program;
import ghidra.program.model.symbol.Symbol;
import ghidra.program.model.symbol.SymbolIterator;
import java.io.FileWriter;
import java.io.PrintWriter;

public class MimoControlFlow extends GhidraScript {

    private static boolean target(String s) {
        if (s == null) return false;
        String n = s.toLowerCase();
        return n.contains("pathmap") || n.contains("chapterfinished")
            || n.contains("lessonprogress") || n.contains("leaderboard")
            || n.contains("streak") || n.contains("reward")
            || n.contains("invokesuspend") || n.contains("getxp")
            || n.contains("sparks") || n.contains("coins");
    }

    @Override
    public void run() throws Exception {
        Program p = currentProgram;
        StringBuilder sb = new StringBuilder();
        FunctionManager fm = p.getFunctionManager();
        int funcs = fm.getFunctionCount();
        sb.append("=== PROGRAM ").append(p.getName())
          .append(" language=").append(p.getLanguage().getLanguageID().getIdAsString())
          .append(" functions=").append(funcs)
          .append(" symbols=").append(p.getSymbolTable().getNumSymbols())
          .append(" memory_blocks=").append(p.getMemory().getBlocks().length)
          .append(" ===\n");

        sb.append("-- namespace inventory (path map / chapter finished / progress) --\n");
        SymbolIterator si = p.getSymbolTable().getAllSymbols(true);
        int ns = 0;
        while (si.hasNext() && ns < 120) {
            Symbol s = si.next();
            if (target(s.getName(true))) {
                sb.append("  SYM ").append(s.getName(true))
                  .append(" @").append(s.getAddress()).append('\n');
                ns++;
            }
        }
        sb.append("  [namespace_symbols_shown=").append(ns).append("]\n");

        sb.append("-- function control flow (real Dalvik instructions, not Java) --\n");
        int dumped = 0, totalInsns = 0, branches = 0, calls = 0, scanned = 0;
        for (Function f : fm.getFunctions(true)) {
            scanned++;
            String n = f.getName();
            // count branch / call instructions across the whole program (bounded)
            if (scanned <= 6000) {
                InstructionIterator ci = p.getListing().getInstructions(f.getBody(), true);
                while (ci.hasNext()) {
                    Instruction c = ci.next();
                    String mn = c.getMnemonicString();
                    if (mn == null) continue;
                    if (mn.startsWith("if-") || mn.equals("goto") || mn.startsWith("goto/")
                        || mn.contains("switch")) branches++;
                    if (mn.startsWith("invoke-")) calls++;
                }
            }
            if (dumped >= 40 || !target(n)) continue;
            sb.append("FUNC ").append(n).append(" @").append(f.getEntryPoint())
              .append(" body_bytes=").append(f.getBody().getNumAddresses()).append('\n');
            int k = 0;
            InstructionIterator it = p.getListing().getInstructions(f.getBody(), true);
            while (it.hasNext() && k < 60) {
                Instruction ins = it.next();
                sb.append("  ").append(ins.getAddress()).append("  ")
                  .append(ins.toString()).append('\n');
                k++; totalInsns++;
            }
            sb.append("  [instructions_shown=").append(k).append("]\n");
            dumped++;
        }
        sb.append("SCANNED_FUNCS=").append(scanned)
          .append(" BRANCH_INSNS=").append(branches)
          .append(" INVOKE_INSNS=").append(calls)
          .append(" DUMPED_FUNCS=").append(dumped)
          .append(" INSTRUCTIONS_SHOWN=").append(totalInsns).append('\n');

        String ws = System.getenv("GITHUB_WORKSPACE");
        if (ws != null) {
            try (PrintWriter w = new PrintWriter(new FileWriter(
                    ws + "/ANALYSIS/GHIDRA/CONTROL_FLOW.txt", true))) {
                w.print(sb.toString());
            }
        }
        println(sb.toString());
    }
}
