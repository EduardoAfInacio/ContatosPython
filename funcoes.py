import json,os,excecoes,tabulate

def carregarContatos():
  contatos = {}
  if os.path.exists('contatos.json'):
      with open('contatos.json') as f:
        contatos = json.load(f)
  return contatos


def organizarContatos(contatos):
  contatosOrganizados = {chave:valor for chave,valor in sorted(contatos.items())}
  return contatosOrganizados


def guardarContato(contatos):
  contatosOrganizados=organizarContatos(contatos)
  with open('contatos.json','w') as f:
      json.dump(contatosOrganizados,f,indent=2, separators=(',',':'))


def criarContato(contatos):
  nome = excecoes.checarOpcaoStr("Digite o nome do contato: ").strip()
  tel = excecoes.checarOpcaoInt("Digite o telefone do contato: ")
  email = excecoes.checarOpcaoStr("Digite o email do contato: ").strip()
  contatos[f'{nome.lower()}'] = {f'Nome': f'{nome}', 'Telefone': f'{tel}', 'Email': f'{email}'''}
  guardarContato(contatos)


def pesquisarContato(contatos):
  listaChaves=[]
  nomePesquisado = excecoes.checarOpcaoStr('Digite o nome a ser pesquisado (Caso queira visualizar todos os contatos, de enter sem digitar nada.): ')
  for chave in contatos:
      if chave.startswith(nomePesquisado):
        listaChaves.append(chave)
  return listaChaves


def imprimirContatoPesquisado(contatos):
  table = []
  listaChaves = pesquisarContato(contatos)
  for chave in listaChaves:
      table.append([
        contatos[chave]['Nome'],
        contatos[chave]['Telefone'],
        contatos[chave]['Email']
      ])
  print(tabulate.tabulate(table,headers=['Nome','Telefone','Email'],tablefmt='grid'))


def atualizarDados(contatos, chaveAtu):
  novoNome = excecoes.checarOpcaoStr('Digite o novo nome do contato: ')
  novoTel = excecoes.checarOpcaoInt('Digite o novo telefone do contato: ')
  novoEmail = excecoes.checarOpcaoStr('Digite o novo email do contato: ')
  contatos[f'{novoNome.lower()}']=contatos[f'{chaveAtu}'] 
  del contatos[chaveAtu]
  contatos[f'{novoNome}'] = {f'Nome': f'{novoNome}', 'Telefone': f'{novoTel}', 'Email': f'{novoEmail}'''}
  guardarContato(contatos)
  print('Contato atualizado')


def auxiliarPesquisa1(contatos):
  listaChaves = pesquisarContato(contatos)
  print('Lista de nomes encontrados: ')
  print('-------------------------------------------------')
  for i,chave in enumerate(listaChaves):
    print(f'{i}'' --> 'f'{chave}')
    print('--------------')
  if len(listaChaves)<1:
    print('Lista de contatos vazia!!! Não foi possível realizar alterações.')
  return listaChaves


def auxiliarChecagem(contatos,listaChaves):
  while True:
      atu = excecoes.checarOpcaoInt('Digite o número correspondede ao contato que quer realizar a ação: ')
      if atu>len(listaChaves) or atu<0:
        print('Número digitado é invalido. Tente novamente.')
      else:
        for i,chave in enumerate(listaChaves):
          if i==atu:
             chaveAtu = chave
             return chaveAtu
  

def atualizarContato(contatos):
  listaChaves=auxiliarPesquisa1(contatos)
  if len(listaChaves)<1:
    return
  elif len(listaChaves)==1:
    print(f'O nome do contato a ser alterado é: {listaChaves[0]}')
    print('-------------------------------------------------')
    atualizarDados(contatos, listaChaves[0])
  else:
    while True:
      chaveAtu=auxiliarChecagem(contatos,listaChaves)
      atualizarDados(contatos, chaveAtu)
      break

    
def desejaExcluir(contatos, chaveAtu):
  while True:
    resposta = excecoes.checarOpcaoStr('Deseja realmente excluir esse contato? Digite s para SIM ou n para NÃO: ')
    if resposta=='s':
       del contatos[f'{chaveAtu}']
       guardarContato(contatos)
       print('O contato foi excluído da sua lista de contatos!')
       break
    elif resposta=='n':
        print('Voltando...')
        break
    else:
        print('Opção inválida. Tente novamente.')
  

def excluirContato(contatos):
  listaChaves=auxiliarPesquisa1(contatos)
  if len(listaChaves)<1:
    return
  elif len(listaChaves)==1:
    print(f'O nome do contato a ser excluido é: {listaChaves[0]}')
    print('-------------------------------------------------')
    desejaExcluir(contatos,listaChaves[0])
  else:
    chaveAtu=auxiliarChecagem(contatos,listaChaves)
    desejaExcluir(contatos,chaveAtu)
    
  
    
      


  
                                        
    
  
      
    
  
    
    
