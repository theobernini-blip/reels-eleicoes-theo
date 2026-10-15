import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const checks=[];
const run=(name,args)=>{const r=spawnSync(name,args,{encoding:'utf8',timeout:12000,windowsHide:true});return r.status===0?(r.stdout||r.stderr).trim().split('\n')[0]:null;};
checks.push({item:'Node.js >=22',ok:Number(process.versions.node.split('.')[0])>=22,value:process.version});
const npm=process.platform==='win32'?run('cmd.exe',['/d','/s','/c','npm --version']):run('npm',['--version']);
checks.push({item:'npm',ok:!!npm,value:npm||'Instale Node.js LTS com npm.'});
let python=null;for(const [bin,args] of process.platform==='win32'?[['py',['-3','--version']],['python',['--version']]]:[['python3',['--version']],['python',['--version']]]){python=run(bin,args);if(python)break;}
checks.push({item:'Python >=3.10 (dados)',ok:!!python&&/Python 3\.(?:1[0-9]|[2-9][0-9])\./.test(python),value:python||'Instale Python 3.10+.'});
checks.push({item:'Skill do projeto',ok:fs.existsSync(path.join(root,'.agents/skills/reels-eleicoes-theo/SKILL.md'))});
const localProfile=fs.existsSync(path.join(root,'config/perfil.local.json'));
checks.push({item:'Perfil próprio',ok:localProfile,optional:true,value:localProfile?'Configurado.':'Copie config/perfil.example.json para perfil.local.json e preencha seus dados.'});
const ffmpeg=run('ffmpeg',['-version']);checks.push({item:'FFmpeg externo (opcional)',ok:!!ffmpeg,optional:true,value:ffmpeg||'A CLI de vídeo pode usar seu runtime próprio; necessário só para operações diretas.'});
console.log(JSON.stringify({checks,note:'Este diagnóstico não faz login, gera voz, compra créditos ou ativa automações.'},null,2));
if(checks.some(c=>!c.ok&&!c.optional))process.exitCode=1;
