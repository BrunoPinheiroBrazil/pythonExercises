import sqlite3
import pytest

#Uma classe para o Objeto Usuario que precisamos.
class Livro:
  def __init__(self, autor:str, titulo:str, valor:int):
    self.autor = autor;
    self.titulo = titulo;
    self.valor = valor;

#Complete a criação da tabela para que a operação existente não dê erro!

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#1° Cria a tabela de carros com os campos 'id chave automatica, marca texto, modelo texto, cavalos inteiro' usando a variável 
#da conexão conn e um cursor igual os outros exercícios.
cur= conn.cursor()
cur.execute('''CREATE TABLE Livraria (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               autor TEXT NOT NULL,
               titulo TEXT NOT NULL, 
               valor INTEGER NOT NULL
            )''')


#2° Salva as alterações com commit. 
conn.commit()

#3° feche o cursor
cur.close()

#==================================================== Exercicio 1 ================================================================================
#Comando de inserção no banco que deverá passar e retornar o ID automatico. 
#Você deverá atualizar a variável commandSql com o comando para fazer a inserção do Livro no banco, 
#baseie-se nos exercícios anteriores.
def insereLivroNoBanco(livro:Livro):
  curUpdate = conn.cursor();  
  
  
  #Dica 1: Monte o comando SQL para inserir nesta variável igual outros exercícios estão fazendo.
  commandSql =f"""
      INSERT INTO Livraria (autor, titulo, valor)
      VALUES ('{livro.autor}', '{livro.titulo}', '{livro.valor}')
  """;
  curUpdate.execute(commandSql);
  
  id = curUpdate.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curUpdate.close();

  return idInserido;

#============================================================TESTES=====================================================================================

def test_validaInsereLivro():
  livro1 = Livro("Joan Lindsey", "Pincnik at Hanging Rock", 67);
  resposta = insereLivroNoBanco(livro1);
  livro2 = Livro("Edgar Allan Poe", "O Corvo", 199);
  resposta2 = insereLivroNoBanco(livro2);

  assert resposta == 1, f"Esperava encontrar o ID automatico '1' na resposta mas encontrou {resposta}"
  assert resposta2 == 2, f"Esperava encontrar o ID automatico '2' na resposta mas encontrou {resposta2}"

#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();