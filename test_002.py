#Identificar o que falta na função e arrumar ela. 
#O esperado é que a função que recebe um parâmetro, deverá utilizar este parâmetro para fazer um calculo. 
#exemplo, se receber a palavra "SOMA" no parametro operacao, ela vai fazer a soma dos parametros a e b, caso ela receba "SUB" 
#vai fazer a subração.

def funcOperacaoMatematica(operacao, a, b):
  resposta = 0;
  if operacao == "SOMA":
     resposta= a+b;
  else:
        resposta= a-b;
    
   
  return resposta;
















#Para rodar os testes precisa rodar este comando no terminal: pip install -U pytest. 
#Assim que o pyTest tiver instalado é só rodar o comando pytest no terminal.




##Tests:
def test_answer01():
  res = funcOperacaoMatematica("SOMA", 5, 10);
  assert(res) == 15, f'Esperava encontrar 15 e encontrou {res}';

def test_answer02():
  res = funcOperacaoMatematica("SUB", 9, 8);
  assert(res) == 1, f'Esperava encontrar 1 e encontrou {res}';

def test_answer03():
  res = funcOperacaoMatematica("SUB", 50, 12);
  assert(res) == 38, f'Esperava encontrar 38 e encontrou {res}';

def test_answer04():
  res = funcOperacaoMatematica("SOMA", 50, 50);
  assert(res) == 100, f'Esperava encontrar 100 e encontrou {res}';

def test_answer05():
  res = funcOperacaoMatematica("SOMA", 75, 125);
  assert(res) == 200, f'Esperava encontrar 200 e encontrou {res}';

def test_answer06():
  res = funcOperacaoMatematica("SUB", 800, 375);
  assert(res) == 425, f'Esperava encontrar 425 e encontrou {res}';