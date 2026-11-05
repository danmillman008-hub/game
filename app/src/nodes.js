/**
 * Data-driven path nodes matching the ORIGINAL Mimo app.
 *
 * The approved prototype hardcodes six static nodes. The real app derives node
 * state from PathMapViewModel; here we do the same from real local progress so
 * the path map is alive. All geometry values are the code-first measurements
 * in mimo-ui/UPGRADE/DESIGN/NODE_CODE_GEOMETRY.json and CATALOGS/MIMO_PATH_NODES.csv.
 * No server behaviour is claimed.
 */
export const NODE_SPEC = Object.freeze({
  size_dp: 92, corner_radius_dp: 26, lip_dp: 8, icon_dp: 48, done_check_dp: 44,
  connector_stroke_dp: 10, elbow_radius_dp: 32, pitch_dp: 116,
  dot_dp: 1.6, dot_spacing_dp: 26,
  lanes: Object.freeze({ left: 80, center: 196, right: 312 }),
  ring: Object.freeze({ size_dp: 60, stroke_dp: 8, progress_percent: 55, label: '1/2' }),
  gloss_fab: Object.freeze({ cx: 340, cy: 650 }),
  states: Object.freeze(['done', 'cur-play', 'cur-half', 'next', 'bolt-active', 'bolt-optional', 'locked']),
});

/** Verify that the injected NODE payload really carries the original geometry. */
export function assertGeometry(NODE) {
  const g = NODE && NODE.nodeGeometry;
  if (!g) return { ok: false, reason: 'NODE.nodeGeometry missing' };
  const n = g.node || {};
  const errors = [];
  if (n.size_dp !== NODE_SPEC.size_dp) errors.push('size_dp');
  if (n.corner_radius_dp !== NODE_SPEC.corner_radius_dp) errors.push('corner_radius_dp');
  if (n.lip_dp !== NODE_SPEC.lip_dp) errors.push('lip_dp');
  if (n.icon_dp !== NODE_SPEC.icon_dp) errors.push('icon_dp');
  if (g.layout.lane_spacing_dp !== 116) errors.push('lane_spacing_dp');
  if (g.layout.pitch_dp !== NODE_SPEC.pitch_dp) errors.push('pitch_dp');
  if (g.layout.elbow_radius_dp !== NODE_SPEC.elbow_radius_dp) errors.push('elbow_radius_dp');
  return { ok: errors.length === 0, errors, source: g.round || 'v10' };
}

/** State of one node from real progress (DESIGN_CHOICE local unlock rule). */
export function stateFor(index, ids, completions, currentVariant = 'half') {
  const id = ids[index];
  if (!id) return 'locked';
  if (completions[id]) return 'done';
  const prevDone = index === 0 || Boolean(completions[ids[index - 1]]);
  if (!prevDone) return 'locked';
  return `cur-${currentVariant === 'play' ? 'play' : 'half'}`;
}

/** Apply original-app node classes/icons to the 6 approved node elements. */
export function applyOriginalNodes(doc, {
  ids, completions = {}, currentVariant = 'half', boltIndexes = [4, 5], PROTO,
  seedStates = null,
}) {
  const wrap = doc.querySelector('[data-screen="learn"] .pathwrap');
  if (!wrap) return { applied: 0 };
  const nodes = [...wrap.querySelectorAll('.node')];
  const states = [];
  const seeded = Boolean(seedStates) && Object.keys(completions).length === 0;
  nodes.forEach((el, i) => {
    let st;
    if (seeded) st = seedStates[i] || 'locked';
    else if (boltIndexes.includes(i)) st = i === boltIndexes[0] ? 'bolt-active' : 'bolt-optional';
    else if (completions[ids[i]]) st = 'done';
    else if (i > 0 && !completions[ids[i - 1]]) st = 'locked';
    else if (i === firstOpenIndex(ids, completions)) st = `cur-${currentVariant === 'play' ? 'play' : 'half'}`;
    else st = 'next';
    el.classList.remove('done', 'cur', 'half', 'play', 'next', 'locked', 'active', 'optional');
    if (st === 'done') el.classList.add('done');
    else if (st.startsWith('cur-')) {
      const cls = st === 'cur-play' ? ['cur', 'play'] : ['half'];
      cls.forEach((c) => el.classList.add(c));
    }
    else if (st === 'next') el.classList.add('next');
    else if (st === 'locked') el.classList.add('locked');
    else el.classList.add('bolt', st === 'bolt-active' ? 'active' : 'optional');
    el.dataset.state = st;
    el.dataset.lessonId = ids[i] || '';
    states.push(st);
  });
  addGlossFab(doc, wrap, PROTO);
  return { applied: nodes.length, states };
}

function firstOpenIndex(ids, completions) {
  for (let i = 0; i < ids.length; i += 1) if (!completions[ids[i]]) return i;
  return ids.length - 1;
}

/** Restore the floating book/dictionary affordance archived in v12.5-fa (PN-15). */
export function addGlossFab(doc, wrap, PROTO) {
  if (!wrap || wrap.querySelector('.gloss-fab')) return false;
  const fab = doc.createElement('div');
  fab.className = 'gloss-fab';
  fab.setAttribute('data-role', 'glossary');
  fab.setAttribute('title', 'واژهنامهٔ مبحث');
  fab.innerHTML = '<span class="abook">A</span>';
  wrap.appendChild(fab);
  return true;
}
