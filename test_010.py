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
            ('Polo',32000),
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
cur.close();


#Exercicio 1
def processaCompraCliente(cpf:str, produto:str):

  #esta funçao retorna os dados de credito do cliente. Para saber os dados, procure a Class Cliente
  dadosDeCreditoDoCliente = buscaDadosDeCreditoDoClienteNoBancoPorCPF(cpf);
  produto_info=buscaDadosProduto(produto)
  valorCreditoAtual=dadosDeCreditoDoCliente.valor
  valorProduto=produto_info.valor
  valorRestante=valorCreditoAtual-valorProduto
  #1 - Aqui Você deverá pegar os dados do produto.


  #2 - Aqui você vai subtrair o valor do produto do valor do credito do cliente. E jogar numa variavel. 



  #3 - Aqui você valida se o cliente ficou com Valor >= 0 então operação continua, senão joga exception dizendo que 
  #O cliente não tem crédito para a compra. 
  #A mensagem da exception tem que conter o texto pelo menos'credito insuficiente, faltou {valorFaltante} reais!'
  #Dica o valorFaltante deve ser limitado a duas casas decimais!! 
  #Dica 2 o valorFaltante deve ser positivo! Não negativo! Pesquise a função abs. e como limitar valor numerico no python para 2 casas decimais.
  if valorRestante<0:
    valorFaltando=round(abs(valorRestante), 2)
    raise Exception(f"credito insuficiente, faltou {valorFaltando:.2f} reais!")



  #4 - Aqui você deverá rodar a função do banco para atualizar os dados do crédito do cliente.
  #Nome da função é atualizaCredito(cpf, valorAtualizado)
  #O ValorAtualizado é o valor que você calculou do credito do clien"te novo. 
  atualizaCredito(cpf, round(valorRestante,2))



  #5 - Devera retornar o valor restante do crédito do cliente, numa mensagem assim: "Compra concluida. Cliente {dadosCreditoCliente.nome} possui ainda {valorCreditoAtual} de credito."
  #Dica, o valor de float deve ser limitado na resposta até 2 casas decimais!!! 
  return f"Compra concluida. Cliente {dadosDeCreditoDoCliente.nome} possui ainda {valorRestante:.2f} de credito.";




















#Uma classe para o Objeto Cliente que precisamos.
class Cliente:
  def __init__(self, nome:str, cpf:str, valor:float, bloqueio:bool):
    self.nome = nome;
    self.cpf = cpf;
    self.valor = valor;
    self.bloqueio = bloqueio;

#Outra classe para o Objeto Produto que precisamos
class Produto:
  def __init__(self, nome:str, valor:float):
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

  cur.close();
  #Retorna a variavel do tipo Cliente.
  return cliente;


def buscaDadosProduto(nomeProduto:str):
#Cria um cursor para interagir com o banco
  cur = conn.cursor();
  cur.execute("SELECT * FROM Produto WHERE Nome = '%s'" %nomeProduto);
  
  #Preenche os dados do Produto encontrado no banco
  row = cur.fetchone();

  nome = row[0];
  valor = row[1];

  #Cria uma variável do tipo "Produto"
  produto = Produto(nome, valor);

  cur.close();

  #Retorna a variavel do tipo Produto.
  return produto;

def atualizaCredito(cpf:str, valorAtualizado:float):
  curUpdate = conn.cursor();
  commandSql = "UPDATE Credito SET Valor = '%f' WHERE CPF = '%s'" %(valorAtualizado ,cpf);
  curUpdate.execute(commandSql);
  curUpdate.close();
  return;


#==========================================================TESTES====================================================================
def test_validaOperacoesCredito():
  ##Fazendo os testes da primeira questão: 
  resultadoTransacao = processaCompraCliente("00888820027", "Computador");

  assert resultadoTransacao == "Compra concluida. Cliente Fabian possui ainda 31500.00 de credito.", f"Esperava encontrar 'Compra concluida. Cliente Fabian possui ainda 31500.00 de credito.' mas encontrou {resultadoTransacao}"

  resultadoTransacao = processaCompraCliente("00888820027", "PS5");

  assert resultadoTransacao == "Compra concluida. Cliente Fabian possui ainda 27501.00 de credito.", f"Esperava encontrar 'Compra concluida. Cliente Fabian possui ainda 27501.00 de credito.' mas encontrou {resultadoTransacao}"

  resultadoTransacao = processaCompraCliente("00888820027", "Cama");

  assert resultadoTransacao == "Compra concluida. Cliente Fabian possui ainda 22901.00 de credito.", f"Esperava encontrar 'Compra concluida. Cliente Fabian possui ainda 22901.00 de credito.' mas encontrou {resultadoTransacao}"

  with pytest.raises(Exception) as info_da_exceptionFabian:
    processaCompraCliente("00888820027", "Polo");
  
  assert 'credito insuficiente, faltou 9099.00 reais!' in info_da_exceptionFabian.value.args[0].lower(), f"A Exception tem que conter uma mensagem contendo 'credito insuficiente, faltou 9099.00 reais!'"

  resultadoTransacao2 = processaCompraCliente("89810030088", "HB20");

  assert resultadoTransacao2 == "Compra concluida. Cliente Pamela possui ainda 89000.00 de credito.", f"Esperava encontrar 'Compra concluida. Cliente Fabian possui ainda 89000.00 de credito.' mas encontrou {resultadoTransacao2}"
  
  #Encerra conexão quando termina os testes.
  conn.close();