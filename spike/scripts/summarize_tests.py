#!/usr/bin/env python3
"""Summarize JUnit XML results produced by `./gradlew testDebugUnitTest`.

Usage: summarize_tests.py <project-root>
Prints a markdown table: module | tests | failures | skipped
"""
import glob
import os
import sys
import xml.etree.ElementTree as ET

root = sys.argv[1] if len(sys.argv) > 1 else "."
rows = []
for path in glob.glob(os.path.join(root, "**", "test-results", "testDebugUnitTest", "*.xml"), recursive=True):
    try:
        r = ET.parse(path).getroot()
    except Exception:
        continue
    module = path.split(f"{root}/")[-1].split("/build/")[0]
    rows.append((module, int(r.get("tests", 0)), int(r.get("failures", 0)), int(r.get("skipped", 0)),
                 int(r.get("errors", 0))))

print("| module | tests | failures | errors | skipped |")
print("|---|---|---|---|---|")
t = f = e = s = 0
for module, tests, failures, skipped, errors in sorted(rows):
    print(f"| {module} | {tests} | {failures} | {errors} | {skipped} |")
    t += tests
    f += failures
    e += errors
    s += skipped
print(f"| **TOTAL** | **{t}** | **{f}** | **{e}** | **{s}** |")
if f or e:
    print("\nFAILED modules:")
    for module, tests, failures, skipped, errors in sorted(rows):
        if failures or errors:
            print(f"- {module} (tests={tests}, failures={failures}, errors={errors})")
