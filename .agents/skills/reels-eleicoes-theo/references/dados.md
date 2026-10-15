# Dados e mapas

Fontes primárias: TSE para votação por seção e cadastro de locais, IBGE para limites e OpenStreetMap para ruas com atribuição. Identificar eleição, cargo, turno e município pelo conteúdo da fonte; não copiar códigos de outra eleição.

Cruzar município, zona e seção/local no ano correto. Somar todas as seções por escola e, depois, por bairro cadastrado. Conferir todos os candidatos com totalização oficial independente. Distinguir voto nominal, legenda, branco e nulo. A soma dos cargos não é número de eleitores.

O recorte representa votos nas escolas situadas no bairro, não voto residencial identificado. Explicar isso no rodapé e no relatório, sem interromper a narração com texto burocrático.

Conferir coordenadas e limites. Valores ausentes e -1,-1 não são pontos válidos. Locais rurais fora da janela do mapa permanecem nos totais. Registrar correspondências de nomes, ambiguidades, omissões e ano da malha. Sem polígonos oficiais, usar pinos reais; não inventar fronteiras.

Preservar proporção das barras e denominadores. Números da tela, voz e relatório devem concordar. A ferramenta `tools/agregar-tse.py` produz um recorte e uma auditoria; só marca conferência externa quando recebe totais independentes e todos coincidem.
