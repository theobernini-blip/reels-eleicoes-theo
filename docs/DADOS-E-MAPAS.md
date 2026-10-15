# Dados oficiais e mapas

Fontes: [Resultados TSE 2022](https://dadosabertos.tse.jus.br/dataset/resultados-2022), [Resultados TSE 2024](https://dadosabertos.tse.jus.br/dataset/resultados-2024), [Resultados TSE 2026](https://dadosabertos.tse.jus.br/dataset/resultados-2026). O cadastro de locais fica em `eleitorado-ANO` no mesmo portal. Para presidente, o arquivo BR reúne as UFs; arquivos estaduais cobrem os cargos estaduais. Confirmar no recurso selecionado.

Baixar **votação por seção** e **locais de votação do mesmo ano**. Para uma cidade:

```powershell
python tools/agregar-tse.py --votos dados-originais/votacao_secao_2024_MT.zip --locais dados-originais/eleitorado_local_votacao_2024_MT.csv --ano 2024 --turno 1 --cargo 13 --municipio 90670 --saida producoes/cuiaba-2024/dados
```

`municipio` é o código TSE, não o código IBGE; `cargo` deve ser conferido no arquivo. Nos exemplos atuais, 1 = presidente, 3 = governador, 5 = senador, 6 = deputado federal, 7 = deputado estadual, 11 = prefeito e 13 = vereador. Não selecionar pelo cargo escrito em uma tela antiga.

O comando gera `dados.json`, `escolas.csv`, `bairros.csv` e `auditoria.json`. Para confrontar todos os candidatos, forneça `--totais-esperados totais-oficiais.json`, um objeto com os números de todos os candidatos e seus votos, obtido de uma totalização oficial independente. Exemplo de formato: `{"22":100,"13":80}`. Sem essa segunda fonte, a auditoria diz que a conferência externa está pendente.

Para um relatório de candidato:

```powershell
python tools/relatorio.py --dados producoes/cuiaba-2024/dados/dados.json --candidato 22300 --saida producoes/cuiaba-2024/relatorio
```

Isso cria CSV e PDF quando ReportLab está instalado. Os números e o nome do candidato vêm do recorte, não do nome do arquivo.

## Geografia

Os mapas das referências estão congelados em arquivos locais. Para um novo município, obter a malha oficial no IBGE e registrar a fonte/ano. Os GeoJSONs de bairros incluídos são referências do Censo 2022. Um limite não representa automaticamente o bairro cadastrado no TSE; conferir nomes e pontos.

Na ausência de limites confiáveis, representar escolas com pinos nas coordenadas reais, como na referência Rondonópolis. Registrar o que ficou fora do enquadramento urbano e manter seus votos no relatório. Os bairros do relatório são agrupamentos por cadastro do local, não inferência do domicílio do eleitor.

Para trocar uma base de ruas, manter a projeção dos pinos e o `map-projection.json` coerentes. Não esticar a imagem ou mudar o enquadramento sem reprojetar o SVG. OpenStreetMap exige atribuição; use fornecedor e política de tiles apropriados para novos mapas. Não colocar screenshot de outra cidade sob os pontos.

Não atualizar apenas o texto da cidade, não inventar coordenadas e não colorir polígonos sem correspondência. Dados ausentes ficam identificados no relatório e neutros no mapa.
