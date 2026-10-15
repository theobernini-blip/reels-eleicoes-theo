# Reels Eleições Théo

Kit para continuar, em outra conta do Codex, a produção da série de vídeos eleitorais de Théo Bernini: mapas reconhecíveis, dados conferidos, motion contínuo, números legíveis, voz expressiva e relatórios.

**Não precisa ter conta no GitHub para baixar.** [Baixe o ZIP](https://github.com/theobernini-blip/reels-eleicoes-theo/archive/refs/heads/main.zip), extraia e abra a pasta extraída como projeto local no Codex. Também pode clonar com Git.

## Comece por aqui

1. Abra esta pasta no Codex usando **a sua conta**.
2. Cole o texto de [COMECE-NO-CODEX.md](COMECE-NO-CODEX.md).
3. Copie `config/perfil.example.json` para `config/perfil.local.json` e preencha seu nome, @perfil e pasta de entrega. Seu arquivo local não entra no Git.
4. O Codex lê a skill em `.agents/skills/reels-eleicoes-theo/` e configura as dependências que faltarem. [Como o Codex encontra skills](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

Para só experimentar um exemplo já pronto:

```powershell
cd projetos/reel-campo-novo-bairros-2026
npm run dev
```

Abra o endereço que o HyperFrames mostrar. A prévia tem animação e SFX; a faixa de narração é um marcador silencioso. Para finalizar um vídeo, gere a voz na própria conta. Não é necessário conectar Instagram para testar os exemplos.

## O que vem no kit

- **12 projetos HTML/CSS/GSAP editáveis**, com cenas, mapas, roteiros e efeitos sonoros locais; faixa de voz preparada para receber a narração própria.
- A **skill Reels Eleições Théo**, com as escolhas editoriais e correções acumuladas na série.
- Exemplos de **roteiros e legendas**, fontes de dados e agregados por bairro/escola.
- Ferramentas para **agregar CSVs do TSE**, gerar CSV/PDF, criar cópia de um modelo e conferir os arquivos.
- Orientações para **voz, sincronização, revisão, render e ChatFunnel**, incluindo encerramento do fluxo após o link.

O catálogo completo está em [catalogo-projetos.json](catalogo-projetos.json). As referências de maior utilidade para começar são:

| Referência | Para estudar |
| --- | --- |
| `reel-cuiaba-bairros-2026` | Formato de bairros que motivou a série; mapa de ruas e revelação por lugares |
| `reel-campo-novo-bairros-2026` | Formato recente, câmera contínua, pinos, SFX e ritmo |
| `reel-mato-grosso-2026` | Mapa do estado, comparação e cadeiras |
| `reel-alta-floresta-darlan-motion` | Identidade adaptada para cliente |
| `reel-pivetta-2026` | Formato com retrato; fotografia substituída por placeholder |

## Pré-requisitos

Node.js **22 ou superior** com npm; Python **3.10 ou superior** para os dados. O HyperFrames baixa seus componentes na primeira execução; requer internet nessa instalação. Para gerar PDF e novos mapas:

```powershell
python -m pip install -r requirements.txt
```

Na raiz, `npm run diagnostico` confere os programas e `npm run verificar` confere caminhos, arquivos e padrões de credenciais. Os modelos mantêm suas versões de HyperFrames; o projeto mais recente usa `0.8.150`.

Se as skills de vídeo ainda não estiverem disponíveis na conta do colega, peça ao Codex para instalar o conjunto oficial do HyperFrames. O comando da CLI é:

```powershell
npx --yes hyperframes@0.8.150 skills update hyperframes general-video hyperframes-core hyperframes-animation hyperframes-keyframes hyperframes-creative hyperframes-cli hyperframes-registry hyperframes-studio media-use hyperframes-audio
```

Se o HyperFrames já estiver instalado por plugin, use as skills desse plugin e seu mecanismo de atualização. Não instale cópias duplicadas.

## Criar um vídeo novo

```powershell
node tools/novo-projeto.mjs --modelo reel-campo-novo-bairros-2026 --nome meu-primeiro-reel
```

Isso cria `producoes/meu-primeiro-reel/`, sem alterar o modelo. **Os dados dessa cópia ainda pertencem à cidade do exemplo.** O Codex deve substituir dados, mapas, roteiro, perfil, voz e tempos de cena antes de tratá-la como produção nova. Não basta trocar o nome da cidade.

Siga [o fluxo de produção](docs/PRODUCAO.md). Apresente roteiro e quadro; depois prévia animada; renderize a versão final quando houver aprovação para ela.

## Contas e custos

O projeto não transporta acesso a contas. Conecte **seu** ElevenLabs se for gerar voz e **seu** ChatFunnel/Instagram se for entregar relatórios. Para adaptar um cliente, configure também perfil, canal e identidade corretos. A autorização de uma produção antiga não vale para um novo envio ou ativação.

As animações e tabelas são código local. TTS, serviços de mídia e recursos de cada conta podem consumir créditos próprios. Não há compra ou chamada paga automática ao abrir o repositório.

## Fontes e adaptações do pacote público

Dados: TSE; limites: IBGE; mapas de ruas: OpenStreetMap. Os exemplos são registros da eleição indicada em cada projeto, não dados que se atualizam sozinhos. Consulte [DADOS-E-MAPAS.md](docs/DADOS-E-MAPAS.md).

As narrações originais e arquivos de conta não são publicados. As fontes comerciais Agency FB/Bahnschrift deram lugar a **Barlow Condensed/Barlow**, com licenças OFL incluídas. Os SFX foram sintetizados para o kit; músicas comerciais devem ser escolhidas no catálogo da conta que publicar. O retrato do exemplo Pivetta foi substituído por um marcador editável. Essas alterações preservam a estrutura visual, mas o pacote público não é uma cópia pixel a pixel dos vídeos anteriores. Consulte [TERCEIROS.md](TERCEIROS.md).

Nenhuma credencial, lista de contatos, sessão de navegador, fluxo real ou banco Supabase acompanha este material.
