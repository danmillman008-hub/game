//@category Mimo.Analysis
// Runs AFTER Ghidra Auto Analysis on ALL 12 DEX of the original Mimo 9.35 APK.
// Joins three evidence layers: namespace symbols, DEX-string cross-references
// (which function actually uses a field name), and real Dalvik instructions.
// Targets: (1) com.getmimo.ui.path.map geometry/scroll,
//          (2) ChapterFinishedViewModel + progress/completion/reward engine.

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.listing.Program;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.Symbol;
import ghidra.program.model.symbol.SymbolIterator;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Iterator;

public class MimoControlFlow extends GhidraScript {

    private static String fullName(Program p, Function f) {
        Symbol s = p.getSymbolTable().getPrimarySymbol(f.getEntryPoint());
        return (s == null) ? f.getName() : s.getName(true);
    }

    private static boolean uiPathMap(String n) {
        return n.toLowerCase().contains("getmimo::ui::path::map");
    }

    private static boolean scoring(String n) {
        String x = n.toLowerCase();
        return x.contains("chapterfinished") || x.contains("lessonprogress")
            || x.contains("completionrepository") || x.contains("rewardrepository")
            || x.contains("getchapterend") || x.contains("streakrepository")
            || x.contains("coinsrepository") || x.contains("dailygoal");
    }

    private static boolean geoString(String s) {
        String x = s.toLowerCase();
        return x.contains("chapterindex") || x.contains("sectionindex")
            || x.contains("columncount") || x.contains("spacing")
            || x.contains("offset") || x.contains("scrollposition")
            || x.contains("dotradius") || x.contains("ellipseradius")
            || x.contains("nodeid") || x.contains("scrolloffset")
            || x.contains("rewardmultiplier") || x.contains("rewardedsparks")
            || x.contains("earnedsparks") || x.contains("earnedcoins")
            || x.contains("correctlessons") || x.contains("firsttry")
            || x.contains("progressbar") || x.contains("estimatedcompletion");
    }

    @Override
    public void run() throws Exception {
        Program p = currentProgram;
        StringBuilder sb = new StringBuilder();
        FunctionManager fm = p.getFunctionManager();
        sb.append("=== PROGRAM ").append(p.getName())
          .append(" language=").append(p.getLanguage().getLanguageID().getIdAsString())
          .append(" functions=").append(fm.getFunctionCount())
          .append(" symbols=").append(p.getSymbolTable().getNumSymbols())
          .append(" memory_blocks=").append(p.getMemory().getBlocks().length)
          .append(" ===\n");

        sb.append("-- DEX string cross references (field names -> owning functions) --\n");
        SymbolIterator si = p.getSymbolTable().getAllSymbols(true);
        int sx = 0;
        while (si.hasNext() && sx < 260) {
            Symbol s = si.next();
            String n = s.getName(true);
            if (!n.startsWith("string_data::") || !geoString(n)) continue;
            sb.append("  STR ").append(n.replace('\n', ' ')).append(" @").append(s.getAddress()).append('\n');
            Address a = s.getAddress();
            Iterator<Reference> refs = p.getReferenceManager().getReferencesTo(a);
            int r = 0;
            while (refs.hasNext() && r < 4) {
                Reference ref = refs.next();
                Address from = ref.getFromAddress();
                Function f = fm.getFunctionContaining(from);
                sb.append("    XREF ").append(from);
                if (f != null) sb.append(" -> ").append(fullName(p, f));
                sb.append('\n');
                r++;
            }
            sb.append("    [xrefs_shown=").append(r).append("]\n");
            sx++;
        }
        sb.append("  [geometry_strings_examined=").append(sx).append("]\n");

        sb.append("-- target function Dalvik instructions --\n");
        int dp = 0, ds = 0, shown = 0, scanned = 0;
        int branches = 0, calls = 0;
        for (Function f : fm.getFunctions(true)) {
            scanned++;
            String n = fullName(p, f);
            if (scanned <= 8000) {
                InstructionIterator ci = p.getListing().getInstructions(f.getBody(), true);
                while (ci.hasNext()) {
                    String mn = ci.next().getMnemonicString();
                    if (mn == null) continue;
                    String m = mn.toLowerCase();
                    if (m.startsWith("if") || m.startsWith("goto") || m.contains("switch")) branches++;
                    if (m.startsWith("invoke")) calls++;
                }
            }
            boolean pm = uiPathMap(n), sc = scoring(n);
            if (pm && dp >= 60) continue;
            if (sc && ds >= 60) continue;
            if (!pm && !sc) continue;
            sb.append("FUNC [").append(pm ? "PATH_MAP" : "SCORING").append("] ")
              .append(n).append(" @").append(f.getEntryPoint())
              .append(" body_bytes=").append(f.getBody().getNumAddresses()).append('\n');
            int k = 0;
            InstructionIterator it = p.getListing().getInstructions(f.getBody(), true);
            while (it.hasNext() && k < 120) {
                Instruction ins = it.next();
                sb.append("  ").append(ins.getAddress()).append("  ")
                  .append(ins.toString()).append('\n');
                k++; shown++;
            }
            sb.append("  [instructions_shown=").append(k).append("]\n");
            if (pm) dp++; else ds++;
            if (dp >= 60 && ds >= 60) break;
        }
        sb.append("SCANNED_FUNCS=").append(scanned)
          .append(" BRANCH_INSNS_FIRST_8000=").append(branches)
          .append(" INVOKE_INSNS_FIRST_8000=").append(calls)
          .append(" PATH_MAP_FUNCS=").append(dp)
          .append(" SCORING_FUNCS=").append(ds)
          .append(" INSTRUCTIONS_SHOWN=").append(shown).append('\n');

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
