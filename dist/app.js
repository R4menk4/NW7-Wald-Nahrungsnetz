'use strict';

const root=document.getElementById('app');
function heading(kicker,title,intro=''){return '<span class="eyebrow">'+kicker+'</span><h1 tabindex="-1">'+title+'</h1>'+(intro?'<p class="intro">'+intro+'</p>':'');}
function render(focus=false){
  const requested=location.hash.slice(1)||'nahrung-start';
  const route=requested==='start'?'nahrung-start':requested;
  if(!foodOrder.includes(route)){location.hash='nahrung-start';return;}
  if(foodOrder.indexOf(route)>1&&!networkComplete()){location.hash='nahrung-netz';return;}
  root.innerHTML=foodSteps(route)+foodPages[route]();
  if(focus){root.querySelector('h1')?.focus({preventScroll:true});window.scrollTo(0,0);}
}

window.addEventListener('hashchange',()=>render(true));
installFoodEvents();
render();
