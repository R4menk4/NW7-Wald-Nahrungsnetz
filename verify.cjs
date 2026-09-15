const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const handlers={};
const root={innerHTML:'',addEventListener:(name,fn)=>handlers[name]=fn,querySelector:()=>null,querySelectorAll:()=>[]};
const ctx={document:{getElementById:()=>root},location:{hash:''},window:{addEventListener:()=>{},scrollTo:()=>{}},console,Math};
vm.createContext(ctx);
for(const file of ['dist/foodweb.js','dist/app.js'])vm.runInContext(fs.readFileSync(file,'utf8'),ctx);
const run=code=>vm.runInContext(code,ctx);

assert(root.innerHTML.includes('Wer frisst wen?'));
assert(!root.innerHTML.includes('Themenübersicht'));
assert(!root.innerHTML.includes('Arbeitsblatt öffnen'));
const index=fs.readFileSync('dist/index.html','utf8');
assert(index.includes('foodweb.js'));
assert(!index.includes('tree.js'));
assert(!index.includes('Ökosystem Wald · Lernprogramm'));

run("foodState.placements={};foodState.connections=new Set();foodState.placementChecked=false;foodState.networkChecked=false;location.hash='#nahrung-netz';render()");
assert.equal([...root.innerHTML.matchAll(/data-food-bank-card=/g)].length,8);
assert.equal([...root.innerHTML.matchAll(/data-food-slot=/g)].length,8);
assert(!root.innerHTML.includes('href="#nahrung-auswerten"'));
assert(root.innerHTML.includes('Zweitkonsumenten')&&root.innerHTML.includes('Erstkonsumenten')&&root.innerHTML.includes('Produzenten'));

run("foodState.placements={...defaultPlacements};foodState.placementChecked=true;foodState.connections=new Set(expectedFoodEdges);foodState.networkChecked=true;render()");
assert(run('networkComplete()'));
assert(root.innerHTML.includes('Nahrungsnetz stimmt'));
assert(root.innerHTML.includes('href="#nahrung-auswerten"'));
assert.equal([...root.innerHTML.matchAll(/class="food-arrow /g)].length,9);
assert(root.innerHTML.includes('orient="auto"')&&root.innerHTML.includes(' L '));

run("foodState.placements={'producer-1':'brombeere','producer-2':'eiche','first-1':'reh','first-2':'raupe','first-3':'waldmaus','second-1':'rotfuchs','second-2':'waldkauz','second-3':'buntspecht'}");
assert(run('placementsValid()'));
run("location.hash='#nahrung-netz';render()");
assert.equal([...root.innerHTML.matchAll(/class="food-arrow /g)].length,9);
run("foodState.placements['producer-1']='reh'");
assert(!run('placementsValid()'));

run("foodState.placements={...defaultPlacements};foodState.placementChecked=true;foodState.connections=new Set(expectedFoodEdges);foodState.networkChecked=true");
for(const route of run('foodOrder')){
  run("location.hash='#"+route+"';render()");
  assert(root.innerHTML.includes('<h1'));
  for(const match of root.innerHTML.matchAll(/src="(assets\/[^"]+)"/g))assert(fs.existsSync('dist/'+match[1]),match[1]);
}
run("location.hash='#nahrung-auswerten';render()");
assert(root.innerHTML.includes('network-recap')&&root.innerHTML.includes('Dein Nahrungsnetz'));
run("foodState.whyOrder=null;location.hash='#nahrung-erklaeren';render()");
const whyOrder=run('foodState.whyOrder.join()');run('render()');assert.equal(run('foodState.whyOrder.join()'),whyOrder);assert.equal(run('new Set(foodState.whyOrder).size'),4);
run("foodState.consequenceOrder=null;location.hash='#nahrung-folgen';render()");
const consequenceOrder=run('foodState.consequenceOrder.join()');run('render()');assert.equal(run('foodState.consequenceOrder.join()'),consequenceOrder);assert.equal(run('new Set(foodState.consequenceOrder).size'),4);
run("location.hash='#nahrung-abschluss';render()");
assert(!root.innerHTML.includes('Arbeitsblatt noch einmal öffnen'));
console.log('PASS: standalone food-web program, placement, arrows, gating, recap, shuffled answers and assets.');
