import sqlite3
import pytest

#Uma classe para o Objeto Usuario que precisamos.
class Usuario:
  def __init__(self, apelido:str, nome:str, idade:int):
    self.apelido = apelido;
    self.nome = nome;
    self.idade = idade;

class Resposta:
  def __init__(self, nomeUsuarioInserido:str, id:int):
    self.nomeUsuarioInserido = nomeUsuarioInserido;
    self.id = id;

#Cria a conexão no banco no inicio
conn = sqlite3.connect(':memory:');

# Cria a tabela de usuarios
cur = conn.cursor();
cur.execute('''CREATE TABLE Usuario
              (Id INTEGER PRIMARY KEY, Apelido varchar(15), Nome varchar(50), Idade INTEGER)''');

# Salva as alterações
conn.commit();

#fecha o cursor
cur.close();


#==================================================== Exercicio 1 ================================================================================
#Siga o passo a passo para otimizar a função. A mesma deverá validar os dados do usuário inserido. 
def insereUsuario(usuario:Usuario):

  #1º Deverá validar se o apelido é maior que 15 caracteres. Caso seja maior deverá lançar exception.
  #   A mensagem de erro deverá conter -> 'apelido ultrapassou o limite de tamanho!'
  if len(usuario.apelido)>15:
    raise Exception('apelido ultrapassou o limite de tamanho!')

  #2º A Idade não pode ser maior que 99 anos. Caso a idade seja maior que 99 anos, deverá lançar exception.
  #  A mensagem de erro deverá conter -> "idade não pode ser maior que 99 anos"
  if usuario.idade>99:
    raise Exception('idade não pode ser maior que 99 anos')

  #3º O nome não pode conter números ou caracteres especiais, tais como @$%¨& e assim por diante. Só letras e espaço. 



  #4° Com tudo validado acima, a função deverá chamar a função de banco que vai criar o usuário no banco! 
  #   Esta função que cria o usuário no banco, retorna o "ID" do funcionário criado. Guarde este ID em uma variável. 
  id_inserido=insereUsuarioNoBanco(usuario)

  #5° Deverá preencher classe 'Resposta' definida acima para o return.  
  #   Crie uma variável do tipo Resposta.
  #   A classe resposta tem os campos nomeUsuarioInserido e id. 
  #   nomeUsuarioInserido será o nome do usuário.
  #   id será o ID retornado na função do banco. 
  #   Preencha estes dois campos da variável resposta e retorne ela. 
  resposta= Resposta (nomeUsuarioInserido=usuario.nome, id=id_inserido)
  return resposta





#=========================================================== Funções prontas ============================================================
def insereUsuarioNoBanco(usuario:Usuario):
  curUpdate = conn.cursor();
  commandSql = "INSERT INTO Usuario(Apelido, Nome, Idade) VALUES('%s','%s','%i')" %(usuario.apelido , usuario.nome, usuario.idade);
  curUpdate.execute(commandSql);
  
  id = curUpdate.lastrowid;
  
  idInserido:int=0;

  if(id != None):
    idInserido = id;
  
  curUpdate.close();

  return idInserido;



#==========================================================TESTES====================================================================
def test_validaOperacoesUsuarioJosiasMatador():
  usuario = Usuario("Matador", "Josias de Melo", 18);
  resposta = insereUsuario(usuario);

  assert resposta.nomeUsuarioInserido == "Josias de Melo", f"Esperava encontrar 'Josias de Melo' na resposta mas encontrou {resposta.nomeUsuarioInserido}"

  usuario1 = buscaUsuarioNoBanco(resposta.id);

  assert usuario1.apelido == "Matador", f"Esperava encontrar o usuario 'Matador' inserido no banco mas encontrou {usuario1.apelido}";

def test_validaOperacoesUsuarioMathiasLouco():
  usuario = Usuario("Louco", "Mathias Silva", 18);
  resposta = insereUsuario(usuario);

  assert resposta.nomeUsuarioInserido == "Mathias Silva", f"Esperava encontrar 'Mathias Silva' na resposta mas encontrou {resposta.nomeUsuarioInserido}"

  usuario1 = buscaUsuarioNoBanco(resposta.id);

  assert usuario1.apelido == "Louco", f"Esperava encontrar o usuario 'Louco' inserido no banco mas encontrou {usuario1.apelido}";

def test_idadeMaiorQue99():
  with pytest.raises(Exception) as info_da_exceptionFabian:
    usuarioBugado = Usuario("Madruga", "Fabian Mohr", 145);
    insereUsuario(usuarioBugado);
  
  assert 'idade não pode ser maior que 99 anos' in info_da_exceptionFabian.value.args[0].lower(), f"A Exception tem que conter uma mensagem contendo 'idade não pode ser maior que 99 anos'"

def test_apelidoMuitoGrande():
  with pytest.raises(Exception) as info_da_exceptionFabian:
    usuarioBugado = Usuario("EuSouLoucoDeMaisEMuitoDoidoDoidoDoidoDoidoDoido", "Bruno Brazil", 38);
    insereUsuario(usuarioBugado);
  
  assert 'apelido ultrapassou o limite de tamanho!' in info_da_exceptionFabian.value.args[0].lower(), f"A Exception tem que conter uma mensagem contendo 'apelido ultrapassou o limite de tamanho!'"


#Função auxiliar para eu validar se o Usuario foi criado com sucesso. 
def buscaUsuarioNoBanco(id:int):

  cur = conn.cursor();
  cur.execute("SELECT Apelido, Nome, Idade FROM Usuario WHERE Id = '%i'" % id);
  
  row = cur.fetchone();

  #Se não encontrou nada, retorna um usuário vazio!
  if(len(row)==0):
    return Usuario("Nada","Nada",0);

  apelido = row[0];
  nome = row[1];
  idade = row[2];

  usuario = Usuario(apelido, nome, idade);
  return usuario;

#Função que roda quando todos testes terminarem. 
def pytest_sessionfinish(session, exitstatus):
  #Encerra conexão quando termina os testes.
  conn.close();