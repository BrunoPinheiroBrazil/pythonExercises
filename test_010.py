import sqlite3
import pytest

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');
# Cria a tabela
cur = conn.cursor();
cur.execute('''CREATE TABLE Credito
              (Nome text, CPF text, Valor real, Bloqueio boolean)''');

cur.execute('''CREATE TABLE Produto
              (Nome text, Valor real)''');

# Insere as 3 linhas no banco
cur.execute("""INSERT INTO Credito VALUES 
            ('Fabian','00888820027',35000,False),
            ('Bruno','00990930026',20000,False),
            ('Pamela','89810030088',150000,False),
            ('Eduardo','99934510024',5000,False),
            ('Guilherme','80746971001',-500000,True),
            ('Jessica','03289302024',-100000,True),
            ('Mathias','46157777010',1000,False)""");

cur.execute("""INSERT INTO Produto VALUES
            ('Computador',3500),
            ('Monitor',1400),
            ('Polo',38000),
            ('HB20',61000),
            ('TV',4100),
            ('PS3',1200),
            ('PS4',1800),
            ('PS5',3999),
            ('Cama',4600),
            ('Celular',1799),
            ('Mouse',50)""");

# Salva as alterações
conn.commit();


#Exercicio 1
def processaCompraCliente(cpf:str, produto:str):

  #esta funçao retorna todos os clientes do banco. (Uma lista de Objeto Cliente)
  dadosDeCreditoDoCliente = buscaDadosDeCreditoDoClienteNoBancoPorCPF(cpf);
  
  #1 - Aqui Você deverá pegar os dados do produto.

  
  #2 - Aqui você vai subtrair o valor do produto do valor do credito do cliente. E jogar numa variavel. 

  
  #3 - Aqui você valida se o cliente ficou com Valor >= 0 então operação continua, senão joga exception dizendo que 
  #O cliente não tem crédito para a compra. 


  #4 - Aqui você deverá rodar a função do banco para atualizar os dados do crédito do cliente.
  #Nome da função é atualizaCredito(cpf, valorAtualizado)
  #O ValorAtualizado é o valor que você calculou do credito do cliente novo. 

  #5 - Devera retornar o valor restante do crédito do cliente, numa mensagem assim: "Compra concluida. Cliente {nomeCliente} possui ainda {valorCreditoAtual}."
  return True;




















#Uma classe para o Objeto que precisamos.
class Cliente:
  def __init__(self, nome:str, cpf:str, valor:float, bloqueio:bool):
    self.nome = nome;
    self.cpf = cpf;
    self.valor = valor;
    self.bloqueio = bloqueio;

class Produto:
  def __init__(self, nome:str, valor:str):
    self.nome = nome;
    self.valor = valor;

#Função que busca um cliente no banco!
def buscaDadosDeCreditoDoClienteNoBancoPorCPF(cpf:str):
  #Cria um cursor para interagir com o banco
  cur = conn.cursor();
  cur.execute("SELECT * FROM Credito WHERE CPF = '%s'" % cpf);
  
  #Preenche os dados do Cliente encontrado no banco
  row = cur.fetchone();

  nome = row[0];
  cpf = row[1];
  valor = row[2];
  bloqueio = row[3];

  #Cria uma variável do tipo "Cliente"
  cliente = Cliente(nome, cpf, valor, bloqueio);

  #Retorna a variavel do tipo JOGO.
  return cliente;


def buscaDadosProduto(nomeProduto:str):
#Cria um cursor para interagir com o banco
  cur = conn.cursor();
  cur.execute("SELECT * FROM Produto WHERE Nome = '%s'" % nomeProduto);
  
  #Preenche os dados do Cliente encontrado no banco
  row = cur.fetchone();

  nome = row[0];
  valor = row[1];

  #Cria uma variável do tipo "Cliente"
  produto = Produto(nome, valor);

  #Retorna a variavel do tipo JOGO.
  return produto;

def atualizaCredito(cpf:str, valorAtualizado:float):
  curUpdate = conn.cursor();
  curUpdate.execute("UPDATE Credito SET Valor = '%f' WHERE CPF = '%s'" % valorAtualizado, cpf);
  return;


#==========================================================TESTES====================================================================
def test_validaOperacoesCredito():
  ##Fazendo os testes da primeira questão: 
  resultadoTransacao = processaCompraCliente("00888820027", "Computador");

  assert resultadoTransacao == True, f"Esperava encontrar True mas encontrou {resultadoTransacao}"

  #Encerra conexão quando termina os testes.
  conn.close();