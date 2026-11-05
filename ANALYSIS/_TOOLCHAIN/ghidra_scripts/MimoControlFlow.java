//@category Mimo.Analysis
// Runs AFTER Ghidra Auto Analysis (no -noanalysis) on the original Mimo DEX.
// Extracts the real Dalvik function inventory, branch/call counts and
// instruction-level control flow for the two analysis targets:
//   (1) com.getmimo.ui.path.map (learning-path geometry / scroll)
//   (2) ChapterFinishedViewModel + Progress/Completion/reward engine.

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

    private static String fullName(Program p, Function f) {
        Symbol s = p.getSymbolTable().getPrimarySymbol(f.getEntryPoint());
        return (s == null) ? f.getName() : s.getName(true);
    }

    private static boolean pathMap(String n) {
        String x = n.toLowerCase();
        return x.contains("getmimo::ui::path::map") || x.contains("pathmap")
            || x.contains("path_map") || x.contains("pathmapscreen");
    }

    private static boolean scoring(String n) {
        String x = n.toLowerCase();
        return x.contains("chapterfinished") || x.contains("chapterendview")
            || x.contains("lessonprogress") || x.contains("completion")
            || x.contains("reward") || x.contains("streak")
            || x.contains("leaderboard") || x.contains("coins")
            || x.contains("sparks") || x.contains("getxp")
            || x.contains("dailygoal") || x.contains("setprogress");
    }

    @Override
    public void run() throws Exception {
        Program p = currentProgram;
        StringBuilder sb = new StringBuilder();
        StringBuilder syms = new StringBuilder();
        FunctionManager fm = p.getFunctionManager();
        int funcs = fm.getFunctionCount();
        sb.append("=== PROGRAM ").append(p.getName())
          .append(" language=").append(p.getLanguage().getLanguageID().getIdAsString())
          .append(" functions=").append(funcs)
          .append(" symbols=").append(p.getSymbolTable().getNumSymbols())
          .append(" memory_blocks=").append(p.getMemory().getBlocks().length)
          .append(" ===\n");

        sb.append("-- target namespace inventory (all matching symbols, capped) --\n");
        SymbolIterator si = p.getSymbolTable().getAllSymbols(true);
        int ns = 0;
        while (si.hasNext() && ns < 900) {
            Symbol s = si.next();
            String n = s.getName(true);
            if (pathMap(n) || scoring(n)) {
                syms.append("  SYM ").append(n).append(" @").append(s.getAddress()).append('\n');
                ns++;
            }
        }
        sb.append(syms);
        sb.append("  [target_symbols_shown=").append(ns).append("]\n");

        sb.append("-- target function control flow (real Dalvik instructions) --\n");
        int dumpedPath = 0, dumpedScore = 0, totalInsns = 0;
        int branches = 0, calls = 0, scanned = 0;
        for (Function f : fm.getFunctions(true)) {
            scanned++;
            String n = fullName(p, f);
            if (scanned <= 8000) {
                InstructionIterator ci = p.getListing().getInstructions(f.getBody(), true);
                while (ci.hasNext()) {
                    Instruction c = ci.next();
                    String mn = c.getMnemonicString();
                    if (mn == null) continue;
                    String m = mn.toLowerCase();
                    if (m.startsWith("if") || m.startsWith("goto") || m.contains("switch")) branches++;
                    if (m.startsWith("invoke")) calls++;
                }
            }
            boolean pm = pathMap(n), sc = scoring(n);
            if (pm && dumpedPath >= 30) continue;
            if (sc && dumpedScore >= 30) continue;
            if (!pm && !sc) continue;
            sb.append("FUNC [").append(pm ? "PATH_MAP" : "SCORING").append("] ")
              .append(n).append(" @").append(f.getEntryPoint())
              .append(" body_bytes=").append(f.getBody().getNumAddresses()).append('\n');
            int k = 0;
            InstructionIterator it = p.getListing().getInstructions(f.getBody(), true);
            while (it.hasNext() && k < 70) {
                Instruction ins = it.next();
                sb.append("  ").append(ins.getAddress()).append("  ")
                  .append(ins.toString()).append('\n');
                k++; totalInsns++;
            }
            sb.append("  [instructions_shown=").append(k).append("]\n");
            if (pm) dumpedPath++; else dumpedScore++;
            if (dumpedPath >= 30 && dumpedScore >= 30) break;
        }
        sb.append("SCANNED_FUNCS=").append(scanned)
          .append(" BRANCH_INSNS_FIRST_8000_FUNCS=").append(branches)
          .append(" INVOKE_INSNS_FIRST_8000_FUNCS=").append(calls)
          .append(" PATH_MAP_FUNCS_DUMPED=").append(dumpedPath)
          .append(" SCORING_FUNCS_DUMPED=").append(dumpedScore)
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
