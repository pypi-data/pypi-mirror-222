(()=>{var e,r,t={1249:(e,r,t)=>{"use strict";var n=t(3578),o=t.n(n),a=t(7401);let i;var l;(l=i||(i={}))[l.init=0]="init",l[l.data=1]="data",l[l.idle=2]="idle";let s,c,u="",f="",p=0,d=0,y=0,b=1,v=255,g=2e8;function h(e,r){const t=function(e,r,t,n,o,a){if(!a)return;const i={Position:new Float32Array(3*a.X.length),Color:new Float32Array(4*a.X.length)};for(let l=0;l<a.X.length;++l)i.Position[3*l]=a.X[l]-e,i.Position[3*l+1]=(a.Z[l]-r)*n,i.Position[3*l+2]=a.Y[l]-t,i.Color[4*l]=a.Red[l]/o,i.Color[4*l+1]=a.Green[l]/o,i.Color[4*l+2]=a.Blue[l]/o,i.Color[4*l+3]=1;return i}(p,d,y,b,v,(e=>{if(e)return{X:new Float32Array(e.X),Y:new Float32Array(e.Y),Z:new Float32Array(e.Z),Red:new Uint16Array(e.Red),Green:new Uint16Array(e.Green),Blue:new Uint16Array(e.Blue)}})(r));self.postMessage({type:i.data,block:e,entries:t,name:self.name},[t?.Position.buffer,t?.Color.buffer])}self.onmessage=async e=>{const r=e.data;if(r.type===i.init){const e=r;u=e.namespace,f=e.groupName,s=e.arraySchema,p=e.translateX,d=e.translateY,y=e.translateZ,b=e.zScale,v=e.rgbMax,g=e.bufferSize;const t=new(o())({apiKey:e.token,...e.tiledbEnv?{basePath:e.tiledbEnv}:{}});c=t.query}r.type===i.data&&async function(e){const r=[[e.minPoint._x+p,e.maxPoint._x+p],[e.minPoint._z+y,e.maxPoint._z+y],[e.minPoint._y+d,e.maxPoint._y+d]],t={layout:a.Layout.Unordered,ranges:r,attributes:["X","Y","Z","Red","Green","Blue"],bufferSize:g,returnRawBuffers:!0};for await(const r of c.ReadQuery(u,f+"_"+e.lod,t,s))h(e,r);self.postMessage({type:i.idle,name:self.name,idle:!0})}(r.block)}},8291:()=>{},4447:()=>{}},n={};function o(e){var r=n[e];if(void 0!==r)return r.exports;var a=n[e]={exports:{}};return t[e].call(a.exports,a,a.exports,o),a.exports}o.m=t,o.c=n,o.x=()=>{var e=o.O(void 0,[578],(()=>o(1249)));return o.O(e)},e=[],o.O=(r,t,n,a)=>{if(!t){var i=1/0;for(u=0;u<e.length;u++){for(var[t,n,a]=e[u],l=!0,s=0;s<t.length;s++)(!1&a||i>=a)&&Object.keys(o.O).every((e=>o.O[e](t[s])))?t.splice(s--,1):(l=!1,a<i&&(i=a));if(l){e.splice(u--,1);var c=n();void 0!==c&&(r=c)}}return r}a=a||0;for(var u=e.length;u>0&&e[u-1][2]>a;u--)e[u]=e[u-1];e[u]=[t,n,a]},o.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return o.d(r,{a:r}),r},o.d=(e,r)=>{for(var t in r)o.o(r,t)&&!o.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},o.f={},o.e=e=>Promise.all(Object.keys(o.f).reduce(((r,t)=>(o.f[t](e,r),r)),[])),o.u=e=>e+".a5ae2bca7b53beb61f4d.js?v=a5ae2bca7b53beb61f4d",o.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),o.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),o.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{o.S={};var e={},r={};o.I=(t,n)=>{n||(n=[]);var a=r[t];if(a||(a=r[t]={}),!(n.indexOf(a)>=0)){if(n.push(a),e[t])return e[t];o.o(o.S,t)||(o.S[t]={}),o.S[t];var i=[];return e[t]=i.length?Promise.all(i).then((()=>e[t]=1)):1}}})(),(()=>{var e;o.g.importScripts&&(e=o.g.location+"");var r=o.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");if(t.length)for(var n=t.length-1;n>-1&&!e;)e=t[n--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),o.p=e})(),(()=>{var e={687:1,606:1,202:1};o.f.i=(r,t)=>{e[r]||importScripts(o.p+o.u(r))};var r=self.webpackChunk_tiledb_inc_pybabylonjs=self.webpackChunk_tiledb_inc_pybabylonjs||[],t=r.push.bind(r);r.push=r=>{var[n,a,i]=r;for(var l in a)o.o(a,l)&&(o.m[l]=a[l]);for(i&&i(o);n.length;)e[n.pop()]=1;t(r)}})(),r=o.x,o.x=()=>o.e(578).then(r),o.x()})();