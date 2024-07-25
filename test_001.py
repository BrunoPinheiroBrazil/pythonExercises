#Identificar o que esta errado na função somaLetraA e arrumar para que os testes passem:
def funcaoSomaLetraA(palavra) :
   resposta = 0;
   for letra in palavra:
     if letra == 'A':
      resposta += 1
   return resposta;






























##Tests:
def test_answer01():
  res1 = funcaoSomaLetraA("ABABA");
  assert(res1) == 3, f'Esperava encontrar 3 e encontrou {res1}';

def test_answer02():
  res2 = funcaoSomaLetraA("CDEFG");
  assert(res2) == 0, f'Esperava encontrar 0 e encontrou {res2}';

def test_answer03():
  res3 = funcaoSomaLetraA("MAR");
  assert(res3) == 1, f'Esperava encontrar 1 e encontrou {res3}';

def test_answer04():
  res4 = funcaoSomaLetraA("DIVULGAR");
  assert(res4) == 1, f'Esperava encontrar 1 e encontrou {res4}';
