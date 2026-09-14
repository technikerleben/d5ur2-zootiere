import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {dirname,resolve} from 'node:path';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const data=JSON.parse(readFileSync(resolve(root,'materialien/schritt3_inhalte.json'),'utf8'));
function renderPack(a){
const esc=s=>String(s).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");
return `<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(a.name)} · Tiermaterial · Deutsch 5.3</title><link rel="stylesheet" href="../schritt3.css"></head><body>
<nav class="toolbar" aria-label="Materialnavigation"><a href="../../index.html#tiermaterial">Zum Cockpit</a><button id="reading" aria-pressed="false">Vorschau der Lesehilfe</button><a href="${a.id}_A5.pdf">A5-Schüler-PDF öffnen</a></nav>
<p class="screen-note">${esc(a.role)} · Nur Lehrkraft-Vorschau. Schülerausgabe: fertiges A5-PDF mit mindestens 14 pt und eingebettetem Foto. Keine Nutzung dieser Webseite durch Lernende.</p>
<main class="sheet"><header><p class="eyebrow">DEUTSCH 5.3 · ZOOTIERE · MATERIAL</p><h1>${esc(a.name)}</h1><p class="latin">${esc(a.latin)}</p></header>
<figure><img id="animalphoto" src="${a.image}" alt="Foto: ${esc(a.name)}" referrerpolicy="no-referrer"><figcaption>Foto: ${esc(a.author)} · <a href="${a.imagePage}">Bildquelle</a> · <a href="${a.licenseUrl}">${a.license}</a> · unverändert, verkleinert angezeigt.</figcaption></figure>
<p class="loadstatus screen-note" id="image-status" role="status">Bild wird geladen.</p>
<section><h2>Informationen zum Tier</h2><p class="animaltext">${a.sentences.map(s=>`<span class="sentence">${esc(s)} </span>`).join("")}</p></section>
<aside class="words"><h2>Wörterhilfe</h2><dl>${a.glossary.map(([w,t])=>`<dt>${esc(w)}</dt><dd>${esc(t)}</dd>`).join("")}</dl></aside>
<section class="task"><h2>Nutze das Material</h2><p>Schau genau hin. Lies den Text. Zeige ein Merkmal, das du auf dem Foto erkennst. Zeige eine weitere Information im Text. Notiere passende Stichwörter im Heft.</p><p><strong>Für deine Beschreibung:</strong> Tiername, mindestens vier äußere Merkmale, eine Größen- oder Gewichtsangabe, Lebensraum und Nahrung. Nutze deinen Schreibplan und die Checkliste.</p></section>
<footer><p>Text: neu formulierte, gekürzte Unterrichtsfassung. Quellen: ${a.sources.map(([name,url])=>`<a href="${url}">${esc(name)}</a>`).join(" · ")}. Abruf: 14.09.2026.</p><p class="license-print">Bildnachweis: ${esc(a.author)} · ${a.license}${a.license.startsWith("CC")?" · "+a.licenseUrl:""}.</p></footer></main>
<script>
const img=document.getElementById('animalphoto'), status=document.getElementById('image-status');
function ready(){status.textContent=img.naturalWidth?'Foto geladen.':'Foto konnte nicht geladen werden. Öffne die Bildquelle und prüfe deine Internetverbindung.';}
img.addEventListener('load',ready);img.addEventListener('error',ready);if(img.complete)ready();
document.getElementById('reading').addEventListener('click',function(){const on=document.body.classList.toggle('reading-help');this.setAttribute('aria-pressed',String(on));this.textContent=on?'Lesehilfe ausschalten':'Vorschau der Lesehilfe';});

</script></body></html>`;
}
mkdirSync(resolve(root,'materialien/tierpakete'),{recursive:true});
for(const animal of data.animals){writeFileSync(resolve(root,'materialien/tierpakete',animal.id+'.html'),renderPack(animal),'utf8');}
console.log('Fünf Tierseiten erstellt. CSS, Checkliste und Bewertungsraster separat mitpflegen.');
