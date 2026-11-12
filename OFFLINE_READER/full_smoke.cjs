const fs=require('fs'),assert=require('assert'),{JSDOM,VirtualConsole}=require('../app/node_modules/jsdom');
const html=fs.readFileSync(process.argv[2],'utf8');let v=new VirtualConsole();v.on('jsdomError',e=>{if(!String(e).includes('Not implemented: window.scrollTo'))throw e});
const d=new JSDOM(html,{runScripts:'dangerously',url:'https://offline.invalid/',virtualConsole:v}).window.document;
function first(){let e=d.querySelector('button.card');assert(e,'missing navigation card: '+d.querySelector('h1').textContent);e.click()}
assert.match(d.querySelector('h1').textContent,/learning path/i);first();first();first();first();assert(d.querySelector('h1'));assert([...d.querySelectorAll('button')].some(b=>/Next lesson|Finish chapter/.test(b.textContent)));console.log('PASS actual bundled data navigation to first lesson and next control');
