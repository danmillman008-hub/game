// Loaded by flutter_tex before its bundled MathJax engine. Keep this file in git.
window.MathJax = {
    startup: {
        ready: function () {
            MathJax.startup.defaultReady();
            // flutter_tex 5.2.x constructs a separate lite SVG output processor.
            // Its defaults ignore the global svg options below.
            var lite = MathJax.flutterTeXLiteDOM;
            if (lite && lite.outputJax && lite.outputJax.options.linebreaks) {
                lite.outputJax.options.linebreaks.inline = false;
            }
        }
    },
    tex: {
        packages: ['base', 'ams', 'newcommand', 'configmacros', 'mhchem'],
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    // Native SVG widgets need each formula to carry its own glyph definitions.
    svg: {
        fontCache: 'local',
        // Native SVG widgets require one document, not multiple inline fragments.
        linebreaks: { inline: false }
    }
};
