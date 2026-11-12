const fs=require('fs'),assert=require('assert'),puppeteer=require('../app/node_modules/puppeteer-core');
(async()=>{
 const browser=await puppeteer.launch({executablePath:process.env.CHROME_BIN||'/usr/bin/google-chrome',headless:true,args:['--no-sandbox','--disable-gpu']});
 try{
 const page=await browser.newPage(); await page.setViewport({width:390,height:844,deviceScaleFactor:1}); let external=[];
 await page.setRequestInterception(true);page.on('request',r=>{let u=r.url();if(!u.startsWith('file:')&&!u.startsWith('data:')&&!u.startsWith('about:')){external.push(u);return r.abort()}return r.continue()});
 await page.goto('file://'+process.argv[2],{waitUntil:'load',timeout:90000});
 await page.waitForSelector('button.card',{timeout:30000});let count=await page.$$eval('button.card',xs=>xs.length);assert.equal(count,19);
 for(let i=0;i<4;i++){await page.waitForSelector('button.card');await page.click('button.card');}
 assert(await page.$('.progress'),'lesson progress indicator missing');
 for(let i=0;i<4;i++){let nxt=await page.$('button.secondary:not(#back)');assert(nxt,'next not found at '+i);await nxt.click();assert(await page.$('main h1'));}
 const selection=await page.evaluate(()=>{for(const t of data.tracks)for(let si=0;si<t.sections.length;si++)for(const id of t.sections[si].tutorialIds){let u=data.tutorials[id];if(!u)continue;for(let ci=0;ci<u.chapters.length;ci++)for(let li=0;li<u.chapters[ci].lessons.length;li++){let l=u.chapters[ci].lessons[li],h=l.interactiveContent||'';if(!/<selection\b/i.test(h))continue;let d=new DOMParser().parseFromString(h,'text/html'), n=d.querySelector('body > selection');if(!n)continue;let items=[...n.querySelectorAll('item')],yes=items.map((x,i)=>x.getAttribute('correct')==='true'?i:-1).filter(i=>i>=0),no=items.findIndex(x=>x.getAttribute('correct')==='false');if(yes.length&&no>=0){nav={page:'lesson',track:t.id,section:si,tutorial:id,chapter:ci,lesson:li};render();return {yes,no,id:l.id}}}}return null});
 assert(selection,'no real selection found');let opts=await page.$$('main input[type=checkbox], main input[type=radio]');assert(opts.length>selection.no);await opts[selection.no].click();await page.evaluate(()=>[...document.querySelectorAll('button')].find(x=>x.textContent==='Check answer').click());assert.match(await page.$eval('#result',x=>x.textContent),/Not quite/);
 if((await opts[selection.no].evaluate(x=>x.type))==='checkbox')await opts[selection.no].click();for(const i of selection.yes)await opts[i].click();await page.evaluate(()=>[...document.querySelectorAll('button')].find(x=>x.textContent==='Check answer').click());assert.equal(await page.$eval('#result',x=>x.textContent),'Correct!');
 await page.screenshot({path:process.env.RUNNER_TEMP+'/reader-browser.png'});assert.deepEqual(external,[]);console.log('PASS Chromium file://, 19 paths, four navigation levels, 4 lesson transitions, actual selection wrong/right lesson='+selection.id+', zero external requests');
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
