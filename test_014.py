import sqlite3
import pytest

#Uma classe para o Objeto Usuario que precisamos.
class Apartamento:
  def __init__(self, condominio:str, bloco:str, andar:int, proprietario:str):
    self.condominio = condominio;
    self.bloco = bloco;
    self.proprietario = proprietario;
    self.andar = andar;

#Complete a criação da tabela para que a operação existente não dê erro!

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

#1° Cria a tabela de carros com os campos 'id chave automatica, marca texto, modelo texto, cavalos inteiro' usando a variável 
#da conexão conn e um cursor igual os outros exercícios.
cur= conn.cursor()
cur.execute('''CREATE TABLE Apartamentos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               condominio TEXT NOT NULL,
               bloco TEXT NOT NULL, 
               proprietario TEXT NOT NULL,
               andar INTEGER NOT NULL
            )''')


#2° Salva as alterações com commit. 
conn.commit()

#3° feche o cursor
cur.close()

def insereApartamentoNoBanco(apartamento:Apartamento):
  curInsert = conn.cursor();  

  commandSql = "INSERT INTO Apartamentos(condominio, bloco, andar, proprietario) VALUES('%s','%s','%i','%s')" %(apartamento.condominio , apartamento.bloco, apartamento.andar, apartamento.proprietario);
  
  curInsert.execute(commandSql);
  
  id = curInsert.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curInsert.close();

  return idInserido;

#==================================================== Exercicio 1 ================================================================================
#Comando para atualizar um apartamento, deve usar o "ID" como referência para atualizar os dados do apartamento.
#Pesquise por conta e tente entender como fazer um UPDATE (Atualização) no SQL. Tente montar a query para que seja feito a atualização
#O comando Update é parecido com o INSERT, a diferença é que você precisa montar ele com base no que precisa de dados para identificar o que precisa ser atualizado.
#Analise o arquivo SqlUpdateExemplo.
def atualizaProprietario(id:int, novoProprietario:str):
  
  curUpdate = conn.cursor();
  
  commandSql = "";

  curUpdate.execute(commandSql);

  conn.commit();

  cur.close();

def  buscaApartamentoNoBancoPeloID(id:int) -> Apartamento:

  cur = conn.cursor();
  cur.execute("SELECT condominio, bloco, andar, proprietario FROM Apartamentos WHERE Id = '%i'" % id);
  
  row = cur.fetchone();

  #Se não encontrou nada, retorna um usuário vazio!
  if(len(row)==0):
    return Apartamento("","",0,"");

  condominio = row[0];
  bloco = row[1];
  andar = row[2];
  proprietario = row[3];

  apartamento = Apartamento(condominio,bloco, andar, proprietario);
  return apartamento;


#============================================================TESTES=====================================================================================

def test_validaInsereLivro():
  respostas = [];
  respostas.append(insereApartamentoNoBanco(Apartamento("Villa di Cremona", "F", 201, "Mickey")));
  respostas.append(insereApartamentoNoBanco(Apartamento("Villa di Cremona", "F", 305, "Vacilo")));
  respostas.append(insereApartamentoNoBanco(Apartamento("Villa di Cremona", "E", 101, "Mulher Chata")));
  respostas.append(insereApartamentoNoBanco(Apartamento("Villa di Cremona", "D", 105, "Amigo do Cachorro")));

  atualizaProprietario(1, "Sonic");
  atualizaProprietario(2, "Mickey");
  atualizaProprietario(3, "Vacilo");
  atualizaProprietario(4, "Pato");

  ap1 = buscaApartamentoNoBancoPeloID(1);
  ap2 = buscaApartamentoNoBancoPeloID(2);
  ap3 = buscaApartamentoNoBancoPeloID(3);
  ap4 = buscaApartamentoNoBancoPeloID(4);

  assert ap1.proprietario == "Sonic", f"Esperava encontrar o proprietário 'Sonic' mas encontrou {ap1.proprietario}"
  assert ap2.proprietario == "Mickey", f"Esperava encontrar o proprietário 'Mickey' mas encontrou {ap2.proprietario}"
  assert ap3.proprietario == "Vacilo", f"Esperava encontrar o proprietário 'Vacilo' mas encontrou {ap3.proprietario}"
  assert ap4.proprietario == "Pato", f"Esperava encontrar o proprietário 'Pato' mas encontrou {ap4.proprietario}"

#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();