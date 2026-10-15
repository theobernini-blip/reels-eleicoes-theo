"""Aggregate official section votes using same-year polling-place metadata."""
from pathlib import Path
from collections import defaultdict,Counter
import argparse,csv,io,json,zipfile,re,hashlib,contextlib
def integer(v):
    try:return int(v)
    except (ValueError,TypeError):return 0
def clean(v):return re.sub(r'\s+',' ',str(v or '')).strip()
def coordinate(v):
    try:
        n=float(str(v).replace(',','.'));return n if n not in [-1,0] and -180<=n<=180 else None
    except (ValueError,TypeError):return None
@contextlib.contextmanager
def rows(path):
    if path.suffix.lower()=='.zip':
        with zipfile.ZipFile(path) as z:
            names=[n for n in z.namelist() if n.lower().endswith('.csv')]
            if len(names)!=1:raise ValueError('Escolha um ZIP com um CSV ou extraia o CSV correto antes de executar.')
            with z.open(names[0]) as raw:yield csv.DictReader(io.TextIOWrapper(raw,encoding='latin1'),delimiter=';')
    else:
        with path.open(encoding='latin1',newline='') as f:yield csv.DictReader(f,delimiter=';')
def write_json(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf8')
def run(args):
    places={};sections_to_local={};city_name='';selected_places=0
    with rows(args.locais) as reader:
        for r in reader:
            if integer(r.get('AA_ELEICAO'))!=args.ano or integer(r.get('NR_TURNO'))!=args.turno or str(integer(r.get('CD_MUNICIPIO')))!=args.municipio or r.get('SG_UF')!=args.uf:continue
            zone=integer(r['NR_ZONA']);section=integer(r['NR_SECAO']);local=integer(r['NR_LOCAL_VOTACAO']);pid=f'{zone}-{local}'
            key=(zone,section)
            if key in sections_to_local and sections_to_local[key]!=pid:raise ValueError(f'Seção com locais conflitantes: {key}')
            sections_to_local[key]=pid;city_name=clean(r['NM_MUNICIPIO']);neighborhood=clean(r.get('NM_BAIRRO'))
            places.setdefault(pid,{'id':pid,'zona':zone,'codigo_local':local,'nome':clean(r['NM_LOCAL_VOTACAO']),'bairro':neighborhood if neighborhood not in ['','#NULO#','#NE#'] else 'Bairro não informado','endereco':clean(r.get('DS_ENDERECO')),'latitude':coordinate(r.get('NR_LATITUDE')),'longitude':coordinate(r.get('NR_LONGITUDE'))})
            selected_places+=1
    if not selected_places:raise ValueError('Nenhum local encontrado. Confira o ano, turno, UF, código TSE e CSV utilizado.')
    local_votes=defaultdict(Counter);special=Counter();candidates={};seen=set();sections=defaultdict(set);dates=set();missing=set();moved=set()
    with rows(args.votos) as reader:
        required={'ANO_ELEICAO','SG_UF','CD_MUNICIPIO','NR_TURNO','CD_CARGO','SQ_CANDIDATO','NR_VOTAVEL','QT_VOTOS','NR_LOCAL_VOTACAO'}
        if not required.issubset(reader.fieldnames or []):raise ValueError('Layout não reconhecido: use o CSV oficial atualizado de votação por seção, com SQ_CANDIDATO.')
        for r in reader:
            if r['SG_UF']!=args.uf or integer(r['ANO_ELEICAO'])!=args.ano or integer(r['NR_TURNO'])!=args.turno or integer(r['CD_CARGO'])!=args.cargo or str(integer(r['CD_MUNICIPIO']))!=args.municipio:continue
            if 'CD_TIPO_ELEICAO' in r and integer(r['CD_TIPO_ELEICAO'])!=2:continue
            zone=integer(r['NR_ZONA']);section=integer(r['NR_SECAO']);local=integer(r['NR_LOCAL_VOTACAO']);pid=f'{zone}-{local}';number=r['NR_VOTAVEL'];sq=integer(r['SQ_CANDIDATO']);amount=integer(r['QT_VOTOS'])
            key=(zone,section,local,number,sq)
            if key in seen:raise ValueError(f'Linha duplicada na votação: {key}')
            seen.add(key);sections[pid].add(section);dates.add(r.get('DT_GERACAO',''));city_name=city_name or clean(r['NM_MUNICIPIO'])
            if (zone,section) not in sections_to_local:missing.add((zone,section))
            elif sections_to_local[(zone,section)]!=pid:moved.add((zone,section))
            if pid not in places:places[pid]={'id':pid,'zona':zone,'codigo_local':local,'nome':clean(r.get('NM_LOCAL_VOTACAO')) or 'Local '+str(local),'bairro':'Bairro não informado','endereco':clean(r.get('DS_LOCAL_VOTACAO_ENDERECO')),'latitude':None,'longitude':None}
            if sq<=0:special[number]+=amount;continue
            if number in candidates and candidates[number]['id_tse']!=str(sq):raise ValueError('Mais de um candidato com o mesmo número no recorte; confira a eleição e a totalização.')
            candidates.setdefault(number,{'numero':number,'nome':clean(r['NM_VOTAVEL']),'id_tse':str(sq)})
            local_votes[pid][number]+=amount
    if not candidates:raise ValueError('Nenhum voto nominal encontrado para o filtro.')
    totals=sum(local_votes.values(),Counter());neighborhoods=defaultdict(Counter)
    final_places=[]
    for pid in sorted(sections):
        p=dict(places[pid],secoes=len(sections[pid]),votos=dict(local_votes[pid]),total_nominal=sum(local_votes[pid].values()));final_places.append(p);neighborhoods[p['bairro']].update(local_votes[pid])
    meta={'ano':args.ano,'turno':args.turno,'cargo':args.cargo,'municipio_tse':args.municipio,'municipio':city_name,'uf':args.uf,'fonte':f'https://dadosabertos.tse.jus.br/dataset/resultados-{args.ano}','locais_fonte':f'https://dadosabertos.tse.jus.br/dataset/eleitorado-{args.ano}','geracao_tse':sorted(dates),'metodologia':'Votos das seções nos locais cadastrados em cada bairro; não representa o voto residencial de todos os moradores. Percentuais calculados entre os votos nominais do mesmo cargo e recorte.'}
    external=False
    if args.totais_esperados:
        expected={str(k):int(v) for k,v in json.loads(args.totais_esperados.read_text(encoding='utf8')).items()}
        if totals!=Counter(expected):raise ValueError('Totais por candidato divergentes da fonte independente. Corrigir antes de produzir o vídeo.')
        external=True
    output={'meta':meta,'candidatos':candidates,'totais':dict(totals),'total_nominal':sum(totals.values()),'votos_especiais':dict(special),'locais':final_places,'bairros':[{'bairro':name,'votos':dict(v),'total_nominal':sum(v.values())} for name,v in sorted(neighborhoods.items())]}
    audit={'totalizacao_externa_conferida':external,'status':'Totais independentes conferidos.' if external else 'Conferência externa pendente: forneça os totais oficiais por candidato.','secoes':len(set((p['zona'],s) for p in final_places for s in sections[p['id']])),'locais':len(final_places),'bairros':len(neighborhoods),'secoes_sem_cadastro':sorted(missing),'secoes_com_local_alterado':sorted(moved),'locais_sem_bairro':[p['id'] for p in final_places if p['bairro']=='Bairro não informado'],'locais_sem_coordenada':[p['id'] for p in final_places if p['latitude'] is None or p['longitude'] is None],'arquivos':[{'arquivo':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [args.votos,args.locais]]}
    args.saida.mkdir(parents=True,exist_ok=True);write_json(args.saida/'dados.json',output);write_json(args.saida/'auditoria.json',audit)
    for filename,items in [('escolas.csv',final_places),('bairros.csv',output['bairros'])]:
        with (args.saida/filename).open('w',encoding='utf-8-sig',newline='') as f:
            writer=csv.writer(f,delimiter=';');writer.writerow(['Ano','Turno','Cargo','Município','Bairro','Local','Número','Candidato','Votos','Total nominal','Participação'])
            for item in items:
                for number,candidate in candidates.items():
                    v=item['votos'].get(number,0);total=item['total_nominal'];writer.writerow([args.ano,args.turno,args.cargo,city_name,item['bairro'],item.get('nome',''),number,candidate['nome'],v,total,v/total if total else 0])
    print(json.dumps({'nominais':sum(totals.values()),'candidatos':len(candidates),'locais':len(final_places),'conferencia_externa':external,'saida':str(args.saida)},ensure_ascii=True))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--votos',type=Path,required=True);p.add_argument('--locais',type=Path,required=True);p.add_argument('--ano',type=int,required=True);p.add_argument('--turno',type=int,choices=[1,2],required=True);p.add_argument('--cargo',type=int,required=True);p.add_argument('--municipio',required=True);p.add_argument('--uf',default='MT');p.add_argument('--saida',type=Path,required=True);p.add_argument('--totais-esperados',type=Path);run(p.parse_args())
