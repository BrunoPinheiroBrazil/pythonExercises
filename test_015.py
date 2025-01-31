import sqlite3
import pytest

#Uma classe para o Objeto Usuario que precisamos.
class Produto:
  def __init__(self, nome:str, descricao:str, quantidade:int, valor:float):
    self.nome = nome;
    self.descricao = descricao;
    self.quantidade = quantidade;
    self.valor = valor;

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#1° Cria a tabela de carros com os campos 'id chave automatica, nome texto, descricao texto, quantidade inteiro e valor decimal' usando a variável 
#da conexão conn e um cursor igual os outros exercícios.
cur= conn.cursor();

cur.execute('''CREATE TABLE Produtos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               descricao TEXT NOT NULL, 
               quantidade INTEGER NOT NULL,
               valor DECIMAL(5, 2) NOT NULL
            )''');


#2° Salva as alterações com commit. 
conn.commit();

#3° feche o cursor
cur.close();

def insereProduto(produto:Produto):
  curInsert = conn.cursor();  

  commandSql = "INSERT INTO Produtos(nome, descricao, quantidade, valor) VALUES('%s','%s','%i','%f')" %(produto.nome , produto.descricao, produto.quantidade, produto.valor);
  
  curInsert.execute(commandSql);
  
  id = curInsert.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curInsert.close();

  return idInserido;


insereProduto(Produto("Nestle", "Uma barra de chocolate preto", 10, 4.90));
insereProduto(Produto("Coca Cola", "Refrigerante de cola", 15, 9.90));
insereProduto(Produto("Colgate", "Pasta de dentes Branca", 25, 6.90));
insereProduto(Produto("Havainas", "Chinelos de borracha verde", 10, 29.90));
insereProduto(Produto("Brahma", "Lata de cerveja", 20, 5.90));
insereProduto(Produto("OMO", "Sabão em pó", 5, 14.90));

#==================================================== Exercicio 1 ================================================================================
#Complete a função que deve buscar a quantidade atual de produtos, subtrair a quantidadeAReduzir passada por parametro
#e atualizar a tabela produtos com a nova quantidade. 
def subtraiQuantidadeProduto(id:int, quantidadeAReduzir:int):
  

  return;

#==================================================== Exercicio 2 ================================================================================
#Complete a função para que a mesma ao receber o ID do produto e o novo valor, atualize a tabela Produtos com o novo valor
#Deste produto usando o ID fornecido nos parâmetros.
def atualizaPrecoProduto(id:int, novoValor:float):
  
  return;


#===============================================Funções pré definidas=================================================================
def  buscaProdutoNoBancoPeloID(id:int) -> Produto:

  cur = conn.cursor();
  cur.execute("SELECT nome, descricao, quantidade, valor FROM Produtos WHERE Id = '%i'" % id);
  
  row = cur.fetchone();

  #Se não encontrou nada, retorna um usuário vazio!
  if(len(row)==0):
    return Produto("","",0,0);

  nome = row[0];
  descricao = row[1];
  quantidade = row[2];
  valor = row[3];

  produto = Produto(nome, descricao, quantidade, valor);
  return produto;



#============================================================TESTES=====================================================================================

def test_validaSubtraiQuantidade():
  
  subtraiQuantidadeProduto(1, 5);
  subtraiQuantidadeProduto(2, 3);
  subtraiQuantidadeProduto(3, 1);
  subtraiQuantidadeProduto(4, 4);


  prod1 = buscaProdutoNoBancoPeloID(1);
  prod2 = buscaProdutoNoBancoPeloID(2);
  prod3 = buscaProdutoNoBancoPeloID(3);
  prod4 = buscaProdutoNoBancoPeloID(4);

  assert prod1.quantidade == 5, f"Esperava encontrar a quantidade 5 mas encontrou {prod1.quantidade}"
  assert prod2.quantidade == 12, f"Esperava encontrar a quantidade 12 mas encontrou {prod2.quantidade}"
  assert prod3.quantidade == 24, f"Esperava encontrar a quantidade 24 mas encontrou {prod3.quantidade}"
  assert prod4.quantidade == 6, f"Esperava encontrar a quantidade 6 mas encontrou {prod4.quantidade}"

  return;

def test_validaAtualizaPrecos():

  atualizaPrecoProduto(1, 5.90);
  atualizaPrecoProduto(2, 12.90);
  atualizaPrecoProduto(3, 8.90);

  prod1 = buscaProdutoNoBancoPeloID(1);
  prod2 = buscaProdutoNoBancoPeloID(2);
  prod3 = buscaProdutoNoBancoPeloID(3);
  prod4 = buscaProdutoNoBancoPeloID(4);

  assert prod1.valor == 5.90, f"Esperava encontrar o valor 5.90 mas encontrou {prod1.valor}"
  assert prod2.valor == 12.90, f"Esperava encontrar a valor 12.90 mas encontrou {prod2.valor}"
  assert prod3.valor == 8.90, f"Esperava encontrar a valor 8.90 mas encontrou {prod3.valor}"

  return;


#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();