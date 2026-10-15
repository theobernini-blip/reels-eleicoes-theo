"""Audit the exact public payload; do not include local productions or account files."""
from pathlib import Path
import json,re,hashlib,wave
ROOT=Path(__file__).resolve().parents[1]
SKIP={'.git','node_modules','producoes','entregas','__pycache__'}
EXT={'.html','.css','.js','.mjs','.json','.geojson','.md','.txt','.py','.yml','.yaml','.svg','.ttf','.wav','.webp','.png','.jpg','.jpeg',''}
TEXT={'.html','.css','.js','.mjs','.json','.geojson','.md','.txt','.py','.yml','.yaml','.svg',''}
PATTERNS=[('credential',r'\b(?:mcp_live_|github_pat_|ghp_|sb_secret_|sk_live_)[A-Za-z0-9_\-]{16,}\b'),('private_key',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),('personal_path',r'[A-Z]:[\\/]+Users[\\/][^\s"\'<>]+'),('jwt',r'\beyJ[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{12,}\b'),('sensitive_record_field',r'"(?:NR_CPF_CANDIDATO|NR_TITULO_ELEITORAL_CANDIDATO|access_token|refresh_token|service_role_key|password|senha)"\s*:\s*"[^"\n]+"')]
fonts={hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'projetos/reel-campo-novo-bairros-2026/assets/fonts').glob('*.ttf')}
generated_audio={hashlib.sha256((ROOT/'projetos/reel-campo-novo-bairros-2026/assets'/n).read_bytes()).hexdigest() for n in ['click.wav','whoosh.wav']}
manifest=[];findings=[];audio_counts={'silence':0,'synthesized_sfx':0,'other':0};raster=[]
for file in sorted(ROOT.rglob('*')):
    relative=file.relative_to(ROOT)
    if not file.is_file() or any(part in SKIP for part in relative.parts) or file.name=='auditoria-publicacao.json':continue
    if file.is_symlink():findings.append([str(relative),'symlink']);continue
    if file.name.endswith('.local.json') or file.name.startswith('.env'):findings.append([str(relative),'local_account_file'])
    data=file.read_bytes();sha=hashlib.sha256(data).hexdigest();kind='source_or_documentation';suffix=file.suffix.lower()
    if suffix not in EXT:findings.append([str(relative),'unknown_extension'])
    if suffix in TEXT:
        text=data.decode('utf-8-sig')
        for label,pattern in PATTERNS:
            if re.search(pattern,text,re.I):findings.append([str(relative),label])
        if suffix in ['.json','.geojson']:
            try:json.loads(text)
            except json.JSONDecodeError:findings.append([str(relative),'invalid_json'])
        if str(relative).startswith('dados'):kind='public_aggregated_tse_ibge_data'
        if suffix=='.svg':kind='generated_vector_or_public_geography'
        if file.name=='gsap.min.js':kind='gsap_with_original_license_header'
    elif suffix=='.ttf':
        kind='google_fonts_ofl'
        if sha not in fonts:findings.append([str(relative),'unrecognized_font'])
    elif suffix=='.wav':
        with wave.open(str(file),'rb') as f:frames=f.readframes(f.getnframes())
        if file.name=='narracao-placeholder.wav' and not any(frames):kind='generated_silence';audio_counts['silence']+=1
        elif sha in generated_audio:kind='original_synthesized_sfx';audio_counts['synthesized_sfx']+=1
        else:kind='unrecognized_audio';audio_counts['other']+=1;findings.append([str(relative),'unrecognized_audio'])
    elif suffix in ['.webp','.png','.jpg','.jpeg']:
        kind='frozen_public_map_or_generated_report_cover';raster.append(str(relative).replace('\\','/'))
        if not(file.name.startswith('base-osm') or 'capa' in file.name):findings.append([str(relative),'raster_needs_manual_review'])
    manifest.append({'file':str(relative).replace('\\','/'),'bytes':len(data),'sha256':sha,'classification':kind})
report={'scope':'Public GitHub production kit requested by owner; no accounts or original narration recordings.','files':len(manifest),'total_bytes':sum(m['bytes'] for m in manifest),'findings':findings,'audio':audio_counts,'raster_assets':raster,'sources':{'data':'https://dadosabertos.tse.jus.br/','boundaries':'https://www.ibge.gov.br/geociencias/','maps':'https://www.openstreetmap.org/copyright','fonts':'https://github.com/google/fonts','animation':'https://gsap.com/standard-license/'},'license_files':['licencas/barlow-OFL.txt','licencas/barlowcondensed-OFL.txt'],'manifest':manifest}
(ROOT/'auditoria-publicacao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:report[k] for k in ['files','total_bytes','findings','audio','raster_assets']},ensure_ascii=True,indent=2))
if findings:raise SystemExit(1)
