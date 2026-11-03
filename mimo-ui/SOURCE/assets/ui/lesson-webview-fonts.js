(function() {
    const style = document.createElement('style');
    for (const [face, weight] of [['regular', 400], ['medium', 500], ['bold', 700]]) {
        for (const variant of ['normal', 'italic']) {
            style.textContent += `@font-face {
                font-family: "Aeonik Pro";
                src: url("https://lesson.mimo.invalid/fonts/aeonik_pro_${face}_${variant}.otf") format("opentype");
                font-weight: ${weight};
                font-style: ${variant};
                font-display: swap;
            }`;
        }
    }
    document.head.appendChild(style);
})();
