# Automação na conta do autor

Conectar o ChatFunnel e o Instagram do autor atual. Escolher o Reel e a palavra-chave, subir o relatório correto e testar a URL. Não usar IDs de fluxos, canais, contatos ou mídias de outra conta.

Fluxo de referência:

```text
Comentário com palavra-chave
  ├─ resposta pública: avisa para conferir o direct e as solicitações
  └─ DM: pede para seguir + Ir para o perfil + Já segui
        └─ verifica de verdade se segue
             ├─ sim → link/PDF → FIM
             └─ não → lembrete e possibilidade de nova verificação
```

Qualquer resposta no direct pode reavaliar se a pessoa seguiu, quando o recurso estiver disponível na conta. Se não houver verificação real de seguidor, informar a limitação; não tratar o clique em “Já segui” como prova.

## Antes de ativar

- Ler o fluxo persistido, editar o rascunho, salvar/publicar e reler.
- Conferir gatilho de novos comentários e escopo do Reel. Resposta pública e DM são dois comportamentos a verificar.
- A entrega deve ser terminal: `nextStepId`, `answerStepId`, `unanswerStepId`, `nextStepInputReceivedId`, `nextStepInputDontReceivedId` e destinos de próximos passos dos botões de URL vazios/nulos conforme o formato da plataforma.
- Verdadeiro na condição de seguidor leva ao relatório; falso leva ao lembrete. O relatório não leva a lembrete, fallback, espera ou outro fluxo.
- Um construtor pode ligar relatório a fallback ou ativar durante a criação; conferir o estado persistido em vez de confiar na descrição.
- Após reconstrução, repetir a verificação. Ativar somente no escopo autorizado, preservando os outros fluxos.
- Com contato de teste autorizado, comentar em um vídeo, receber o relatório e entrar em outro vídeo. Conferir entrega real, reentrada e resposta pública. Uma configuração terminal não prova sozinha esses três resultados.

Não enviar testes para terceiros, varrer comentários antigos nem repetir envios que o autor já fez manualmente sem autorização.
