---
format: 1080x1920
duration: 29.75s
message: A vitória municipal esconde disputas muito próximas em locais de votação de Várzea Grande.
arc: Pergunta → contexto → contraste → revelação → consulta pessoal
mode: collaborative
---

## Direção
Mapa contínuo é a espinha visual. Identidade de Cuiabá: fundo #0A1D1A, texto #F2F6EF, verde #75D49E e vermelho #ED807B, Agency/Body locais. Sem vinheta. Voz Paulo expressiva; música instrumental discreta e sons nos números. A estimativa é 35 s; narração define a duração final. Quadro inicial: ../../outputs/quadro-inicial-varzea-grande-v1.png. Roteiro completo: ../../outputs/roteiro-varzea-grande-v1.md.

## Ainda aberto
Roteiro e quadro aprovados. Voz, animação, render e PDF concluídos. Fluxo VG configurado e desativado até a postagem; horários finais em audio_meta.json.

## Frame 1 — Só dois votos
- status: rendered
- src: compositions/hook.html
- duration: 4s
- motion: multi-phase-camera + kinetic-beat-slam
- scene: EM QUAL BAIRRO A DIFERENÇA FOI SÓ 2 VOTOS?
Pergunta sobre mapa contextual. Primeiro movimento em 0,2 s, sem mostrar a resposta.

## Frame 2 — Cidade e contraste
- status: rendered
- src: compositions/cidade.html
- duration: 5s
- motion: multi-phase-camera
- scene: Flávio venceu no município; existem locais com liderança de Lula.
Legenda entra com a voz. Aproximação preserva rio, ruas e orientação.

## Frame 3 — Cristo Rei e Parque do Lago
- status: rendered
- src: compositions/verde.html
- duration: 5s
- motion: coordinate-target-zoom + stat-bars-and-fills
- scene: Duas lideranças de Flávio.
Passagem contínua por bairros identificados, relevo discreto sem deslocar fronteiras.

## Frame 4 — Jardim Glória II
- status: rendered
- src: compositions/gloria.html
- duration: 5s
- motion: coordinate-target-zoom + stat-bars-and-fills
- scene: Escola, marcador vermelho, 1.146 × 1.132 e 14 VOTOS.
Enquadrar escola do cadastro; não pintar todo o polígono Glória de vermelho.

## Frame 5 — Capão do Pequi
- status: rendered
- src: compositions/pequi.html
- duration: 9s
- motion: coordinate-target-zoom + stat-bars-and-fills
- scene: Duas escolas, 658 × 656, 2 VOTOS.
Resolve a pergunta inicial. Mostrar pontos das escolas e nome do agrupamento, mantendo a geografia oficial. Reservar 0,5 s para leitura estável.

## Frame 6 — Consulta e envio
- status: rendered
- src: compositions/cta.html
- duration: 7s
- motion: multi-phase-camera + kinetic-beat-slam
- scene: COMENTE VG. Manda para alguém conferir também.
Retorno ao mapa; texto guia o acesso ao relatório. Movimento desacelera sem salto final.
