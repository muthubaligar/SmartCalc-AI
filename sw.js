const CACHE='smartcalc-v1';
const CORE=['/','/manifest.webmanifest'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE))));
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(u.origin===location.origin&&e.request.method==='GET'){e.respondWith(caches.match(e.request).then(c=>c||fetch(e.request).then(r=>{let copy=r.clone();caches.open(CACHE).then(x=>x.put(e.request,copy));return r}).catch(()=>caches.match('/'))))}});
