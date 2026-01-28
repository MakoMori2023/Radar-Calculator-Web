const CACHE_NAME = 'radar-calculator-v1';
const CACHE_ASSETS = [
    './index.html',
    './manifest.json'
    './Data/icon-512.png'
    './Data/icon-192.png'
];

// 安装阶段：缓存静态资源
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('缓存已打开');
                return cache.addAll(CACHE_ASSETS);
            })
    );
});

// 激活阶段：清理旧缓存
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.filter(cacheName => cacheName !== CACHE_NAME)
                    .map(oldCache => caches.delete(oldCache))
            );
        })
    );
});

// 拦截请求：优先使用缓存，无缓存则请求网络
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // 缓存命中则返回缓存，否则请求网络
                return response || fetch(event.request);
            })
    );
});