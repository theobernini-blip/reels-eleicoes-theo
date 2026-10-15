import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const walk=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(d=>(d.name.startsWith('.')&&!['.agents','.github'].includes(d.name))||['node_modules','producoes','entregas'].includes(d.name)?[]:d.isDirectory()?walk(path.join(dir,d.name)):[path.join(dir,d.name)]);
const errors=[],catalog=JSON.parse(fs.readFileSync(path.join(root,'catalogo-projetos.json'),'utf8'));let checked=0;
const checkText=(file,text)=>{
 const relative=path.relative(root,file);
 const patterns=[['caminho pessoal',/[A-Z]:[\\/]+Users[\\/][^\s"'<>]+/i],['token de serviço',/\b(?:mcp_live_|github_pat_|ghp_|sb_secret_|sk_live_)[A-Za-z0-9_\-]{16,}\b/],['chave privada',/-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/],['JWT literal',/\beyJ[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{12,}\b/]];
 for(const [label,pattern]of patterns)if(pattern.test(text))errors.push(`${relative}: ${label}`);
};
for(const p of catalog){const dir=path.join(root,p.path);for(const required of ['index.html','package.json','hyperframes.json','meta.json'])if(!fs.existsSync(path.join(dir,required)))errors.push(`${p.id}: falta ${required}`);
 for(const file of walk(dir)){checked++;if(fs.statSync(file).size>=95*1024*1024)errors.push(`${p.id}: arquivo grande demais para GitHub`);if(!/\.(html|css|js|json|svg|md)$/.test(file))continue;const text=fs.readFileSync(file,'utf8');checkText(file,text);if(!/\.(html|css)$/.test(file))continue;
  const refs=[...text.matchAll(/(?:\b(?:src|href|data-composition-src)=["']([^"']+)["']|url\(["']?([^"')]+)["']?\))/g)].map(m=>m[1]||m[2]);
  for(let ref of refs){if(!ref||/^(?:https?:|data:|#|mailto:|javascript:)/i.test(ref))continue;ref=decodeURIComponent(ref.split(/[?#]/)[0]);if(!ref)continue;const relative=path.resolve(path.dirname(file),ref),projectRelative=path.resolve(dir,ref);if(!fs.existsSync(relative)&&!fs.existsSync(projectRelative))errors.push(`${path.relative(root,file)}: referência ausente ${ref}`);}
 }
}
for(const file of walk(root)){if(/\.(md|mjs|py|json|txt|yml)$/.test(file)&&!file.includes(path.sep+'projetos'+path.sep))checkText(file,fs.readFileSync(file,'utf8'));}
for(const file of ['.agents/skills/reels-eleicoes-theo/SKILL.md','.agents/skills/reels-eleicoes-theo/references/editorial.md','config/perfil.example.json'])if(!fs.existsSync(path.join(root,file)))errors.push(`Falta ${file}`);
console.log(JSON.stringify({projects:catalog.length,projectFiles:checked,errors},null,2));if(errors.length)process.exitCode=1;
