import sqlite3
import pytest

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#A aplicação irá buscar dados no banco que criei em memória! 
#Arrumar a função para que a mesma retorne o Preço do jogo, a quantidade e o nome do jogo na ordem. 
#1° Se não passar o nome do jogo, deve lançar exceção igual o Eduardo ensinou! 
#2° Na Exception lançada deve conter o texto "Nome faltando!"
#3° A função deve passar a variável nomeGame para o método interno do banco buscaGameNoBanco.
def buscaGame(nomeGame:str):
  if not nomeGame:
    raise Exception ('Nome faltando!');
  game = Jogo("","",0,0);
  game= buscaGameNoBanco(nomeGame)
  return game;















#Uma classe para o Objeto que precisamos.
class Jogo:
  def __init__(self, lancamento:str, titulo:str, valor:float, quantidade:int):
    self.lancamento = lancamento;
    self.titulo = titulo;
    self.valor = valor;
    self.quantidade = quantidade;


def buscaGameNoBanco(titulo:str):
  #Cria um cursor para interagir com o banco
  cur = conn.cursor();
  cur.execute("SELECT * FROM Games WHERE Titulo = '%s'" % titulo);

  #Preenche os dados do Game encontrado no banco
  row = cur.fetchone();
  if row is None:
    raise Exception('Jogo não encontrado')
  tituloEncontrado = row[1];
  quantidadeEncontrada = row[2];
  valorEncontrado = row[3];
  dataLancamento = row[0];
  
  #Cria uma variável do tipo "JOGO"
  game = Jogo(dataLancamento, tituloEncontrado, valorEncontrado, quantidadeEncontrada);

  #Retorna a variavel do tipo JOGO.
  return game;

#TESTES!
def test_validaGames():
  # Cria a tabela
  cur = conn.cursor();
  cur.execute('''CREATE TABLE Games
                (Lancamento text, Titulo text, Quantidade real, Valor real)''');

  # Insere as 3 linhas no banco
  cur.execute("INSERT INTO Games VALUES ('2006-01-05','Sonic',10,99.99)");
  cur.execute("INSERT INTO Games VALUES ('2001-02-05','Silent',5,199.99)");
  cur.execute("INSERT INTO Games VALUES ('1999-01-20','Metal Gear',1,399.99)");
  cur.execute("INSERT INTO Games VALUES ('1997-12-24','Parasite',1,499.99)");

  # Salva as alterações
  conn.commit();

  game1 = buscaGame("Sonic");
  game2 = buscaGame("Silent");
  game3 = buscaGame("Metal Gear");
  game4 = buscaGame("Parasite");

  with pytest.raises(Exception) as info_da_exception:
    buscaGame("");
  
  assert info_da_exception.value.args[0] == 'Nome faltando!', f"A Exception tem que conter uma mensagem dizendo 'Nome faltando!'"
  
  assert game1.valor == 99.99, f"Esperava encontrar 99.99 mas encontrou {game1.valor}"
  assert game2.valor == 199.99, f"Esperava encontrar 199.99 mas encontrou {game2.valor}"
  assert game3.valor == 399.99, f"Esperava encontrar 399.99 mas encontrou {game3.valor}"
  assert game4.valor == 499.99, f"Esperava encontrar 499.99 mas encontrou {game4.valor}"

  #Encerra conexão quando termina os testes.
  conn.close();