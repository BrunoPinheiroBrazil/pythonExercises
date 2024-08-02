import sqlite3
import pytest

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#Exercício 1
#A aplicação irá buscar dados no banco que criei em memória! 
#Arrumar a função para que a mesma retorne o Cliente do do banco. 
#1° Se não passar o nome do Cliente, deve lançar exceção igual o Eduardo ensinou novamente! 
#2° Na Exception lançada deve pelo menos conter o texto "nome faltando"
#3° A função deve passar a variável nome para o método interno do banco buscaClienteNoBanco.
def buscaCliente(nome:str):
  cliente = Cliente("","",0,"");
  if not nome:
    raise Exception("Nome Faltando")
  cliente= buscaClienteNoBanco(nome)
  return cliente;



#Exercício 2
#Esta segunda função deve contar quantos clientes foram encontrados no banco.
#Analise a função e implemente o que está faltando. 
#Lembrando, a funcionalidade dela é parecida com a de cima. 
#Esta função vai contar os clientes por idade ou por gênero, nunca pelos dois! 
#A prioridade é a Idade, se tiver idade > 0 então deve contar por idade, independente se adicionaram genero ou não.
#Caso a Idade inserida seja 0, então faz a conta pelo Genero e retorna a soma. 
#Regra: 
#1ª Quando inserida a idade, vai buscar a quantidade de clientes que tiverem a idade até o número passado, Exemplo: Inseriu 40, vai trazer 
#os clientes de 0 a 40 anos. 
#2ª Quando a idade for 0, vai buscar por genero, ou seja, o sistema vai somar quantos clientes voltam com o genero igual ao passado
#por parametro. 
#3ª Quando idade for 0 e genero vazio "" então vai lançar Exception que deverá conter o texto, "adicione pelo menos um dos parametros"
#4ª Lembre-se de usar a função interna BuscaClientes passando os dados Idade e Genero que você recebe nesta função! 
#5ª A função BuscaClientes retorna uma lista de clientes, você deverá contar quantos clientes tem nesta lista de retorno e 
#Passar este número no return. 
def contaClientes(idade:int,genero:str):
  if idade >0:
    clientes=buscaClientes(idade, "")
  elif genero:
    clientes= buscaClientes(0, genero)
  else:
    raise Exception("adicione pelo menos um dos parametros")
  return len(clientes)


















#Uma classe para o Objeto que precisamos.
class Cliente:
  def __init__(self, nome:str, cpf:str, idade:int, genero:str):
    self.nome = nome;
    self.idade = idade;
    self.cpf = cpf;
    self.genero = genero;


#Função que busca um cliente no banco!
def buscaClienteNoBanco(nome:str):
  #Cria um cursor para interagir com o banco
  cur = conn.cursor();
  cur.execute("SELECT * FROM Clientes WHERE Nome = '%s'" % nome);
  
  #Preenche os dados do Cliente encontrado no banco
  row = cur.fetchone();

  nome = row[0];
  cpf = row[1];
  idade = row[2];
  genero = row[3];

  #Cria uma variável do tipo "Cliente"
  cliente = Cliente(nome, cpf, idade, genero);

  #Retorna a variavel do tipo JOGO.
  return cliente;


#Esta função retorna uma LISTA de clientes! 
def buscaClientes(idade:int, genero:str):
  #Cria um cursor para interagir com o banco
  cur = conn.cursor();
  if(idade > 0):
    cur.execute("SELECT * FROM Clientes WHERE idade <= '%s'" % idade);
  else:
    cur.execute("SELECT * FROM Clientes WHERE Genero = '%s'" % genero);
  
  #Preenche os dados do Cliente encontrado no banco
  rows = cur.fetchall();

  clientes = list();

  for row in rows:
    cliente = Cliente(row[0],row[1],row[2],row[3]);
    clientes.append(cliente);

  #Retorna a variavel do tipo JOGO.
  return clientes;


#==========================================================TESTES====================================================================
def test_validaClientes():
  # Cria a tabela
  cur = conn.cursor();
  cur.execute('''CREATE TABLE Clientes
                (Nome text, CPF text, Idade real, Genero text)''');

  # Insere as 3 linhas no banco
  cur.execute("""INSERT INTO Clientes VALUES 
              ('Fabian','00888820027',32,'M'),
              ('Bruno','00990930026',38,'M'),
              ('Pamela','89810030088',30,'F'),
              ('Eduardo','99934510024',45,'M'),
              ('Guilherme','80746971001',34,'M'),
              ('Jessica','03289302024',28,'F'),
              ('Mathias','46157777010',64,'M')""");

  # Salva as alterações
  conn.commit();

  ##Fazendo os testes da primeira questão: 
  cliente1 = buscaCliente("Eduardo");
  cliente2 = buscaCliente("Jessica");

  with pytest.raises(Exception) as info_da_exception:
    buscaCliente("");
  
  assert 'nome faltando' in info_da_exception.value.args[0].lower(), f"A Exception tem que conter uma mensagem contendo 'nome faltando'"
  
  assert cliente1.cpf == "99934510024", f"Esperava encontrar 99934510024 mas encontrou {cliente1.cpf}"
  assert cliente1.idade == 45, f"Esperava encontrar 45 mas encontrou {cliente1.idade}"
  assert cliente1.genero == 'M', f"Esperava encontrar 45 mas encontrou {cliente1.genero}"
  assert cliente2.cpf == "03289302024", f"Esperava encontrar 03289302024 mas encontrou {cliente2.cpf}"
  assert cliente2.idade == 28, f"Esperava encontrar 28 mas encontrou {cliente2.idade}"
  assert cliente2.genero == 'F', f"Esperava encontrar F mas encontrou {cliente2.genero}"


  #### Fazendo os testes da segunda questão:
  contagemClienteAte40 = contaClientes(40,"");
  contagemClienteAte30 = contaClientes(30,"M");
  contagemClienteAte60 = contaClientes(60, "");

  assert contagemClienteAte40 == 5, f"Esperava encontrar 5 clientes mas encontrou {contagemClienteAte40}";
  assert contagemClienteAte30 == 2, f"Esperava encontrar 2 clientes mas encontrou {contagemClienteAte30}";
  assert contagemClienteAte60 == 6, f"Esperava encontrar 6 clientes mas encontrou {contagemClienteAte60}";

  contagemClientesM = contaClientes(0, "M");
  contagemClientesF = contaClientes(0, "F");

  assert contagemClientesM == 5, f"Esperava encontrar 5 clientes do genero Masculino mas encontrou {contagemClientesM}";
  assert contagemClientesF == 2, f"Esperava encontrar 5 clientes do genero Feminino mas encontrou {contagemClientesF}";

  with pytest.raises(Exception) as info_da_exception2:
    contaClientes(0, "");
  
  assert 'adicione pelo menos um dos parametros' in info_da_exception2.value.args[0].lower(), f"A Exception tem que conter uma mensagem contendo 'adicione pelo menos um dos parametros'"

  #Encerra conexão quando termina os testes.
  conn.close();