const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const dir=process.argv[2],out=process.argv[3];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1664,height:700},deviceScaleFactor:1});
for(const f of fs.readdirSync(dir).filter(x=>x.endsWith('.html')).sort()){await p.goto('file://'+path.join(dir,f));await p.screenshot({path:path.join(out,f.replace('.html','.png'))});
const ov=await p.evaluate(()=>[...document.querySelectorAll('*')].filter(e=>{const r=e.getBoundingClientRect();return r.bottom>700||r.right>1664&&!e.classList.contains('ft')&&e.tagName!='BODY'&&e.tagName!='HTML'}).length);console.log(f,ov)}
await b.close()})();
