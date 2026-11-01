# Mission 6 — Application Startup

## Scope
The real initialization path from process start to the first screen, as far as static evidence supports.

## Method
Decoded manifest (application/provider declarations, launch activity, aliases); read `com.getmimo.App`
and its Hilt component holder; read the DI factory (`ae.m`) provider order; read `SplashActivity` and
`MainActivity` entry code; check for `androidx.startup` initializers in the manifest.

## Sources
`/tmp/manifest.xml` (decoded), `com.getmimo.App.java`, `ae.m.java`, `com.getmimo.ui.SplashActivity.java`,
`com.getmimo.ui.main.MainActivity.java`, `evidence/DI_GRAPH.json`.

## Findings
1. **`Application` is `com.getmimo.App`, and it extends `bin.ghost.yrf`** (an injected superclass; see
   baseline I-2). Superclass initialization therefore happens *before* any Mimo code — this is the
   earliest interception point in the process and it is not Mimo's own code.
2. **DI is Hilt**: `App` holds `x30.g` (the generated component holder) constructed from a
   `cc.b` factory; injected singletons appear as fields (`analytics.a`, `be.d`, `i9.h` worker factory,
   `lf.a` settings worker factory, `kf.d`, `be.a4`, `mg.a`). WorkManager is initialized with a Hilt
   worker factory plus a second "settings" worker factory (`App.a()`), so **background work can start
   without the UI**.
3. **The DI factory `ae.m` is a 127-case switch.** Its case order is the wiring order of the graph and
   reveals startup-relevant singletons: Gson with Joda adapters (case 3), OkHttp (case 20),
   `com.getmimo.network.a` connectivity (case 21), **API base URL selection (case 22)**,
   `authentication` repository (case 24), Room (`mimo.db`, case 33), analytics handles.
4. **No `androidx.startup` initializers are declared** in the decoded manifest (the
   `InitializationProvider` meta-data list is absent), so initialization is Hilt + explicit `App` work,
   not the App Startup library.
5. **Entry activity**: `com.getmimo.ui.SplashActivity` is the launcher and also owns the deep-link
   filters; `MainActivity` (`com.getmimo.ui.main.MainActivity`) carries **12** `https://getmimo.com`
   filters. Six `SplashActivity` **aliases** (`_default`, `_ninja`, `_ukraine`, `_chemist`, `_bat`,
   `_proud`) indicate seasonal launch icons/themes selected at build or by component enabling.
6. **Startup performs network-dependent work**: the base URL is chosen from a dev-menu flag (case 22),
   and the analytics facade registers Adjust attribution callbacks in its constructor
   (`Adjust.getAdid`, `Adjust.getAttribution`), which is a network/IPC touch on first use.
7. **Error handling at startup**: `hg.e` guarantees that any request attempted while offline throws
   `NoConnectionException` rather than hanging; `com.getmimo.network.a` treats *only* Wi-Fi or cellular
   transports as online (VPN/ethernet are reported offline).

## Evidence labels
Declared components, class inheritance, DI case order, interceptors: **VERIFIED_STATIC**.
"Seasonal aliases are selected at runtime by a feature flag": **INFERRED** (aliases exist; selection
mechanism not located).

## Limitations
`onCreate` bodies (in `App$onCreate$1/2`) were not fully traced; the ordering *within* `App.onCreate`
is therefore not enumerated. Startup timing, splash duration and any blocking I/O are **UNKNOWN**
without runtime.

## Open questions
`Q-08` exact `App.onCreate` sequence; `Q-09` whether the splash performs content/version checks before
`MainActivity`; `Q-10` what `bin.ghost.yrf` does at attach time.

## Reproduction
```bash
grep -o 'android:name="[^"]*"' /tmp/manifest.xml | sort -u | grep -iE 'App|Splash|Main'
sed -n '1,60p' /tmp/dad/com.getmimo.App.java
python3 -c "import json;d=json.load(open('evidence/DI_GRAPH.json'));print([c['case'] for c in d['providers']][:30])"
```
