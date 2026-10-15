# Sinop — proposta de Reel para aprovação

Data: 11/10/2026. Status: roteiro e edição aprovados; voz e prévia animada prontas. Render pendente de aprovação da animação.

## Ideia
Pergunta: Lula ganhou em algum bairro de Sinop? Revelação: Flávio liderou nos 41 locais de votação conferidos, e também nos 33 grupos de bairros/localidades do cadastro TSE. Lula teve 17.568 votos na cidade; isso não virou liderança em nenhum desses grupos. Evitar atribuir a todos os moradores o comportamento das urnas.

## Roteiro (aproximadamente 30–35 s; timing final depende da voz)
Você acha que o Lula ganhou em algum bairro de Sinop?
Ele teve mais de dezessete mil votos na cidade.
Mas olha o que acontece quando a gente abre o mapa.
No Jardim Imperial, Flávio passou dos oito mil votos.
No Jardim Primavera, passou dos seis mil.
E no Jardim América, Lula teve quinhentos e treze votos. Deu pra virar?
Não. Ali, Flávio teve exatamente o dobro: mil e vinte e seis.
E a resposta do começo? Nenhum.
Flávio ficou na frente nos quarenta e um locais de votação que eu conferi.
E onde você votou?
Comente SINOP para receber o relatório completo.
Manda pra alguém de Sinop conferir também.

## Edição
9:16, 1080×1920, 60 fps. Mesma identidade verde, creme e Agency/Body. Voz Paulo expressiva, ritmo rápido e natural. Mapa tipo recorte de Maps, ruas reais e SINOP reconhecível no centro. Movimento desde o primeiro quadro. Sem vinheta.
0–3s: pergunta grande e mapa em aproximação; não revelar o preenchimento completo.
3–7s: 17.568 em destaque; revelar marcadores e regiões progressivamente.
7–14s: focos suaves Jardim Imperial (8.104 × 1.804) e Jardim Primavera (6.267 × 1.233), barras rápidas.
14–21s: Jardim América (1.026 × 513), suspense curtíssimo e animação do dobro.
21–27s: retorno ao mapa, 41/41 locais com liderança Flávio; resposta NENHUM. Texto de apoio: locais de votação conferidos, presidente, primeiro turno de 2026.
27–35s: convite para consultar o próprio bairro, CTA COMENTE SINOP e compartilhar.
Zoom com contexto, contraste de áreas e relevo discreto nos marcadores; sem alterar fronteiras reais. Pontos das escolas sempre visíveis. Campos sem associação cartográfica não devem receber cor inventada.

## Dados conferidos
TSE município 89850, IBGE 5107909. 346 seções com votos, 41 locais, 33 grupos de bairros/localidades cadastrados. Cadastro e resultado por seção cruzados; nenhuma seção sem correspondência. Totais de cada candidato conferidos contra a totalização municipal já salva.
Flávio: 73.701 (76,66% dos 96.146 votos válidos oficiais). Lula: 17.568 (18,27%). Outros candidatos válidos: 4.877. Brancos 816; nulos totais 1.380, incluindo 6 votos nulos técnicos.
Não há liderança de Lula em nenhum dos 41 locais nem nos 33 grupos cadastrais.
Jardim Imperial 8.104 × 1.804; Jardim Primavera 6.267 × 1.233; Jardim América 1.026 × 513.
Dados em ../work/sinop-dados. IBGE: 21 polígonos, correspondência inicial com votos em 11 nomes; validar posições/geometrias antes de quadro e render. Cadastro TSE agrupa alguns nomes, como bairros I/II/III; não equivale automaticamente à malha IBGE.
Fontes: https://dadosabertos.tse.jus.br/dataset/resultados-2026 ; https://www.ibge.gov.br/cidades-e-estados/mt/sinop.html ; malha IBGE 2022 e base OpenStreetMap.

## Automação criada (desativada durante revisão)
Palavra SINOP, fluxo separado. Resposta pública avisando do direct, mensagem com botão de perfil e Já segui, verificação nativa instagramFollowBusinnes TRUE, entrega do PDF próprio de Sinop. Rejeição/fallback e relatório terminais. Ativar antes da publicação; não alterar MAPA, BAIRRO ou VG.

## Próximo passo
Assistir à prévia animada de 36,65 segundos. Renderizar somente depois da aprovação da animação. Fluxo SINOP criado no ChatFunnel, com PDF publicado na galeria e verificação de seguidor. Ativar antes da publicação do Reel.
