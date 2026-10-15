# ChatFunnel

Usar a conexão da conta do autor atual. Não importar IDs ou sessões de outra pessoa. Planejar como rascunho e preservar outros fluxos.

Comentário com palavra-chave → resposta pública avisando o direct → DM com botão para o perfil e “Já segui” → condição real de seguidor → link do relatório. Falso vai ao lembrete; verdadeiro vai à entrega. Quando suportado, qualquer nova resposta no direct pode reavaliar a condição. Não simular a verificação de seguidor.

Ler o estado persistido antes da edição e novamente após publicar e antes de ativar. Na entrega: `nextStepId`, `answerStepId`, `unanswerStepId`, destinos de entrada das flows e próximos passos dos botões de URL vazios. Nenhum fallback, lembrete ou espera depois do link. O relatório nunca encaminha ao lembrete.

O construtor pode ligar relatório a fallback automaticamente, ou ativar apesar da descrição. Conferir o estado real e corrigir no editor antes de ativar. Se reconstruir, repetir a conferência. Não repetir toggle sem verificar `isActive` após erro ambíguo.

Verificar a reentrada de uma pessoa em dois vídeos com contato de teste autorizado. O gráfico terminal é necessário, mas não prova entrega ou reentrada. Não duplicar envios manuais nem processar comentários antigos sem autorização.

Gatilho de comentário não deve ficar limitado ao primeiro comentário quando a intenção for aceitar novas solicitações. Escopar o Reel correto e conferir a resposta pública, além da DM. Publicar o Reel não prova que o gatilho está ativo.
