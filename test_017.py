import sqlite3;

#Uma classe para o Objeto Usuario que precisamos.
class Item:
  def __init__(self, nome:str, descricao:str, tipo:str, valor:float):
    self.nome = nome;
    self.descricao = descricao;
    self.tipo = tipo;
    self.valor = valor;

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#Crie o comando que executa a criação da tabela necessária.
# Analise os códigos e ache oque precisa de nome, campo e etc para criação da tabela.
cursor = conn.cursor();
cursor.execute('''
                  CREATE TABLE Itens (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      descricao TEXT NOT NULL,
                      tipo TEXT NOT NULL,
                      valor DECIMAL(10, 2) NOT NULL
               
                  )''');

conn.commit();

cursor.close();

def insereItem(item:Item):
  curInsert = conn.cursor();  

  commandSql = "INSERT INTO Itens(nome, descricao, tipo, valor) VALUES('%s','%s','%s','%f')" %(item.nome , item.descricao, item.tipo, item.valor);
  
  curInsert.execute(commandSql);
  
  id = curInsert.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curInsert.close();

  return idInserido;


insereItem(Item("Cafe", "Po de cafe 1kg ", "Alimento", 8.90));
insereItem(Item("Tang Laranja", "Suco de Laranja em pó marca Tang", "Alimento", 0.89));
insereItem(Item("Dell Inspiron", "Notebook da Dell", "Eletronico", 6999.90));
insereItem(Item("Controle XBOX", "Joystick do XBOX 360", "Eletronico", 199.90));
insereItem(Item("Agua", "garrafa com 2 litros de agua", "Alimento", 7.90));
insereItem(Item("Cha", "Pacotinho de Cha", "Alimento", 2.90));
insereItem(Item("Vassoura", "Vassoura para limpeza", "Limpeza", 29.90));
insereItem(Item("Esponja", "Esponja para lavar louca", "Limpeza", 3.90));

#==================================================== Exercicio 1 ================================================================================
#Complete a função que deve buscar o produto e retornar um objeto do tipo Produto
def encontraItemPorID(id:int) -> Item:
  cursor = conn.cursor()
  cursor.execute(f"SELECT  nome, descricao, tipo, valor FROM Itens WHERE id = {id}") 
  result= cursor.fetchone()
  cursor.close()
  if result:
    nome,descricao,tipo,valor=result
  return Item(nome,descricao,tipo,valor)

#==================================================== Exercicio 2 ================================================================================
#Esta função vai ser uma função de pesquisa de produtos por Tipo!!
# Arrume a função para a mesma buscar no banco os produtos baseado na coluna "tipo"
# E a mesma função deve preencher uma lista com os produtos encontrados e retornar a lista com os itens encontrados. 
# Como você pode observar está faltando bastante coisa nesta função, analise e complete a mesma para que ela passe nos testes.
def listarItensPorTipo(tipo:str) -> list[Item]:
  cursor = conn.cursor()
  cursor.execute(f"SELECT  nome, descricao, tipo, valor FROM Itens WHERE tipo = '{tipo}'")
  results=cursor.fetchall()
  cursor.close()
  produtos=[]
  for result in results:
    nome , descricao , tipo_produto , valor =result
    produtos.append(Item(nome , descricao , tipo_produto , valor ))
  #Retorna uma lista de objetos do tipo Cliente.
  return produtos; 

#==================================================== Exercicio 3 ================================================================================
#Esta função aqui vai fazer a soma dos valores de todos produtos por tipo. 
#Ela recebe como parametro o tipo, e retorna o valor somado dos produtos encontrados pelo tipo.
#Observe que a função tá vazia, tente completar ela corretamente para que a mesma funcione e os testes passem.
#Use exercicios anteriores como referência para acessar o banco, buscar os itens em lista, e somar cada um encontrado nesta lista
def somaValoresPorTipo(tipo:str) -> float:
  cursor= conn.cursor()
  cursor.execute(f"SELECT valor FROM Itens WHERE tipo = '{tipo}'")
  results= cursor.fetchall()
  total= 0.0
  ##Soma os valores dos produtos encontrados
  for result in results:
    valor = result[0]
    total += valor
  cursor.close()
  return total

#============================================================TESTES=====================================================================================

def test_validaEncontraItemPorID():

  item1 = encontraItemPorID(1);
  item2 = encontraItemPorID(3);
  item3 = encontraItemPorID(4);
  item4 = encontraItemPorID(5);

  assert item1.nome == "Cafe", f"Esperava encontrar o nome 'Cafe' mas encontrou {item1.nome}";
  assert item2.nome == "Dell Inspiron", f"Esperava encontrar o nome 'Dell Inspiron' mas encontrou {item2.nome}";
  assert item3.nome == "Controle XBOX", f"Esperava encontrar o nome 'Controle XBOX' mas encontrou {item3.nome}";
  assert item4.nome == "Agua", f"Esperava encontrar o nome 'Agua' mas encontrou {item4.nome}";

  return;

def test_validaListaItensPorTipo():

  alimentos = listarItensPorTipo("Alimento");
  eletronicos = listarItensPorTipo("Eletronico");
  limpeza = listarItensPorTipo("Limpeza");

  for a in alimentos:
    assert a.tipo == "Alimento", f"Erro no teste da litagem de Alimentos.. todos itens tem que ser do tipo Alimento";
  
  for e in eletronicos: 
    assert e.tipo == "Eletronico", f"Erro no teste de listagem de Eletronicos.. todos os itens tem que ser do tipo Eletronico";
  
  for l in limpeza:
    assert l.tipo == "Limpeza", f"Erro no teste de listagem de Limpeza.. todos os itens tem que ser do tipo Limpeza";
  
  return;

def test_somaValoresPorTipo():

  totalAlimentos = somaValoresPorTipo("Alimento");
  totalEletronicos = somaValoresPorTipo("Eletronico");
  totalLimpeza = somaValoresPorTipo("Limpeza");

  assert totalAlimentos >= 20.58 and totalAlimentos <= 20.60, f"Esperava encontrar o valor total de Alimentos de '20.59' porém encontrou {totalAlimentos}";
  assert totalEletronicos >= 7199.70 and totalEletronicos <= 7199.90, f"Esperava encontrar o valor total de Eletronicos de '7199.80' porém encontrou {totalEletronicos}";
  assert totalLimpeza >= 33.70 and totalLimpeza <= 33.90, f"Esperava encontrar o valor total de Limpeza de '33.80' porém encontrou {totalLimpeza}";

  return;


#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();