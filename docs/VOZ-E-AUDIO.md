# Voz e áudio

Conectar ElevenLabs na conta autorizada do autor. Se o conector não expuser geração, usar a interface do serviço e baixar o áudio. Não copiar API key, sessão ou configuração de outro usuário.

Referência da série: **Paulo — Expressive and Confident**, com surpresa e entusiasmo naturais; estabilidade em torno de 25% e similaridade em torno de 75%, quando esses controles existirem no modelo escolhido. A disponibilidade do modelo e da voz depende da conta; não adivinhar IDs. Fazer uma amostra curta antes de gerar a narração inteira. Nada de clonagem sem autorização e material adequado.

Evitar fala monótona ou gritada. Acentuar números, mudanças de lugar e a revelação com intenção de conversa. Aceleração foi usada em algumas gravações, mas não é uma regra: conferir compreensão e preservar tom. Normalização de referência: -16 LUFS, -1,5 dBTP e LRA 9; ajustar conforme a gravação.

Salvar voz em `assets/narracao.wav` ou no arquivo referenciado pela composição. Transcrever/alinhá-la com a ferramenta local disponível ou com o recurso de transcrição autorizado e refazer os tempos das cenas. A duração declarada não deve cortar o fim da frase.

SFX do kit: cliques e whooshes locais, curtos, em mudanças de cena e revelações; não em cada palavra. Os volumes dos modelos já deixam a voz em primeiro plano. Ouvir no celular e verificar picos quando os sons coincidem.

Música sugerida deve ser adicionada pelo catálogo autorizado da conta do Instagram quando indicada. A referência de 8–12% não se traduz igualmente entre músicas: a fala precisa continuar clara.

Exemplo de normalização com FFmpeg, quando já instalado:

```powershell
ffmpeg -i voz-original.wav -af "loudnorm=I=-16:TP=-1.5:LRA=9" -ar 48000 assets/narracao.wav
```

Não sobrescrever o único original. Gerar voz e outros serviços pode consumir os créditos do próprio autor; o setup do kit não faz essas chamadas automaticamente.
