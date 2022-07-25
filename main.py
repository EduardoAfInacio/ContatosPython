import funcoes,excecoes

while True:
    contatos = funcoes.carregarContatos()
    print('---------------------------------------')
    print('---------------------------------------')
    opcao = excecoes.checarOpcaoInt('Escolha uma opção:/n 1 - Adicionar contato /n// 2 - Pesquisar contato /n// 3 - Atualizar contato /n// 4 - Excluir contato /n// 5 - Sair: ')
    print('---------------------------------------')
    print('---------------------------------------')
    if opcao == 1:
      funcoes.criarContato(contatos)
    elif opcao == 2:
      funcoes.imprimirContatoPesquisado(contatos)
    elif opcao == 3:
      funcoes.atualizarContato(contatos)
    elif opcao == 4:
      funcoes.excluirContato(contatos)
    elif opcao == 5:
      break
    else:
      print('Opção inválida')