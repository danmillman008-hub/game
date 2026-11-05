
(function(){
  "use strict";
  var q=function(s,r){return (r||document).querySelector(s)};
  var qa=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  var toastEl=q("#toast"),tt;
  function toast(m){toastEl.textContent=m;toastEl.classList.add("on");clearTimeout(tt);tt=setTimeout(function(){toastEl.classList.remove("on")},2300)}
  function fa(n){return String(n).replace(/\d/g,function(d){return "۰۱۲۳۴۵۶۷۸۹"[+d]})}
  /* ---------- ARGB -> CSS ---------- */
  function ac(c){
    if(!c||c.charAt(0)!=="#")return "currentColor";
    if(c.length===9){var a=parseInt(c.slice(1,3),16)/255;if(a===0)return "none";
      return "rgba("+parseInt(c.slice(3,5),16)+","+parseInt(c.slice(5,7),16)+","+parseInt(c.slice(7,9),16)+","+(+a.toFixed(3))+")";}
    if(c.length===7)return c; return "currentColor";
  }
  function icon(name,size,mono){
    var v=GEO.vectors[name];if(!v||!v.paths)return "";
    var h=Math.max(1,Math.round(size*v.viewport[1]/v.viewport[0]));
    var s='<svg class="ic" width="'+size+'" height="'+h+'" viewBox="0 0 '+v.viewport[0]+' '+v.viewport[1]+'" aria-hidden="true">';
    v.paths.forEach(function(p){
      var f=mono?"currentColor":ac(p.fill);
      if(f==="currentColor"&&!p.fill)f="currentColor";
      s+='<path d="'+p.d+'" fill="'+f+'"'+(p.fillType==="1"?' fill-rule="evenodd"':'')+(p.alpha?' fill-opacity="'+p.alpha+'"':'')+'/>';
    });
    return s+"</svg>";
  }
  function paintIcons(root){
    qa("[data-icon]",root||document).forEach(function(el){
      if(el.dataset.painted)return;
      el.innerHTML=icon(el.dataset.icon,+(el.dataset.size||24),el.dataset.mono==="1");
      el.dataset.painted="1";
    });
  }
  paintIcons();
  var gs=q("#geoStats");
  if(gs)gs.innerHTML="<b>شمارش:</b> "+Object.keys(GEO.vectors).length+" وکتور · "+Object.keys(GEO.colors).length+" رنگ · "+Object.keys(GEO.dimens).length+" دایمنشن · "+Object.keys(GEO.styles).length+" استایل · "+Object.keys(GEO.strings).length+" رشته · "+Object.keys(GEO.layouts).length+" لایه · "+GEO.compose_path_class_count+" کلاس Composeی مسیر";

  /* ---------- navigation ---------- */
  var tabMap={learn:"Learn",chapter:"Learn",lesson:"Learn","select-path":"Learn","path-overview":"Learn","section-detail":"Learn","section-practice":"Learn",leaderboard:"Leaderboard","user-profile":"Leaderboard",profile:"Profile","exam-hub":"Practice","exam-run":"Practice","exam-result":"Practice",ai:"AI"};
  var tabScreen={Learn:"learn",Practice:"exam-hub",AI:"ai",Leaderboard:"leaderboard",Profile:"profile"};
  function go(name){
    if(window.PROTO_NAV)try{window.PROTO_NAV(name)}catch(e){}
    var prev=q(".screen.on");var prevName=prev?prev.dataset.screen:"learn";
    qa(".screen").forEach(function(s){s.classList.toggle("on",s.dataset.screen===name)});
    qa("#switcher button").forEach(function(b){b.classList.toggle("on",b.dataset.go===name)});
    qa("#tabs .tab").forEach(function(t){t.classList.toggle("on",t.dataset.tab===tabMap[name])});
    if(name!=="exam-run"){qa(".sheet").forEach(function(s){s.classList.remove("on")})}
    if(name!=="chapter"){qa(".modal").forEach(function(m){m.classList.remove("on")})}
    if(name==="chapter"){go(prevName);q("#chapterModal").classList.add("on");qa("#switcher button").forEach(function(b){b.classList.toggle("on",b.dataset.go==="chapter")});return}
    var sc=q('.screen[data-screen="'+name+'"]');if(sc)sc.scrollTop=0;
  }
  document.addEventListener("click",function(e){
    var g=e.target.closest("[data-go]");if(g){go(g.dataset.go);return}
    var n=e.target.closest("[data-nav]");if(n){go(n.dataset.nav);return}
    var sh=e.target.closest("[data-sheet]");if(sh){var t=q("#"+sh.dataset.sheet);if(t)t.classList.add("on");return}
    var cl=e.target.closest("[data-close]");if(cl){var c=q("#"+cl.dataset.close);if(c)c.classList.remove("on");return}
    var h=e.target.closest("[data-help]");if(h){toast("راهنمای «"+h.dataset.help+"»: گامبهگام، همان الگوی helpcenter");return}
    var lh=e.target.closest("[data-lh]");if(lh){toast("چارچوب یادگیری ← "+(lh.dataset.fa||"شاهد کد"));return}
    var kt=e.target.closest("#keytabs button");if(kt){qa("#keytabs button").forEach(function(b){b.classList.remove("on")});kt.classList.add("on");qa(".keypanel").forEach(function(p){p.classList.toggle("on",p.id===kt.dataset.key)});return}
    if(e.target.closest("#curNode")){q("#chapterModal").classList.add("on");return}
    if(e.target.closest("#myRow")){go("user-profile");return}
    if(e.target.closest("#startLearning")){q("#chapterModal").classList.remove("on");go("lesson");return}
  });
  var tabFa={Learn:"یادگیری",Practice:"تمرین",AI:"هوش مصنوعی",Leaderboard:"امتیازها",Profile:"پروفایل"};
  qa("#tabs .tab").forEach(function(t){t.addEventListener("click",function(){go(tabScreen[t.dataset.tab]);toast("تب "+tabFa[t.dataset.tab]+" · ناوبری ۵ تب میمو")})});
  var themeBtn=q("#themeBtn");
  if(themeBtn)themeBtn.addEventListener("click",function(){document.body.classList.toggle("night");this.textContent=document.body.classList.contains("night")?"☀️ حالت روز":"🌙 حالت شب"});
  var rtl=false;
  /* v12.5-fa: لیبلها پیشفرض فارسیاند؛ دکمه فقط جهت را آینه میکند و متن انگلیسی برنمیگرداند */
  var dirBtn=q("#dirBtn");
  if(dirBtn)dirBtn.addEventListener("click",function(){
    rtl=!rtl;var ph=q("#phone");ph.style.direction=rtl?"rtl":"ltr";
    qa(".mimo,.exv12",ph).forEach(function(s){s.style.direction=rtl?"rtl":"ltr"});
    this.textContent=rtl?"↔ چپبراست":"↔ راستبهچپ";
    toast(rtl?"آینهٔ راستبهچپ · لیبلها فارسی":"نمای چپبراست · لیبلها فارسی");
  });

  /* ---------- exam policy: پاسخبرگ / پاسخنامه ---------- */
  var POLICY={
    comprehensive:{label:"جامع · زمان خالص آزمون · پاسخنامه در پایان",during:false,keyDuring:false},
    review:{label:"جمع بندی / نهایی · زمان خالص آزمون",during:false,keyDuring:false},
    normal:{label:"عادی · پاسخبرگ + پاسخنامه حین آزمون",during:true,keyDuring:true},
    timed:{label:"زماندار · پاسخبرگ + پاسخنامه حین آزمون",during:true,keyDuring:true},
    analytical:{label:"تحلیلی · پاسخبرگ + پاسخنامه حین و بعد",during:true,keyDuring:true}
  };
  var EXAM_KIND="comprehensive";
  function applyPolicy(){
    var p=POLICY[EXAM_KIND]||POLICY.normal;
    q("#answerSheetBtn").style.display=p.during?"":"none";
    q("#answerKeyBtn").style.display=p.keyDuring?"":"none";
    q("#resultKind").textContent=EXAM_KIND==="comprehensive"?"جامع":p.label.split(" · ")[0];
    /* v8: no policy explanation inside the UI */
  }
  /* v12.1 B2: the WHOLE Mimo list row is clickable, not just the 44dp icon */
  function openExam(n){
    if(SAVED&&SAVED.exam===n.dataset.exam){resumeExam();return}
    EXAM_KIND=n.dataset.kind||"normal";q("#examTitle").textContent=n.dataset.exam;
    QI=0;MARKS={};ANSWERS={};CHECKED={};q("#examFinished").innerHTML="";resetOptions();renderQuestion();
    T.state="idle";clearInterval(T.timer);T.timer=null;render();
    /* 270 is a preset, NOT a lock: the same field stays editable for every kind */
    q("#timerMinutes").value=EXAM_KIND==="comprehensive"?270:30;
    q("#timerMinutes").readOnly=false;
    applyPolicy();go("exam-run");toast("وارد «"+n.dataset.exam+"» شدید — "+(POLICY[EXAM_KIND]||POLICY.normal).label);
  }
  var ehRows=qa('[data-screen="exam-hub"] .grid3 > div');
  ehRows.forEach(function(row){
    var n=row.querySelector(".nodek[data-exam]");if(!n)return;
    row.setAttribute("role","button");row.tabIndex=0;
    row.addEventListener("click",function(){openExam(n)});
    row.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();openExam(n)}});
    /* B7: the previously hidden .mini badge becomes the row subtitle */
    var mini=row.querySelector(".mini"),lab=row.querySelector(".label");
    if(mini&&lab){mini.className="row-meta";lab.appendChild(mini)}
  });
  /* v12.1 B3: filter chips were decorative; wire them to the 7 labelled sections */
  var ehSec=q('[data-screen="exam-hub"]'),ehGroups=[],ehCur=null;
  Array.prototype.forEach.call(ehSec.children,function(c){
    if(c.classList.contains("sec")){ehCur=[c];ehGroups.push(ehCur)}
    else if(ehCur&&(c.classList.contains("cat-meta")||c.classList.contains("grid3")))ehCur.push(c);
  });
  qa('[data-screen="exam-hub"] .chips .chip').forEach(function(ch){
    ch.addEventListener("click",function(){
      qa('[data-screen="exam-hub"] .chips .chip').forEach(function(x){x.classList.remove("on")});
      ch.classList.add("on");
      var want=(ch.dataset.filter==="all")?null:ch.dataset.filter.split(",");
      ehGroups.forEach(function(g,i){
        var show=!want||want.indexOf(String(i))>=0;
        g.forEach(function(el){el.style.display=show?"":"none"});
      });
    });
  });
  applyPolicy();

  /* ---------- timer state machine · v12.5: ONE chip, manual minutes for EVERY exam kind ---------- */
  var T={state:"idle",remaining:0,total:0,timer:null,endAt:0};
  var wrap=q("#timerWrap"),chip=q("#timerChip"),label=q("#timerLabel"),ctl=q("#timerControls");
  function fmt(s){var m=Math.floor(s/60),x=s%60;return fa(m>=100?String(m):("0"+m).slice(-2))+":"+fa(("0"+x).slice(-2))}
  function pauseOrResume(){
    if(T.state==="running"){T.remaining=Math.max(0,Math.ceil((T.endAt-Date.now())/1000));T.state="paused";clearInterval(T.timer);T.timer=null;toast("تایمر متوقف شد")}
    else if(T.state==="paused"){T.endAt=Date.now()+T.remaining*1000;T.state="running";T.timer=setInterval(tick,250);toast("ادامهٔ تایمر")}
    render();
  }
  function render(){
    wrap.classList.remove("running","finished");
    var pb=q("#timerPause"),bars=pb.querySelector(".tm-bars"),play=pb.querySelector(".tm-play");
    if(T.state==="idle"||T.state==="setting"){label.textContent="تنظیم زمان";ctl.hidden=true}
    else if(T.state==="running"){
      label.textContent=fmt(T.remaining);wrap.classList.add("running");ctl.hidden=false;
      pb.classList.remove("is-paused");pb.setAttribute("aria-label","توقف تایمر");bars.hidden=false;play.hidden=true;
    } else if(T.state==="paused"){
      label.textContent=fmt(T.remaining);wrap.classList.add("running");ctl.hidden=false;
      pb.classList.add("is-paused");pb.setAttribute("aria-label","ادامهٔ تایمر");bars.hidden=true;play.hidden=false;
    } else if(T.state==="finished"){label.textContent=fmt(0);wrap.classList.add("finished");ctl.hidden=true}
  }
  function tick(){if(T.state!=="running")return;T.remaining=Math.max(0,Math.ceil((T.endAt-Date.now())/1000));if(T.remaining===0)finishExam("زمان تمام شد (ثبت خودکار)");render()}
  function finishExam(reason,partial){
    T.state="finished";clearInterval(T.timer);T.timer=null;
    q("#examFinished").innerHTML='<div class="banner warn">'+reason+' — گزینهها قفل و پاسخها ثبت شدند.</div>';
    qa(".opt").forEach(function(o){o.style.pointerEvents="none";o.style.opacity=".55"});
    /* the exam is over: no saved run is left behind, the کارنامه is the result screen */
    SAVED=null;q("#resumeBar").hidden=true;if(window.PROTO_PERSIST)try{window.PROTO_PERSIST(null)}catch(e){}
    go("exam-result");render();renderReport(!!partial);
    var p=POLICY[EXAM_KIND]||POLICY.normal;
    if(partial){toast("کارنامهٔ تا این لحظه — درصد پاسخهای زدهشده")}
    else if(!p.during){q("#keySheet").classList.add("on");toast("پایان آزمون: صفحهٔ پاسخنامه باز شد")}
    else toast("آزمون به پایان رسید — پاسخبرگ و پاسخنامه آمادهاند");
  }
  chip.addEventListener("click",function(){
    if(T.state==="running"||T.state==="paused"){pauseOrResume();return}
    q("#timerSheet").classList.add("on");T.state="setting";
    /* v12.5: manual minutes in EVERY exam kind — the field is never locked.
       270 is only the comprehensive preset, assigned once in openExam(). */
    var fld=q("#timerMinutes");fld.readOnly=false;fld.removeAttribute("readonly");
    q("#timerHint").textContent="مدت دلخواه به دقیقه — در همهٔ آزمونها قابل تغییر است"+(EXAM_KIND==="comprehensive"?" (پیشفرض جامع: ۲۷۰ دقیقه)":"");
    render();
  });
  qa("[data-min]").forEach(function(b){b.addEventListener("click",function(){q("#timerMinutes").value=b.dataset.min;qa("[data-min]").forEach(function(x){x.classList.remove("on")});b.classList.add("on")})});
  q("#timerStart").addEventListener("click",function(){
    var m=parseInt(q("#timerMinutes").value,10);if(!m||m<1){toast("مدت آزمون را به دقیقه وارد کنید");return}
    T.total=m*60;T.remaining=T.total;T.endAt=Date.now()+T.total*1000;T.state="running";
    clearInterval(T.timer);T.timer=setInterval(tick,250);
    q("#timerSheet").classList.remove("on");q("#examFinished").innerHTML="";resetOptions();restoreAnswer();
    toast("شروع شد: "+fa(m)+" دقیقه معکوس");render();
  });
  q("#timerPause").addEventListener("click",function(e){e.stopPropagation();pauseOrResume()});
  q("#timerReset").addEventListener("click",function(e){
    e.stopPropagation();clearInterval(T.timer);T.timer=null;T.state="idle";T.remaining=0;T.total=0;
    q("#examFinished").innerHTML="";resetOptions();restoreAnswer();q("#timerSheet").classList.remove("on");
    toast("تایمر پاک شد");render();
  });
  function resetOptions(){qa(".opt").forEach(function(o){o.style.pointerEvents="";o.style.opacity="";o.classList.remove("on","correct","wrong")})}
  /* ============ v12.1 · Mimo lesson_interactive question flow (corrected) ============
     ChoiceView -> btn_submit (بررسی پاسخ) -> feedback bottom sheet -> btn_continue_big
     (ادامه) -> next question.  btn_undo = سؤال قبل (48dp square).  No equal prev/next pair.
     B5: 20 distinct questions match the declared QTOTAL; QI resets for every new exam. */
  var QRAW=[
    ["زیست · سمها · دشواری متوسط","کدامیک از گزینههای زیر دربارهٔ «سمها» درست است؟",["سمها همواره تنها در کبد ساخته میشوند","سمها میتوانند با اتصال به آنزیمها، فعالیت آنها را مهار کنند","همهٔ سمها در بدن به گلوکز تبدیل میشوند","سمها فقط از راه پوست وارد بدن میشوند"],1,"سمها با اتصال به جایگاه فعال آنزیمها میتوانند آنها را مهار کنند؛ زیست یازدهم، فصل سمها و بیماریها."],
    ["شیمی · تعادل شیمیایی · دشواری متوسط","ثابت تعادل یک واکنش برگشتپذیر در دمای ثابت، با افزایش غلظت یکی از واکنشدهندهها…",["کاهش مییابد","افزایش مییابد","تغییر نمیکند","صفر میشود"],2,"Kc فقط تابع دماست؛ تغییر غلظت سامانه را جابهجا میکند ولی مقدار ثابت تعادل ثابت میماند (اصل لوشاتلیه)."],
    ["فیزیک · ترمودینامیک · دشواری سخت","کار انجامشده توسط گاز در یک فرایند همحجم برابر است با…",["PΔV","صفر","nRΔT","ΔU"],1,"در فرایند همحجم ΔV=۰ است، پس W=PΔV=۰ و تمام گرما صرف تغییر انرژی درونی میشود."],
    ["ریاضی · مشتق · دشواری متوسط","مشتق تابع f(x)=x³−3x در x=۱ کدام است؟",["۰","۱","۳","۶"],0,"f′(x)=3x²−3، پس f′(1)=0؛ نقطهٔ بحرانی و اکسترمم نسبی."],
    ["زیست · ژنتیک · دشواری آسان","در قانون دوم مندل (تفکیک)، نسبت ژنوتیپی نسل F₂ برای یک صفت تکژنی چیست؟",["۳:۱","۱:۲:۱","۹:۳:۳:۱","۱:۱"],1,"نسبت فنوتیپی ۳:۱ و نسبت ژنوتیپی ۱:۲:۱ است (AA:Aa:aa)."],
    ["شیمی · پیوند شیمیایی · دشواری آسان","کدام عنصر الکترونگاتیویتر است؟",["سدیم","منیزیم","کلر","پتاسیم"],2,"الکترونگاتیوی در یک دوره از چپ به راست افزایش و در یک گروه از بالا به پایین کاهش مییابد؛ کلر بیشینه است."],
    ["فیزیک · نور و پرتو · دشواری متوسط","هنگام گذر نور از هوا به شیشه، کدام کمیت ثابت میماند؟",["سرعت نور","طول موج","بسامد","جهت پرتو"],2,"بسامد نور هنگام تغییر محیط ثابت است؛ سرعت و طول موج تغییر میکنند و پرتو میشکند."],
    ["ریاضی · دنبالهها · دشواری متوسط","حد دنبالهٔ aₙ=(2n+1)/(3n−1) کدام است؟",["۰","۲/۳","۱","∞"],1,"با تقسیم صورت و مخرج بر n، حد برابر ۲/۳ میشود."],
    ["زیست · سلول · دشواری متوسط","کدام اندامک مسئول ساخت ATP در یاختهٔ یوکاریوتی است؟",["ریبوزوم","میتوکندری","دستگاه گلژی","شبکهٔ آندوپلاسمی"],1,"میتوکندری با تنفس یاخته‌ای ATP میسازد؛ ریبوزوم محل ساخت پروتئین است."],
    ["شیمی · استوکیومتری · دشواری متوسط","چند مولکول آب از واکنش کامل ۲ مول هیدروژن با اکسیژن کافی بهدست میآید؟",["۱ مول","۲ مول","۳ مول","۴ مول"],1,"2H₂+O₂→2H₂O؛ نسبت مولی H₂ به H₂O برابر ۱:۱ است، پس ۲ مول آب."],
    ["فیزیک · مکانیک · دشواری سخت","نیروی ۱۲ نیوتونی به جسمی به جرم ۳ کیلوگرم وارد میشود؛ شتاب چند متر بر مجذور ثانیه است؟",["۲","۳","۴","۱۲"],2,"قانون دوم نیوتون: a=F/m=۱۲/۳=۴ m/s²."],
    ["ریاضی · احتمال · دشواری متوسط","در پرتاب یک تاس سالم، احتمال آمدن عدد زوج چقدر است؟",["۱/۶","۱/۳","۱/۲","۲/۳"],2,"اعداد زوج ۲، ۴ و ۶اند؛ ۳ حالت مطلوب از ۶ حالت، یعنی ۱/۲."],
    ["زیست · فتوسنتز · دشواری متوسط","واکنشهای نوری فتوسنتز در کدام بخش کلروپلاست رخ میدهند؟",["استروما","تیلاکوئید","دیوارهٔ یاخته","واکوئول"],1,"واکنشهای نوری در غشای تیلاکوئید و چرخهٔ کالوین در استروما انجام میشود."],
    ["شیمی · محلولها · دشواری آسان","افزایش دما معمولاً انحلالپذیری نمکهای جامد در آب را…",["کاهش میدهد","افزایش میدهد","تغییر نمیدهد","صفر میکند"],1,"انحلال اغلب نمکهای جامد گرماگیر است؛ با افزایش دما انحلالپذیری بیشتر میشود."],
    ["فیزیک · الکتریسیته · دشواری متوسط","دو مقاومت ۶ و ۳ اهمی بهصورت موازی بسته شوند؛ مقاومت معادل چقدر است؟",["۹ اهم","۴٫۵ اهم","۲ اهم","۱ اهم"],2,"1/R=1/6+1/3=1/2، پس R=۲ اهم."],
    ["ریاضی · مثلثات · دشواری متوسط","مقدار sin²x+cos²x برای هر zاویهٔ x کدام است؟",["۰","۱/۲","۱","۲"],2,"اتحاد بنیادی مثلثات: sin²x+cos²x=۱."],
    ["زیست · گردش خون · دشواری آسان","خون سرشار از اکسیژن از ششها به کدام حفرهٔ قلب بازمیگردد؟",["دهلیز راست","بطن راست","دهلیز چپ","بطن چپ"],2,"سیاهرگهای ششی خون اکسیژندار را به دهلیز چپ میآورند."],
    ["شیمی · سینتیک · دشواری سخت","کاتالیزگر در یک واکنش شیمیایی چه میکند؟",["آنتروپی را تغییر میدهد","انرژی فعالسازی را کاهش میدهد","تعادل را جابهجا میکند","دمای واکنش را افزایش میدهد"],1,"کاتالیزگر مسیری با انرژی فعالسازی کمتر فراهم میکند؛ ثابت تعادل و ΔG را تغییر نمیدهد."],
    ["فیزیک · موج · دشواری متوسط","اگر بسامد موجی دو برابر شود و سرعت ثابت بماند، طول موج…",["دو برابر میشود","نصف میشود","ثابت میماند","چهار برابر میشود"],1,"v=fλ؛ با ثابت بودن v، دو برابر شدن f یعنی نصف شدن λ."],
    ["ریاضی · انتگرال · دشواری سخت","∫(2x+1)dx کدام است؟",["x²+x+C","2x²+x+C","x²+C","2+C"],0,"انتگرال جزءبهجزء: x²+x+C (C ثابت انتگرالگیری)."]
  ];
  var QBANK=QRAW.map(function(r){return {sub:r[0],stem:r[1],opts:r[2],ok:r[3],expl:r[4]}});
  var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={};
  /* v12.5 · prototype-only in-memory state: chosen option per question, whether its
     feedback was shown, and the snapshot taken by «خروج و ذخیره». */
  var ANSWERS={},CHECKED={},SAVED=null;
  function renderQuestion(){
    var item=QBANK[QI%QBANK.length];
    q("#examStep").textContent="سؤال "+fa(QI+1)+" از "+fa(QTOTAL);
    /* B5: build the subject chip from DOM nodes (no innerHTML / no esc() dependency) */
    var subj=q("#examSubject");subj.innerHTML="";
    var dot=document.createElement("span");dot.className="lb-dot";subj.appendChild(dot);
    item.sub.split(" · ").forEach(function(part,i){
      if(i){var sep=document.createElement("span");sep.className="lb-sep";sep.textContent="·";subj.appendChild(sep)}
      var t=document.createElement("span");t.textContent=part;subj.appendChild(t);
    });
    q("#qText").textContent=item.stem;
    qa("#exChoices .opt").forEach(function(o,i){o.querySelector(".opt-txt").textContent=item.opts[i]});
    resetOptions();q("#exFeedback").hidden=true;QCHECKED=false;
    restoreAnswer();paintPalette();
    q("#nextQLabel").textContent=(q(".opt.on")&&!QCHECKED)?"بررسی پاسخ":"ادامه";
    q("#examProgress").style.width=Math.min(100,((QI+1)/QTOTAL)*100)+"%";
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
  }
  function setCtaLabel(){q("#nextQLabel").textContent=(q(".opt.on")&&!QCHECKED)?"بررسی پاسخ":"ادامه"}
  qa(".opt").forEach(function(o){o.addEventListener("click",function(){
    if(T.state==="finished")return;
    qa(".opt").forEach(function(x){x.classList.remove("on","correct","wrong")});
    o.classList.add("on");ANSWERS[QI]=+o.dataset.opt;CHECKED[QI]=false;QCHECKED=false;q("#exFeedback").hidden=true;setCtaLabel();
  })});
  q("#nextQ").addEventListener("click",function(){
    var chosen=q(".opt.on");
    if(chosen&&!QCHECKED){
      var item=QBANK[QI%QBANK.length];
      var ok=+chosen.dataset.opt-1===item.ok;
      ANSWERS[QI]=+chosen.dataset.opt;CHECKED[QI]=true;QCHECKED=true;
      chosen.classList.remove("on");chosen.classList.add(ok?"correct":"wrong");
      var fb=q("#exFeedback");fb.classList.toggle("bad",!ok);fb.hidden=false;
      q("#exFeedbackTitle").textContent=ok?"پاسخ درست است":"پاسخ نادرست است";
      q("#exFeedbackText").textContent=item.expl;
      q("#nextQLabel").textContent="ادامه";toast(ok?"درست ✔ پاسخنامهٔ تشریحی نشان داده شد":"نادرست ✕ توضیح مبحث نشان داده شد");
      return;
    }
    QI=Math.min(QTOTAL-1,QI+1);renderQuestion();toast("سؤال بعدی · "+fa(QI+1)+" از "+fa(QTOTAL));
  });
  q("#prevQ").addEventListener("click",function(){QI=Math.max(0,QI-1);renderQuestion();toast("سؤال قبل · "+fa(QI+1)+" از "+fa(QTOTAL))});
  q("#markQ").addEventListener("click",function(){
    if(MARKS[QI])delete MARKS[QI];else MARKS[QI]=true;
    q("#markQ").classList.toggle("marked",!!MARKS[QI]);
    toast(MARKS[QI]?"سؤال علامتگذاری شد":"علامت برداشته شد");
  });
  renderQuestion();
  q("#submitExam").addEventListener("click",function(){q("#paletteSheet").classList.remove("on");finishExam("پاسخها ثبت شد")});
  var pal=q("#palette");for(var i=1;i<=20;i++){
    var d=document.createElement("div");d.innerHTML="<span>"+fa(i)+"</span>"+(i<15?"<small>"+fa((i%4)+1)+"</small>":"<small>—</small>");
    if(i<15)d.className="done";if(i===3)d.className="cur";pal.appendChild(d);
  }
  paintPalette();

  /* ---------- v12.5 · answer state, save/resume, partial & full کارنامه ---------- */
  function restoreAnswer(){
    var a=ANSWERS[QI];if(!a)return;
    var pick=null;qa("#exChoices .opt").forEach(function(o){if(+o.dataset.opt===a)pick=o});
    if(!pick)return;
    var item=QBANK[QI%QBANK.length];
    if(CHECKED[QI]){
      var ok=a-1===item.ok;
      pick.classList.add(ok?"correct":"wrong");QCHECKED=true;
      var fb=q("#exFeedback");fb.classList.toggle("bad",!ok);fb.hidden=false;
      q("#exFeedbackTitle").textContent=ok?"پاسخ درست است":"پاسخ نادرست است";
      q("#exFeedbackText").textContent=item.expl;
    }else pick.classList.add("on");
  }
  function paintPalette(){
    /* keep the v12.1 static 20-cell demo sheet until a real answer is recorded */
    if(!Object.keys(ANSWERS).length)return;
    var cells=qa("#palette > div");if(cells.length!==20)return;
    cells.forEach(function(c,i){var a=ANSWERS[i];c.className=i===QI?"cur":(a?"done":"");
      var sm=c.querySelector("small");if(sm)sm.textContent=a?fa(a):"—"});
  }
  function score(){
    var correct=0,wrong=0,answered=0;
    Object.keys(ANSWERS).forEach(function(k){
      var i=+k,a=ANSWERS[k];if(!a)return;
      answered++;if(a-1===QBANK[i%QBANK.length].ok)correct++;else wrong++;
    });
    return {correct:correct,wrong:wrong,blank:QTOTAL-answered,answered:answered,
            pct:answered?Math.max(0,Math.round((correct-wrong/3)/answered*100)):0,
            pctNoNeg:answered?Math.round(correct/answered*100):0};
  }
  /* partial = «پایان آزمون و دیدن کارنامه / خروج و دیدن درصد»;
     full    = «ثبت پاسخها و پایان» / اتمام تایمر، حتی بعد از ادامهٔ آزمون ذخیرهشده */
  function renderReport(partial){
    var s=score();
    if(partial){
      q("#resTitle").textContent="کارنامهٔ تا این لحظه";
      q("#resSub").textContent="پایان زودهنگام · "+fa(s.answered)+" پاسخ زدهشده محاسبه شد"+(s.answered?"":" (هنوز پاسخی ثبت نشده است)");
      q("#resPctLabel").textContent="درصد تا این لحظه (با نمرهٔ منفی)";
      q("#resPct").textContent=fa(s.pct)+"٪";
      q("#resPctNoNeg").textContent=fa(s.pctNoNeg)+"٪";
      q("#resWrongBlank").textContent=fa(s.wrong)+" / "+fa(s.blank);
      q("#resRank").textContent="—";
      q("#resultKind").textContent="تا این لحظه";
      var b=q("#resPartial");b.hidden=false;
      b.textContent="خروج و دیدن درصد: این عدد فقط از "+fa(s.answered)+" پاسخی که تا همینجا زدهاید بهدست آمد ("+fa(s.correct)+" درست · "+fa(s.wrong)+" غلط)؛ "+fa(s.blank)+" سؤال نزده ماندهاند.";
    }else{
      q("#resTitle").textContent="آزمون تمام شد!";
      q("#resSub").textContent="۳ سؤال نیاز به مرور دارد. پاسخنامهٔ تشریحی آماده است.";
      q("#resPctLabel").textContent="درصد با نمرهٔ منفی";
      q("#resPct").textContent="۶۸٪";
      q("#resPctNoNeg").textContent="۷۴٪";
      q("#resWrongBlank").textContent="۴ / ۵";
      q("#resRank").textContent="۱۲۴۰ / ۶۲۰۰";
      q("#resultKind").textContent=EXAM_KIND==="comprehensive"?"جامع":(POLICY[EXAM_KIND]||POLICY.normal).label.split(" · ")[0];
      q("#resPartial").hidden=true;
    }
  }
  function saveExam(){
    if(T.state==="running"){
      T.remaining=Math.max(0,Math.ceil((T.endAt-Date.now())/1000));
      clearInterval(T.timer);T.timer=null;T.state="paused";render();
    }
    SAVED={exam:q("#examTitle").textContent,kind:EXAM_KIND,qi:QI,
      answers:Object.assign({},ANSWERS),checked:Object.assign({},CHECKED),marks:Object.assign({},MARKS),
      minutes:q("#timerMinutes").value,
      timer:{state:T.state,remaining:T.remaining,total:T.total}};
    q("#resumeBar").hidden=false;
    q("#resumeText").textContent="«"+SAVED.exam+"» · سؤال "+fa(QI+1)+" از "+fa(QTOTAL)+" ذخیره شد";
    if(window.PROTO_PERSIST)try{window.PROTO_PERSIST(SAVED)}catch(e){}
    toast("پیشرفت ذخیره شد — بعداً از همان سؤال ادامه میدهید");
  }
  function resumeExam(){
    if(!SAVED)return;
    var sv=SAVED;
    EXAM_KIND=sv.kind;q("#examTitle").textContent=sv.exam;
    QI=sv.qi;ANSWERS=Object.assign({},sv.answers);CHECKED=Object.assign({},sv.checked);MARKS=Object.assign({},sv.marks);
    q("#timerMinutes").value=sv.minutes;q("#timerMinutes").readOnly=false;
    T.state=sv.timer.state;T.remaining=sv.timer.remaining;T.total=sv.timer.total;
    T.endAt=Date.now()+T.remaining*1000;clearInterval(T.timer);T.timer=null;
    if(T.state==="running")T.state="paused"; /* ادامه با همان پلی داخل چیپ تایمر */
    q("#examFinished").innerHTML="";renderQuestion();render();applyPolicy();go("exam-run");
    q("#resumeBar").hidden=true;SAVED=null;if(window.PROTO_PERSIST)try{window.PROTO_PERSIST(null)}catch(e){}
    toast("ادامهٔ آزمون ذخیرهشده · سؤال "+fa(QI+1));
  }
  q("#exitSaveBtn").addEventListener("click",saveExam);
  q("#exitFinishBtn").addEventListener("click",function(){
    q("#exitSheet").classList.remove("on");finishExam("پایان آزمون و دیدن کارنامه",true);
  });
  q("#resumeBtn").addEventListener("click",resumeExam);

  /* ---------- ONE AI button: exam questions page + exam final page ---------- */
  var WRONG=[
    {q:"سؤال ۲ · زیست / سمها — «کدام گزینه دربارهٔ سمها درست است؟»",a:"پاسخ شما: گزینهٔ ۴",k:"پاسخ صحیح: گزینهٔ ۱"},
    {q:"سؤال ۴ · شیمی / تعادل — «ثابت تعادل در دمای ثابت…»",a:"پاسخ شما: نزده",k:"پاسخ صحیح: گزینهٔ ۴"},
    {q:"سؤال ۹ · فیزیک / ترمودینامیک — «کار انجامشده در فرایند همحجم…»",a:"پاسخ شما: گزینهٔ ۲",k:"پاسخ صحیح: گزینهٔ ۳"}
  ];
  function setCtx(txt,summary){
    var c=q("#aiContext");c.hidden=false;c.textContent=txt;
    var th=q("#chatThread");
    qa(".ctx-detail",th).forEach(function(x){x.remove()});
    if(summary){var d=document.createElement("div");d.className="bubble ctx-detail";d.innerHTML=summary;th.insertBefore(d,q("#typing"));th.scrollTop=th.scrollHeight}
  }
  q("#askAiBtn").addEventListener("click",function(){
    var chosen=(q(".opt.on")||{}).textContent||"هنوز انتخاب نشده";
    setCtx("زمینه: "+q("#examTitle").textContent+" · سؤال "+fa(QI+1)+" · "+q("#qText").textContent+" · پاسخ شما: "+chosen.trim(),null);
    go("ai");toast("صورت سؤال و پاسخ شما به چت مینیمال منتقل شد");
  });
  q("#askAiResultBtn").addEventListener("click",function(){
    var s="<b>صورت اشتباهات + پاسخهای من + صورت سؤالها:</b><br>";
    WRONG.forEach(function(w){s+="• "+w.q+" | "+w.a+" | "+w.k+"<br>"});
    setCtx("زمینه: نتیجهٔ "+q("#examTitle").textContent+" · ۳ سؤال غلط (همراه پاسخ و صورت سؤال)",s);
    go("ai");toast("اشتباهات، پاسخها و صورت سؤالها به هوش مصنوعی منتقل شد");
  });

  /* ---------- minimal chat ---------- */
  var HIST=[{t:"مشتق و کاربرد آن",m:"دیروز · ۴ پیام"},{t:"سمها — زیست یازدهم",m:"۲ روز پیش · ۶ پیام"},{t:"تحلیل آزمون جامع",m:"۳ روز پیش · ۳ پیام"}];
  function histRender(){var box=q("#histList");box.innerHTML="";HIST.forEach(function(h){var d=document.createElement("div");d.className="hist-item";var s=document.createElement("small");s.textContent=h.m;d.appendChild(document.createTextNode(h.t));d.appendChild(s);d.addEventListener("click",function(){q("#historySheet").classList.remove("on");toast("گفتگو باز شد: "+h.t)});box.appendChild(d)})}
  function addBubble(txt,me){var d=document.createElement("div");d.className="bubble"+(me?" me":"");d.textContent=txt;var th=q("#chatThread");th.insertBefore(d,q("#typing"));th.scrollTop=th.scrollHeight;return d}
  q("#aiSend").addEventListener("click",function(){
    var v=q("#aiInput").value.trim();if(!v){toast("یک پیام بنویسید");return}
    addBubble(v,true);q("#aiInput").value="";q("#typing").hidden=false;
    setTimeout(function(){q("#typing").hidden=true;addBubble("بیا قدمبهقدم جلو بریم: اول صورت سؤال رو با هم مرور میکنیم، بعد یه تست مشابه میزنیم.","")},700);
    toast("ارسال به چارچوب یادگیری");
  });
  q("#aiInput").addEventListener("keydown",function(e){if(e.key==="Enter")q("#aiSend").click()});
  q("#newChat").addEventListener("click",function(){
    var th=q("#chatThread");qa(".bubble",th).forEach(function(x){x.remove()});
    q("#aiContext").hidden=true;addBubble("سلام! روی کدوم مبحث میخوای کار کنیم؟","");
    q("#historySheet").classList.remove("on");toast("گفتگوی تازه شروع شد");
  });
  qa("#mode button").forEach(function(b){b.addEventListener("click",function(){qa("#mode button").forEach(function(x){x.classList.remove("on")});b.classList.add("on");toast("حالت "+b.dataset.fa+" انتخاب شد")})});

  /* ============ v6 · Learn sub-screens rendered from extracted code data ============ */
  function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
  var LS=LEARN.strings, CM=LEARN.contentModel;
  /* ============ v11 · program-based / topic-based Konkur tracks ============ */
  var V11_PROGRAMS=KONKUR.programs, V11_COURSES=KONKUR.courses, V11_DATES=KONKUR.dates;
  var V11_SUBJECT_LINE=KONKUR.lessons_line, V11_SUBJECTS=KONKUR.subjects;
  var V11_SEL={kind:"program",key:"grade12"}, V11_ROWS=[];
  function v11Course(k){for(var i=0;i<V11_COURSES.length;i++)if(V11_COURSES[i].key===k)return V11_COURSES[i];return null}
  function v11Program(k){for(var i=0;i<V11_PROGRAMS.length;i++)if(V11_PROGRAMS[i].key===k)return V11_PROGRAMS[i];return null}
  function v11Lab(s){return ' data-fa="'+esc(s)+'"'}
  /* 4 BIG cards — icons are decoded Mimo vectors, never programming emblems */
  var V11_CARDS=V11_PROGRAMS.map(function(p){return {key:p.key,kind:"program",label:p.label,icon:p.icon,sec:"۲/۱۰",pct:22}});
  var CC=q("#careerCards");CC.innerHTML="";
  V11_CARDS.forEach(function(c,i){
    var b=document.createElement("button");b.className="career-card"+(i===0?" sel":"");
    b.dataset.v11=c.kind+":"+c.key;
    b.setAttribute("data-code","track_switcher career card · Mimo vector "+c.icon);
    b.innerHTML='<span class="badges"><span data-icon="'+c.icon+'" data-size="48"></span></span>'
      +'<h4'+v11Lab(c.label)+'>'+esc(c.label)+'</h4>'
      +'<span class="cr"><span data-fa="فصل">فصل</span><span>'+esc(c.sec)+'</span></span>'
      +'<span class="cbar"><i style="width:'+c.pct+'%"></i></span>';
    CC.appendChild(b);
  });
  /* 12 Courses = 4 subjects x 3 grades */
  var CR=q("#courseRows");CR.innerHTML="";
  V11_COURSES.forEach(function(c){
    var b=document.createElement("button");b.className="course-row";b.dataset.v11="course:"+c.key;
    b.setAttribute("data-code","section_details · "+c.chapters.length+" chapters");
    b.innerHTML='<span class="cbadge" data-icon="'+c.icon+'" data-size="38"></span>'
      +'<span class="ctxt"><b'+v11Lab(c.name)+'>'+esc(c.name)+'</b>'
      +'<small'+v11Lab(fa(c.chapters.length)+" فصل")+'>'+fa(c.chapters.length)+' فصل</small></span>'
      +'<span class="cring"><b>0/'+c.chapters.length+'</b></span>';
    CR.appendChild(b);
  });
  /* Path Overview: 10 fortnightly slots, or chapters + lessons for a course */
  function v11RenderOverview(){
    var course=V11_SEL.kind==="course"?v11Course(V11_SEL.key):null;
    var kick=course?KONKUR.topic_label:KONKUR.program_label;
    var title=course?course.name:(v11Program(V11_SEL.key)||V11_PROGRAMS[0]).label;
    q("#poKicker").textContent=kick;q("#poKicker").dataset.fa=kick;
    q("#poTitle").textContent=title;q("#poTitle").dataset.fa=title;
    var rows=[];
    if(course){
      course.chapters.forEach(function(ch,i){
        rows.push({ord:i+1,title:"فصل "+fa(i+1)+" · "+ch.name,
                   desc:KONKUR.lessons_label+": "+ch.lessons.join("، "),lessons:ch.lessons});
      });
    } else {
      V11_DATES.forEach(function(d,i){
        rows.push({ord:i+1,title:d,desc:V11_SUBJECT_LINE,lessons:V11_SUBJECTS});
      });
    }
    V11_ROWS=rows;
    var SR=q("#sectionRows");SR.innerHTML="";
    rows.forEach(function(r,i){
      var pct=i===0?43:0;
      var b=document.createElement("button");b.className="po-sec"+(i===0?" active":"");
      b.dataset.v11section=String(i);
      b.setAttribute("data-code","path_overview_section_ordinal · "+r.title);
      b.innerHTML='<span class="ring'+(pct?" part":"")+'"><b>'+pct+'%</b></span>'
        +'<span class="st"><b'+v11Lab(fa(r.ord)+". "+r.title)+'>'+esc(fa(r.ord)+". "+r.title)+'</b>'
        +'<p'+v11Lab(r.desc)+'>'+esc(r.desc)+'</p>'
        +(i===1?'<span class="proj" data-fa="پروژهٔ مبحث">پروژهٔ مبحث</span>':'')
        +(i===4?'<span class="soon" data-fa="بهزودی">بهزودی</span>':'')+'</span>';
      SR.appendChild(b);
    });
    paintIcons(SR);
    v11RenderSection(0);
    var lp=q("#learnPathTitle");if(lp){lp.textContent=title;lp.dataset.fa=title}
  }
  /* Section detail: «دروس» — subjects for programs, real lesson names for courses */
  function v11RenderSection(i){
    var r=V11_ROWS[i];if(!r)return;
    var kick=V11_SEL.kind==="course"?("فصل "+fa(i+1)):(fa(i+1)+" · "+V11_DATES[i]);
    q("#sdKicker").textContent=kick;q("#sdKicker").dataset.fa=kick;
    q("#sdTitle").textContent=r.title;q("#sdTitle").dataset.fa=r.title;
    q("#sdDesc").textContent=r.desc;q("#sdDesc").dataset.fa=r.desc;
    var LR=q("#lessonRows");LR.innerHTML="";
    r.lessons.forEach(function(name,j){
      var b=document.createElement("button");
      b.className="sd-row "+(j<2?"done":j===2?"cur":"");b.dataset.nav="chapter";
      var lab="درس "+fa(j+1)+" · "+name;
      b.innerHTML='<span class="sr" data-icon="'+(j<2?"ic_check_white":j===2?"ic_play":"ic_arrow_right")+'" data-size="18" data-mono="1"></span>'
        +'<span class="stx"><b'+v11Lab(lab)+'>'+esc(lab)+'</b>'
        +'<small'+v11Lab(r.title)+'>'+esc(r.title)+'</small></span>'
        +'<span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
      LR.appendChild(b);
    });
    var proj=document.createElement("button");proj.className="sd-row";proj.dataset.nav="chapter";
    proj.innerHTML='<span class="sr" data-icon="ic_cap" data-size="20"></span>'
      +'<span class="stx"><b data-fa="پروژهٔ مبحث">پروژهٔ مبحث</b>'
      +'<small data-fa="پروژهٔ پایانی مبحث">پروژهٔ پایانی مبحث</small></span>'
      +'<span class="si" data-icon="ic_arrow_right" data-size="18" data-mono="1"></span>';
    LR.appendChild(proj);
    paintIcons(LR);
  }
  v11RenderOverview();
  /* One delegated handler: cards switch the track, section rows open their own data */
  document.addEventListener("click",function(e){
    var c=e.target.closest("[data-v11]");
    if(c){
      var parts=c.dataset.v11.split(":");
      V11_SEL={kind:parts[0],key:parts[1]};
      qa("#careerCards .career-card").forEach(function(x){x.classList.remove("sel")});
      if(parts[0]==="program")c.classList.add("sel");
      v11RenderOverview();
      if(parts[0]==="program"||parts[0]==="course")go("path-overview");
      return;
    }
    var s=e.target.closest("[data-v11section]");
    if(s){v11RenderSection(+s.dataset.v11section);go("section-detail");return}
  });
  /* generic modal open/close (Unfinished track) */

  document.addEventListener("click",function(e){
    var m=e.target.closest("[data-modal]");if(m){var t=q("#"+m.dataset.modal);if(t)t.classList.add("on");return}
    var c=e.target.closest("[data-modal-close]");if(c){var t2=q("#"+c.dataset.modalClose);if(t2)t2.classList.remove("on");return}
  });
  paintIcons();
  var l6=q("#learnStats");
  if(l6)l6.innerHTML="<b>شواهد دور ششم:</b> "+LEARN.counts.strings+" رشتهٔ ARSC · "+LEARN.counts.vectors+" وکتور pathData · "+LEARN.counts.layouts+" لایهٔ AXML · "+CM.sections.length+" فصل واقعی · "+LEARN.counts.dex_classes+" کلاس DEX · "+LEARN.counts.catalog_rows+" ردیف کاتالوگ";


  /* ============ v7 · bolt nodes -> isolated section-practice checkpoint quiz ============ */
  var NS=NODE.strings, NCM=NODE.contentModel, PRACTICE_SECTION=3;
  /* v12.5-fa: نام فصلهای کنکوری جایگزین عنوانهای HTML/برنامهنویسی شد */
  var P_FA=["ساختار سلول و بافت","آنزیمها","اتم و ساختار الکترونی","حرکتشناسی","تابع و مشتق","ژنتیک و وراثت","تعادل شیمیایی","ترمودینامیک","گسلش و فشار","دستهبندی گیاهان"];
  var P_STEMS=[
    "کدام گزینه تعریف درست این مبحث را میدهد؟",
    "کدام نکته دربارهٔ درسهای تا این فصل صحیح است؟",
    "کدام حالت، نتیجهٔ درست تمرین قبل است؟"
  ];
  function practiceScope(n){
    var arr=NCM.sections.slice(0,n), ids=[];
    arr.forEach(function(s){ids=ids.concat(s.tutorialIds)});
    return {sections:arr,ids:ids};
  }
  function renderPractice(n){
    PRACTICE_SECTION=n;
    var sc=practiceScope(n), sec=NCM.sections[Math.min(n,NCM.sections.length)-1];
    q("#spTitle").textContent=P_FA[Math.min(n,P_FA.length)-1];
    q("#spScope").textContent="تا فصل "+fa(n)+" · "+fa(sc.ids.length)+" درس";
    var box=q("#practiceQuestions");box.innerHTML="";
    P_STEMS.forEach(function(stem,i){
      var d=document.createElement("div");d.className="sp-q";d.dataset.q=String(i);
      var sname=P_FA[i%P_FA.length];
      var tid=sc.ids[i%sc.ids.length]||0;
      var opts=[1,2,3,4].map(function(o){return '<button class="sp-opt" data-o="'+o+'">'+fa(o)+'</button>'}).join("");
      d.innerHTML='<div class="sp-stem"><b>'+fa(i+1)+'. '+esc(stem)+'</b><small>'+esc(sname)+' · شناسهٔ درس '+fa(tid)+'</small></div><div class="sp-opts">'+opts+'</div>';
      box.appendChild(d);
    });
    q("#practiceResult").innerHTML="";
    q("#practiceStart").textContent="شروع تمرین";
    q("#practiceModalTitle").textContent="شارژ کامل!";
    q("#practiceModalText").textContent="هر روز کمی تمرین کردن، مؤثرترین راه یادگیری است.";
    paintIcons(box);
  }
  q("#practiceStart").addEventListener("click",function(){
    var qs=qa("#practiceQuestions .sp-q"),answered=0,correct=0;
    qs.forEach(function(x,i){var s=q(".sp-opt.on",x);if(s){answered++;if(+s.dataset.o===(i%4)+1)correct++}});
    q("#practiceResult").innerHTML='<div class="sp-fb"><b>'+fa(answered)+' / '+fa(qs.length)+'</b> پاسخ ثبت شد · '+esc("ادامه بده، خوب پیش میروی")+'</div>';
    if(answered===qs.length){
      q("#practiceModalTitle").textContent="همهٔ تمرینها تمام شد!";
      q("#practiceModalText").textContent="این مبحث را بهطور کامل تمرین کردهاید.";
      q("#practiceModal").classList.add("on");
      toast("همهٔ تمرینهای این مبحث انجام شد");
    }else toast("چند سؤال هنوز پاسخ ندادهاند");
  });

  /* ============ v8 · «روتین روزانه» و کل ایدهٔ Habitica حذف شد ============ */
  renderPractice(4);

  /* ============ v8 · current-node state (review chrome only, NOT app UI) ============ */
  function setCurState(mode){
    var box=q("#curInner");if(!box)return;
    if(mode==="play")box.innerHTML='<span data-icon="ic_play" data-size="46" data-mono="1"></span>';
    else box.innerHTML='<span class="hring"><b>1/2</b></span>';
    paintIcons(box);
  }
  var nh=q("#nodeHalfBtn"),nplay=q("#nodePlayBtn");
  if(nh)nh.addEventListener("click",function(){setCurState("half");toast("گرهٔ فعلی: حلقهٔ ½")});
  if(nplay)nplay.addEventListener("click",function(){setCurState("play");toast("گرهٔ فعلی: پلی")});

  /* ============ v8 · delegated interactions: bolt nodes / glossary / practice ============ */
  document.addEventListener("click",function(e){
    var b=e.target.closest("[data-practice]");
    if(b){
      var n=+b.dataset.practice;
      if(!n)return;
      renderPractice(n);
      toast("تمرین مبحث: تا فصل "+fa(n)+" (جدا از آزمون کنکور)");
      return;
    }
    var o=e.target.closest(".sp-opt");
    if(o){qa(".sp-opt",o.parentNode).forEach(function(x){x.classList.remove("on")});o.classList.add("on");return}
  });

  var n8=q("#nodeStats");
  if(n8)n8.innerHTML="<b>شواهد دور دهم (معماری اورجینال):</b> "+NODE.counts.vectors+" وکتور pathData · "+NODE.counts.strings+" رشتهٔ ARSC · "+NODE.counts.shapes+" شِیپ AXML · "+NODE.counts.pathmap_classes+" کلاس PathMap DEX · "+NODE.counts.sections+" فصل / "+NODE.counts.tutorial_ids+" شناسهٔ درس · "+NODE.counts.catalog_rows+" ردیف کاتالوگ گره · چیدمان "+NODE.nodeGeometry.layout.mode+" / قوسهای Q="+NODE.counts.curves+" / فاصله "+NODE.nodeGeometry.layout.node_gap_dp+"dp";
  /* ---- APP HOOKS (working copy only; protected prototype is untouched) ---- */
  window.PROTO={
    go:go,toast:toast,fa:fa,paintIcons:paintIcons,icon:icon,
    tabMap:tabMap,tabScreen:tabScreen,openExam:openExam,resumeExam:resumeExam,
    renderQuestion:renderQuestion,applyPolicy:applyPolicy,render:render,
    questions:QBANK,bankSize:QTOTAL,
    currentScreen:function(){var e=q(".screen.on");return e?e.dataset.screen:"learn"},
    getSaved:function(){return SAVED},
    setSaved:function(v){SAVED=v;var rb=q("#resumeBar");if(!rb)return;
      rb.hidden=!v;if(v){q("#resumeText").textContent="«"+v.exam+"» · سؤال "+fa(v.qi+1)+" ذخیره شد"}},
    examState:function(){return {exam:q("#examTitle").textContent,kind:EXAM_KIND,qi:QI,
      answers:Object.assign({},ANSWERS),checked:Object.assign({},CHECKED),
      marks:Object.assign({},MARKS),minutes:q("#timerMinutes").value,
      timer:{state:T.state,remaining:T.remaining,total:T.total},qt:QTOTAL}},
    practice:renderPractice
  };
  /* v8 · node positions re-applied at runtime from the injected code geometry */
  (function(){
    var G=NODE.nodeGeometry, vb=G.viewBox, sz=G.node.size_dp;
    G.nodes.forEach(function(n){
      var el=q("."+n.id);
      if(el){el.style.left=(n.cx/vb[0]*100)+"%";el.style.top=(n.cy-sz/2)+"px";}
    });
    var c=q(".pathwrap.l10 .connector");
    if(c)c.setAttribute("viewBox","0 0 "+vb[0]+" "+vb[1]);
  })();
  paintIcons();

  histRender();render();
})();
