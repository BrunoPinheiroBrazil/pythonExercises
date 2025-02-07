import sqlite3
import pytest

#Uma classe para o Objeto Usuario que precisamos.
class Produto:
  def __init__(self, nome:str, descricao:str, tipo:str, valor:float):
    self.nome = nome;
    self.descricao = descricao;
    self.tipo = tipo;
    self.valor = valor;

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#1° Cria a tabela de carros com os campos 'id chave automatica, nome texto, descricao texto, tipo texto e valor decimal' usando a variável 
#da conexão conn e um cursor igual os outros exercícios.
cur= conn.cursor();

cur.execute('''CREATE TABLE Produtos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               descricao TEXT NOT NULL, 
               tipo TEXT NOT NULL,
               valor DECIMAL(5, 2) NOT NULL
            )''');


#2° Salva as alterações com commit. 
conn.commit();

#3° feche o cursor
cur.close();

def insereProduto(produto:Produto):
  curInsert = conn.cursor();  

  commandSql = "INSERT INTO Produtos(nome, descricao, tipo, valor) VALUES('%s','%s','%s','%f')" %(produto.nome , produto.descricao, produto.tipo, produto.valor);
  
  curInsert.execute(commandSql);
  
  id = curInsert.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curInsert.close();

  return idInserido;


insereProduto(Produto("Cafe", "Po de cafe 1kg ", "Alimento", 8.90));
insereProduto(Produto("Tang Laranja", "Suco de Laranja em pó marca Tang", "Alimento", 0.89));
insereProduto(Produto("Dell Inspiron", "Notebook da Dell", "Eletronicos", 6999.90));
insereProduto(Produto("Controle XBOX", "Joystick do XBOX 360", "Eletronicos", 199.90));
insereProduto(Produto("Agua", "garrafa com 2 litros de agua", "Alimento", 7.90));
insereProduto(Produto("Cha", "Pacotinho de Cha", "Alimento", 2.90));
insereProduto(Produto("Vassoura", "Vassoura para limpeza", "Limpeza", 29.90));
insereProduto(Produto("Esponja", "Esponja para lavar louca", "Limpeza", 3.90));

#==================================================== Exercicio 1 ================================================================================
#Complete a função que deve buscar o produto e retornar um objeto do tipo Produto
def encontraProdutoPorID(id:int) -> Produto:

  return Produto("","","",0);

#==================================================== Exercicio 2 ================================================================================
#Esta função vai ser uma função de pesquisa de produtos por Tipo!!
# Arrume a função para a mesma buscar no banco os produtos baseado na coluna "tipo"
# E a mesma função deve preencher uma lista com os produtos encontrados e retornar a lista com os itens encontrados. 
# Como você pode observar está faltando bastante coisa nesta função, analise e complete a mesma para que ela passe nos testes.
def listarProdutosPorTipo(tipo:str) -> list[Produto]:
  produto = Produto("","","",0);
  produtos = [produto];
  
  return produtos;

#==================================================== Exercicio 3 ================================================================================
#Esta função aqui vai fazer a soma dos valores de todos produtos por tipo. 
#Ela recebe como parametro o tipo, e retorna o valor somado dos produtos encontrados pelo tipo.
#Observe que a função tá vazia, tente completar ela corretamente para que a mesma funcione e os testes passem.
#Use exercicios anteriores como referência para acessar o banco, buscar os itens em lista, e somar cada um encontrado nesta lista
def somaValoresPorTipo(tipo:str) -> float:

  return 0.0;


#============================================================TESTES=====================================================================================

def test_validaEncontraProdutoPorID():

  prod1 = encontraProdutoPorID(1);
  prod2 = encontraProdutoPorID(3);
  prod3 = encontraProdutoPorID(4);
  prod4 = encontraProdutoPorID(5);

  assert prod1.nome == "Cafe", f"Esperava encontrar o nome 'Cafe' mas encontrou {prod1.nome}";
  assert prod2.nome == "Dell Inspiron", f"Esperava encontrar o nome 'Dell Inspiron' mas encontrou {prod2.nome}";
  assert prod3.nome == "Controle XBOX", f"Esperava encontrar o nome 'Controle XBOX' mas encontrou {prod3.nome}";
  assert prod4.nome == "Agua", f"Esperava encontrar o nome 'Agua' mas encontrou {prod4.nome}";

  return;

def test_validaListaProdutosPorTipo():

  alimentos = listarProdutosPorTipo("Alimentos");
  eletronicos = listarProdutosPorTipo("Eletronicos");
  limpeza = listarProdutosPorTipo("Limpeza");

  for a in alimentos:
    assert a.tipo == "Alimentos", f"Erro no teste da litagem de alimentos.. todos itens tem que ser do tipo alimentos";
  
  for e in eletronicos: 
    assert e.tipo == "Eletronicos", f"Erro no teste de listagem de eletronicos.. todos os itens tem que ser do tipo Eletronicos";
  
  for l in limpeza:
    assert l.tipo == "Limpeza", f"Erro no teste de listagem de Limpeza.. todos os itens tem que ser do tipo Limpeza";
  
  return;

def test_somaValoresPorTipo():

  totalAlimentos = somaValoresPorTipo("Alimentos");
  totalEletronicos = somaValoresPorTipo("Eletronicos");
  totalLimpeza = somaValoresPorTipo("Limpeza");

  assert totalAlimentos == 20.59, f"Esperava encontrar o valor total de Alimentos de '20.59' porém encontrou {totalAlimentos}";
  assert totalEletronicos == 7199.80, f"Esperava encontrar o valor total de Eletronicos de '7199.80' porém encontrou {totalEletronicos}";
  assert totalLimpeza == 33.80, f"Esperava encontrar o valor total de Limpeza de '33.80' porém encontrou {totalLimpeza}";

  return;


#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();