import sqlite3
import pytest

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');
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


#Exercicio 1
#O metodo aqui vai preencher a variavel listaDeClientes com todos clientes do banco
#Sua missão é colocar os clientes em ordem alfabética. (Pelos nomes)
#E depois retornar a lista;
def buscaEOrdenaClientes():

  #esta funçao retorna todos os clientes do banco. (Uma lista de Objeto Cliente)
  listaDeClientes = buscaTodosClientes();
  listaDeClientes.sort(key=lambda cliente: cliente.nome);
  return listaDeClientes;




















#Uma classe para o Objeto que precisamos.
class Cliente:
  def __init__(self, nome:str, cpf:str, idade:int, genero:str):
    self.nome = nome;
    self.idade = idade;
    self.cpf = cpf;
    self.genero = genero;



#Esta função retorna uma LISTA de clientes! 
def buscaTodosClientes():
  #Cria um cursor para interagir com o banco
  cur = conn.cursor();

  cur.execute("SELECT * FROM Clientes");
  
  #Preenche os dados do Cliente encontrado no banco
  rows = cur.fetchall();

  clientes = list();

  for row in rows:
    cliente = Cliente(row[0],row[1],row[2],row[3]);
    clientes.append(cliente);

  #Retorna uma lista de objetos do tipo Cliente.
  return clientes;






#==========================================================TESTES====================================================================
def test_validaClientes():
  ##Fazendo os testes da primeira questão: 
  clientesOrdenados = buscaEOrdenaClientes();

  assert clientesOrdenados[0].cpf == "00990930026", f"Esperava encontrar 00990930026 mas encontrou {clientesOrdenados[0].cpf}"
  assert clientesOrdenados[1].cpf == "99934510024", f"Esperava encontrar 99934510024 mas encontrou {clientesOrdenados[1].cpf}"
  assert clientesOrdenados[2].cpf == "00888820027", f"Esperava encontrar 99934510024 mas encontrou {clientesOrdenados[2].cpf}"
  assert clientesOrdenados[3].cpf == "80746971001", f"Esperava encontrar 80746971001 mas encontrou {clientesOrdenados[3].cpf}"
  assert clientesOrdenados[4].cpf == "03289302024", f"Esperava encontrar 03289302024 mas encontrou {clientesOrdenados[4].cpf}"
  assert clientesOrdenados[5].cpf == "46157777010", f"Esperava encontrar 46157777010 mas encontrou {clientesOrdenados[5].cpf}"
  assert clientesOrdenados[6].cpf == "89810030088", f"Esperava encontrar 89810030088 mas encontrou {clientesOrdenados[6].cpf}"

  #Encerra conexão quando termina os testes.
  conn.close();