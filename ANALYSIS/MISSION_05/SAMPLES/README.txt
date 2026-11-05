MISSION 05 - SAMPLES
Every file here is a verbatim (or explicitly truncated) extract from the ORIGINAL
APK sha256 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a.
No sample was authored, rewritten or reconstructed. Source path is on the first
line of each text sample; the full asset inventory with SHA-256 of every
non-curriculum asset is EVIDENCE/ASSET_MANIFEST.txt.

  tracks_json_head.json           VALID JSON wrapper with a verbatim truncated
                                 preview of the first track object (v753)
  test_tracks_json_head.json      wrapper with verbatim preview of the v52 fixture
  test_tutorial_json_head.json    wrapper with verbatim preview of the v52 fixture
                                 (the "*_head.json" files are previews, not
                                 complete JSON documents; their `preview` field
                                 holds the exact bytes)
  testdata_127-0-1.html          shipped fixture showing spell/selection/fillTheGap + visible-if
  validatedinput_lesson.txt      real v753 lesson with <interaction type="validatedInput">
  fillthegap_lesson.txt          real v753 lesson with fillTheGap + hardModeContent
  selection_lesson.txt           real v753 lesson with <selection> and correct="true/false"
  webview_lesson.txt             real v753 lesson with <webview version="2">
  hardmode_lesson.txt            real v753 alternative hardModeContent
  bridge_message_lesson.txt      real v753 lesson emitting mimo.activity.correct/wrong/completed
                                 (truncated at 6000 chars, marked)
  executable_lesson.json         real v753 executableContent incl. solvedContent
  lesson-webview.js              verbatim assets/lesson-webview.js (JS<->native bridge)
  runtime_matched_lesson_151403.txt          shipped tutorial-904 lesson rendered at runtime STEP-24
  runtime_matched_executable_lesson_63259.json  shipped tutorial-2199 lesson rendered OFFLINE-03/05
