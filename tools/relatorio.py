"""Generate a candidate CSV and PDF from agregar-tse.py output, without AI calls."""
from pathlib import Path
import argparse,csv,json,html
def run(args):
    data=json.loads(args.dados.read_text(encoding='utf8'));candidate=data['candidatos'].get(args.candidato)
    if not candidate:raise ValueError('Número de candidato ausente do recorte.')
    meta=data['meta'];total=data['totais'][args.candidato];rows=[]
    for place in data['locais']:
        v=place['votos'].get(args.candidato,0);n=place['total_nominal'];rows.append([place['bairro'],place['nome'],place['zona'],place['codigo_local'],v,n,v/n if n else 0])
    rows.sort(key=lambda r:-r[4]);assert sum(r[4] for r in rows)==total
    args.saida.parent.mkdir(parents=True,exist_ok=True);csv_path=args.saida.with_suffix('.csv')
    with csv_path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f,delimiter=';');w.writerow(['Bairro','Local de votação','Zona','Código local','Votos do candidato','Votos nominais','Participação']);w.writerows(rows)
    try:
        from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,LongTable,TableStyle
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
        from reportlab.lib.pagesizes import A4
    except ImportError:
        print(json.dumps({'csv':str(csv_path),'pdf':None,'instrucoes':'Instale requirements.txt e execute novamente para o PDF.'}));return
    styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=8,leading=10));P=lambda text:Paragraph(html.escape(str(text)),styles['Cell'])
    story=[Paragraph(html.escape(f"{meta['municipio']} — {candidate['nome']}"),styles['Title']),Paragraph(f"{meta['ano']} · {meta['turno']}º turno · Cargo {meta['cargo']} · Número {html.escape(args.candidato)}",styles['Normal']),Spacer(1,12),Paragraph(f"Votos: {total:,}".replace(',','.'),styles['Heading2']),Paragraph(html.escape(meta['metodologia']),styles['Normal']),Spacer(1,12)]
    body=[[P(x) for x in ['Bairro','Local de votação','Zona/local','Votos','% nominais']]]+[[P(r[0]),P(r[1]),P(f'{r[2]}/{r[3]}'),P(f'{r[4]:,}'.replace(',','.')),P(f'{r[6]*100:.1f}%'.replace('.',','))] for r in rows]
    table=LongTable(body,colWidths=[98,206,57,53,61],repeatRows=1,hAlign='LEFT');table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DCEDE2')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F3F6F2')]),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story.extend([table,Spacer(1,14),Paragraph('Fonte: '+html.escape(meta['fonte']),styles['Normal']),Paragraph('Locais: '+html.escape(meta['locais_fonte']),styles['Normal'])])
    pdf_path=args.saida.with_suffix('.pdf');SimpleDocTemplate(str(pdf_path),pagesize=A4,leftMargin=36,rightMargin=36,topMargin=36,bottomMargin=36,title=f"Relatório eleitoral — {meta['municipio']}").build(story)
    print(json.dumps({'csv':str(csv_path),'pdf':str(pdf_path),'votos':total,'locais':len(rows)},ensure_ascii=True))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--dados',type=Path,required=True);p.add_argument('--candidato',required=True);p.add_argument('--saida',type=Path,required=True);run(p.parse_args())
