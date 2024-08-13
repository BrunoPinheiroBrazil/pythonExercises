import sqlite3
import pytest

#Uma classe para o Objeto Usuario que precisamos.
class Carro:
  def __init__(self, marca:str, modelo:str, cavalos:int):
    self.marca = marca;
    self.modelo = modelo;
    self.cavalos = cavalos;

class Resposta:
  def __init__(self, carro:Carro, id:int):
    self.carro = carro;
    self.id = id;


#==================================================== Exercicio 1 ================================================================================
#Complete a criação da tabela para que a operação existente não dê erro!

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#1° Cria a tabela de carros com os campos 'id chave automatica, marca texto, modelo texto, cavalos inteiro' usando a variável 
#da conexão conn e um cursor igual os outros exercícios.



#2° Salva as alterações com commit. 



#3° feche o cursor



#============================================================TESTES=====================================================================================
#Comando de inserção no banco que deverá passar e retornar o ID automatico. 
def insereCarroNoBanco(carro:Carro):
  curUpdate = conn.cursor();
  commandSql = "INSERT INTO Carros(marca, modelo, cavalos) VALUES('%s','%s','%i')" %(carro.marca , carro.modelo, carro.cavalos);
  curUpdate.execute(commandSql);
  
  id = curUpdate.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curUpdate.close();

  resposta = Resposta(carro, idInserido);

  return resposta;


def test_validaInsereCarro():
  carro1 = Carro("Ford", "Ka", 92);
  resposta = insereCarroNoBanco(carro1);
  carro2 = Carro("RENAULT", "LOGAN", 102);
  resposta2 = insereCarroNoBanco(carro2);

  assert resposta.id == 1, f"Esperava encontrar o ID automatico '1' na resposta mas encontrou {resposta.id}"
  assert resposta2.id == 2, f"Esperava encontrar o ID automatico '2' na resposta mas encontrou {resposta2.id}"

#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();