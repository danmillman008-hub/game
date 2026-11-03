(() => {
    const documentID = __MIMO_DOCUMENT_ID__;
    const post = payload => MimoLesson.postMessage(JSON.stringify({ documentID, ...payload }));

    // Observe ownership; never prevent a DOM event on the activity's behalf.
    let gesture = null;
    const movementThreshold = __MIMO_TOUCH_SLOP_CSS_PX__;
    function decide(current, decision) {
        if (!current || current.decided || gesture !== current) return;
        current.decided = true;
        post({ kind: 'gesture', decision, startedAt: current.startedAt });
    }
    function claim() { decide(gesture, 'web'); }
    function belongsToWeb(target) {
        for (let element = target; element && element !== document.body
            && element !== document.documentElement; element = element.parentElement) {
            if (element.getAttribute('draggable') === 'true' || element.isContentEditable
                || element.matches('input, textarea, select')) return true;
            const style = getComputedStyle(element);
            const action = style.touchAction;
            // Root-wide touch-action:none is boilerplate, not a draggable hit region.
            if (action === 'none' || (action !== 'auto' && action !== 'manipulation'
                && !/pan-y|pan-up|pan-down/.test(action))) return true;
            if (element.scrollHeight > element.clientHeight && /auto|scroll/.test(style.overflowY)) return true;
        }
        return false;
    }
    function begin(event, point) {
        if (!event.isTrusted) return;
        gesture = {
            startedAt: performance.timeOrigin + event.timeStamp,
            x: point.clientX, y: point.clientY, pointerID: event.pointerId,
            eventTime: event.timeStamp, decided: false, framePending: false
        };
        const target = event.composedPath()[0];
        // An iframe without our bridge must retain its gestures rather than change lessons.
        if (target instanceof Element && (belongsToWeb(target) || target.matches('iframe'))) claim();
    }
    function move(event, point) {
        const current = gesture;
        if (!event.isTrusted || !current || current.decided) return;
        current.dx = point.clientX - current.x;
        current.dy = point.clientY - current.y;
        if (current.framePending) return;
        current.framePending = true;
        requestAnimationFrame(() => {
            current.framePending = false;
            if (gesture !== current || current.decided) return;
            const dx = Math.abs(current.dx), dy = Math.abs(current.dy);
            if (Math.max(dx, dy) < movementThreshold) return;
            decide(current, dy > dx ? 'lesson' : 'web');
        });
    }
    const preventDefault = Event.prototype.preventDefault;
    Event.prototype.preventDefault = function (...args) {
        const result = Reflect.apply(preventDefault, this, args);
        if (this.isTrusted && this.defaultPrevented && gesture && this.timeStamp >= gesture.eventTime
            && /^(touchstart|touchmove|pointerdown|pointermove|dragstart)$/.test(this.type)) claim();
        return result;
    };
    const setPointerCapture = Element.prototype.setPointerCapture;
    Element.prototype.setPointerCapture = function (pointerID) {
        const result = Reflect.apply(setPointerCapture, this, [pointerID]);
        if (gesture && gesture.pointerID === pointerID) claim();
        return result;
    };
    window.addEventListener('pointerdown', event => {
        if (gesture && !event.isPrimary) { claim(); return; }
        begin(event, event);
    }, { capture: true, passive: true });
    window.addEventListener('pointermove', event => {
        if (gesture && event.pointerId === gesture.pointerID) move(event, event);
    }, { capture: true, passive: true });
    window.addEventListener('touchstart', event => {
        if (!event.isTrusted) return;
        if (event.touches.length > 1) { claim(); return; }
        if (!gesture) begin(event, event.touches[0]);
    }, { capture: true, passive: true });
    window.addEventListener('touchmove', event => {
        if (event.touches.length === 1) move(event, event.touches[0]);
    }, { capture: true, passive: true });
    window.addEventListener('dragstart', event => {
        if (event.isTrusted) claim();
    }, { capture: true, passive: true });
    function finish() {
        const current = gesture;
        // Chromium can deliver the last move and UP in the same frame. Let the queued
        // ownership decision run before clearing it, even though native touch has ended.
        requestAnimationFrame(() => {
            if (gesture === current) gesture = null;
        });
    }
    for (const name of ['pointerup', 'pointercancel']) {
        window.addEventListener(name, event => {
            if (!event.isTrusted || !gesture || event.pointerId !== gesture.pointerID) return;
            // On Android, Chromium cancels pointer events when it begins panning, but continues
            // touch events. That is not a cancelled physical gesture; touchend/cancel ends it.
            if (name === 'pointercancel' && event.pointerType === 'touch') return;
            if (name === 'pointercancel') gesture = null;
            else { move(event, event); finish(); }
        }, { capture: true, passive: true });
    }
    for (const name of ['touchend', 'touchcancel']) {
        window.addEventListener(name, event => {
            if (!event.isTrusted || event.touches.length !== 0) return;
            if (name === 'touchcancel') gesture = null;
            else {
                if (event.changedTouches.length === 1) move(event, event.changedTouches[0]);
                finish();
            }
        }, { capture: true, passive: true });
    }
    post({ kind: 'gesture', decision: 'ready', startedAt: 0 });

    if (window !== window.top) return;
    const activityMessageTypes = ['mimo.activity.correct', 'mimo.activity.wrong', 'mimo.activity.completed'];
    window.addEventListener('message', event => {
        if (event.source !== window) return;
        const message = event.data;
        if (message && activityMessageTypes.includes(message.type)) {
            post({ kind: 'activity', result: message.type });
        }
    });
    function setupLayout() {
        const meta = document.createElement('meta');
        meta.name = 'viewport';
        meta.content = 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no';
        document.head.appendChild(meta);
        const style = document.createElement('style');
        style.textContent = ':root { color-scheme: light dark; }';
        __MIMO_FONT_SCRIPT__
        document.head.appendChild(style);
        function reportFocus() {
            const element = document.activeElement;
            post({ kind: 'focus', focused: !!element
                && (element.matches('input, textarea') || element.isContentEditable) });
        }
        document.addEventListener('focusin', reportFocus);
        document.addEventListener('focusout', () => queueMicrotask(reportFocus));
        reportFocus();
        let pendingMeasurement = false;
        function reportHeight() {
            if (pendingMeasurement) return;
            pendingMeasurement = true;
            requestAnimationFrame(() => {
                pendingMeasurement = false;
                const body = document.body;
                const styles = getComputedStyle(body);
                const height = body.getBoundingClientRect().height
                    + parseFloat(styles.marginTop) + parseFloat(styles.marginBottom);
                post({ kind: 'height', height: Math.ceil(height) });
            });
        }
        new ResizeObserver(reportHeight).observe(document.body);
        new MutationObserver(reportHeight).observe(document.body, {
            attributes: true, childList: true, characterData: true, subtree: true
        });
        window.addEventListener('load', reportHeight);
        document.fonts.ready.then(reportHeight);
        reportHeight();
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupLayout, { once: true });
    } else {
        setupLayout();
    }
})();
