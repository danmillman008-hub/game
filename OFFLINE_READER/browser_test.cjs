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
 await page.screenshot({path:process.env.RUNNER_TEMP+'/reader-browser.png'});assert.deepEqual(external,[]);console.log('PASS Chromium file://, 19 paths, four navigation levels, 4 lesson transitions, zero external requests');
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
