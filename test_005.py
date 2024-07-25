#A aplicação é um motor de crédito! Que vai avaliar se o usuário está com alguma pendência de crédito. 
#Caso o usuário esteja com uma pendêndia de crédito vai impedir a compra. Caso o usuário não tenha pendência
#A transação irá continuar e avaliar se o usuário tem quantia suficiente para deduzir a compra no cartão. 
#Passo a passo da operação:
#1 - Inicia transação da compra onde é passado o produto desejado, e o nome do usuário
#2 - O sistema avalia se o usuário tem pendência, caso tiver, já retorna Falso para compra.
#3 - Caso o usuário não tenha pendência a transação continua para a avaliação de quantia de crédito do usuário
#4 - O Sistema busca os dados de crédito do usuário pelo nome e guarda em uma variável
#5 - Caso o usuário tenha crédito suficiente, o sistema busca o valor do produto passado e guarda em uma variável.
#6 - O sistema calcula se o usuário tem crédito suficiente para compra do produto, se tiver, retorna True, senão False.

def pegaPendenciaUsuario(usuario:str):
  return pendenciaUsuarios.get(usuario);

#passo 1
def Transacao_Compra(usuario:str, produto:str):
  if usuario not in pendenciaUsuarios or usuario not in creditosUsuarios:
    return False
  if produto not in valoresProdutos:
    return False
  #passo 2 e 3
  pendencia = pegaPendenciaUsuario(usuario);
  if(pendencia == "Pendencia"):
    return False;
  
  #passo 
  creditoUsuario = pegaCreditoUsuario(usuario)
  
  #passo 5
  valorDeProduto = pegaValorProduto(produto)
 
  #valorDeProduto = produto
  #Faça o cálculo necessário do passo 6 usando as variáveis acima. 
  
  if creditoUsuario >= valorDeProduto:
    return True
  else:
    return False












def pegaValorProduto(produto:str):
  return valoresProdutos[produto];

def pegaCreditoUsuario(usuario:str):
  return creditosUsuarios[usuario];

#Tabela fake para persistir a pendencia dos usuarios
pendenciaUsuarios = {
  "Sonic": "Sem Pendencia",
  "Mickey": "Pendencia",
  "Pato": "Pendencia",
  "Vacilo": "Sem Pendencia"
}

valoresProdutos = {
  "Computador": 2500,
  "Mouse": 50,
  "Teclado": 120,
  "Carro": 15000
}

creditosUsuarios = {
  "Sonic": 1000,
  "Mickey": 50000,
  "Pato": 10000,
  "Vacilo": 50
}



##Tests:
def test_answer01():
  res = Transacao_Compra("Mickey", "Computador");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';

def test_answer02():
  res = Transacao_Compra("Sonic", "Mouse");
  assert(res) == True, f'Esperava encontrar True e encontrou {res}';


def test_answer03():
  res = Transacao_Compra("Pato", "Teclado");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';

def test_answer04():
  res = Transacao_Compra("Sonic", "Teclado");
  assert(res) == True, f'Esperava encontrar True e encontrou {res}';

def test_answer05():
  res = Transacao_Compra("Vacilo", "Mouse");
  assert(res) == True, f'Esperava encontrar True e encontrou {res}';

def test_answer06():
  res = Transacao_Compra("Vacilo", "Carro");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';

def test_answer07():
  res = Transacao_Compra("Sonic", "Carro");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}'

def test_answer08():
  res = Transacao_Compra("dudu", "Carro")
  assert(res) == False, f'Esperava encontrar False e encontrou {res}'

def test_answer09():
  res = Transacao_Compra("Sonic", "mercedez")
  assert(res) == False, f'Esperava encontrar False e encontrou {res}'