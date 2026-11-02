// Génère les illustrations du site (WebP), l'image de partage (JPG) et les icônes (PNG)
// à partir de SVG dessinés à la main. Aucune photo : uniquement des illustrations.
// Usage : node src/images.mjs   (Chromium + Playwright requis)
import { createRequire } from 'node:module';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const { chromium } = createRequire(import.meta.url)('playwright');
const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', 'public');
const R = '#B3121F', Y = '#F2B705', C = '#FBF8F1', D = '#1F1A17', W = '#FFFFFF';

// Clé blanche (réutilisée par le logo)
const key = (fill = W) => `
  <circle cx="22" cy="32" r="9" fill="none" stroke="${fill}" stroke-width="5"/>
  <rect x="29" y="29.5" width="24" height="5" rx="1.5" fill="${fill}"/>
  <rect x="43" y="33" width="4.5" height="8" rx="1" fill="${fill}"/>
  <rect x="49" y="33" width="4.5" height="6" rx="1" fill="${fill}"/>`;

export const LOGO_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="32" height="64" fill="${Y}"/><rect x="32" width="32" height="64" fill="${R}"/>${key()}</svg>`;

const bigKey = (x, y, s, rot, fill) => `
  <g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})">
    <circle cx="0" cy="0" r="30" fill="none" stroke="${fill}" stroke-width="16"/>
    <rect x="26" y="-8" width="120" height="16" rx="4" fill="${fill}"/>
    <rect x="104" y="6" width="14" height="26" rx="3" fill="${fill}"/>
    <rect x="126" y="6" width="14" height="18" rx="3" fill="${fill}"/>
  </g>`;

const door = (x, y, w, h) => `
  <rect x="${x - 14}" y="${y - 14}" width="${w + 28}" height="${h + 14}" rx="6" fill="${D}"/>
  <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="3" fill="${R}"/>
  <rect x="${x + 24}" y="${y + 26}" width="${w - 48}" height="${h * 0.36}" rx="4" fill="#9c0f1a"/>
  <rect x="${x + 24}" y="${y + 50 + h * 0.36}" width="${w - 48}" height="${h * 0.36}" rx="4" fill="#9c0f1a"/>`;

const handle = (x, y) => `
  <rect x="${x}" y="${y}" width="22" height="88" rx="11" fill="${C}"/>
  <rect x="${x - 34}" y="${y + 14}" width="48" height="13" rx="6.5" fill="${C}"/>
  <circle cx="${x + 11}" cy="${y + 56}" r="6" fill="${D}"/>
  <rect x="${x + 8.5}" y="${y + 58}" width="5" height="14" rx="2" fill="${D}"/>`;

const svgs = {
  'hero-porte': [640, 560, `
    <rect width="640" height="560" fill="${D}"/>
    <circle cx="330" cy="290" r="250" fill="${Y}"/>
    ${door(205, 70, 250, 440)}
    ${handle(400, 270)}
    ${bigKey(150, 420, 1.15, -28, C)}
    <circle cx="540" cy="110" r="14" fill="${R}"/><circle cx="90" cy="150" r="8" fill="${Y}"/>`],

  'service-ouverture': [480, 360, `
    <rect width="480" height="360" fill="${C}"/>
    <rect x="150" y="40" width="190" height="300" fill="${D}"/>
    <rect x="160" y="50" width="170" height="290" fill="${Y}"/>
    <polygon points="160,50 270,80 270,330 160,340" fill="${R}"/>
    <circle cx="250" cy="200" r="9" fill="${C}"/>
    <rect x="0" y="338" width="480" height="22" fill="#e8e1d3"/>
    ${bigKey(370, 120, 0.55, 35, R)}`],

  'service-serrure': [480, 360, `
    <rect width="480" height="360" fill="${C}"/>
    <g transform="translate(170 60)">
      <circle cx="70" cy="70" r="66" fill="${D}"/>
      <rect x="40" y="70" width="60" height="170" rx="10" fill="${D}"/>
      <circle cx="70" cy="70" r="48" fill="${Y}"/>
      <rect x="62" y="40" width="16" height="60" rx="5" fill="${D}"/>
      <circle cx="70" cy="200" r="18" fill="${Y}"/>
    </g>
    ${bigKey(70, 280, 0.6, -10, R)}`],

  'service-blindage': [480, 360, `
    <rect width="480" height="360" fill="${C}"/>
    <path d="M240 30 L370 80 V170 C370 250 310 305 240 330 C170 305 110 250 110 170 V80 Z" fill="${R}"/>
    <path d="M240 30 L240 330 C170 305 110 250 110 170 V80 Z" fill="${Y}"/>
    <circle cx="240" cy="160" r="26" fill="${D}"/>
    <path d="M228 172 h24 l8 60 h-40 z" fill="${D}"/>`],

  'service-effraction': [480, 360, `
    <rect width="480" height="360" fill="${C}"/>
    ${door(150, 50, 180, 300)}
    <polyline points="330,120 290,150 315,175 270,205 300,232 262,262" fill="none" stroke="${Y}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
    <rect x="96" y="170" width="290" height="26" rx="6" fill="${D}" transform="rotate(-12 240 183)"/>
    <circle cx="410" cy="70" r="30" fill="${Y}"/><rect x="405" y="50" width="10" height="26" rx="4" fill="${D}"/><circle cx="410" cy="86" r="5" fill="${D}"/>`],

  'og-image': [1200, 630, `
    <rect width="1200" height="630" fill="${D}"/>
    <rect x="0" y="0" width="1200" height="14" fill="${R}"/>
    <g transform="translate(80 120) scale(3)">${LOGO_SVG.replace(/<\/?svg[^>]*>/g, '')}</g>
    <text x="80" y="400" fill="${C}" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="76">Serrurier Genève 7j/7</text>
    <text x="80" y="470" fill="${Y}" font-family="Arial, sans-serif" font-weight="700" font-size="40">Clé en Main Genève · +41 79 942 95 44</text>
    <text x="80" y="530" fill="${C}" font-family="Arial, sans-serif" font-size="32">Devis gratuit par téléphone avant intervention</text>
    ${bigKey(980, 230, 1.4, -30, Y)}`],
};

const icons = { 'logo-512': 512, 'apple-touch-icon': 180, 'icon-192': 192 };

const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent('<canvas id="c"></canvas>');

async function render(svg, w, h, type, quality) {
  return page.evaluate(async ({ svg, w, h, type, quality }) => {
    const img = new Image();
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    await img.decode();
    const c = document.getElementById('c');
    c.width = w; c.height = h;
    const ctx = c.getContext('2d');
    ctx.clearRect(0, 0, w, h);
    ctx.drawImage(img, 0, 0, w, h);
    return c.toDataURL(type, quality).split(',')[1];
  }, { svg, w, h, type, quality });
}

function save(rel, b64) {
  const p = join(ROOT, rel);
  mkdirSync(dirname(p), { recursive: true });
  writeFileSync(p, Buffer.from(b64, 'base64'));
  console.log('écrit', rel);
}

for (const [name, [w, h, body]] of Object.entries(svgs)) {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${body}</svg>`;
  if (name === 'og-image') save('img/og-image.jpg', await render(svg, w, h, 'image/jpeg', 0.85));
  else save(`img/${name}.webp`, await render(svg, w, h, 'image/webp', 0.82));
}
for (const [name, size] of Object.entries(icons)) {
  const svg = LOGO_SVG.replace('<svg ', `<svg width="${size}" height="${size}" `);
  save(`img/${name}.png`, await render(svg, size, size, 'image/png'));
}
writeFileSync(join(ROOT, 'favicon.svg'), LOGO_SVG);
console.log('écrit favicon.svg');
await browser.close();
