import time;

tempoTimer = 1;

#Identificar o que esta errado na função somaLetraA e arrumar para que os testes passem:
def funcaoSomaLetraA(palavra) :
  resposta = 0;
  for letra in palavra:
    if letra == 'A':
      resposta+=1;
   
  return resposta;



#Para rodar os testes abra o Terminal abaixo e rode o comando python -m exercicio01 -cov




























##Testes:
res1 = funcaoSomaLetraA("ABABA");
res2 = funcaoSomaLetraA("CDEFG");
res3 = funcaoSomaLetraA("MAR");
res4 = funcaoSomaLetraA("DIVULGAR");

print("Rodando testes");
time.sleep(tempoTimer);

assert(res1) == 3, f'Esperava encontrar 3 e encontrou {res1}';
print(f"Teste 1 passou!");
time.sleep(tempoTimer);

assert(res2) == 0, f'Esperava encontrar 0 e encontrou {res2}';
print(f"Teste 2 passou!");
time.sleep(tempoTimer);

assert(res3) == 1, f'Esperava encontrar 1 e encontrou {res3}';
print(f"Teste 3 passou!");
time.sleep(tempoTimer);

assert(res4) == 1, f'Esperava encontrar 1 e encontrou {res4}';
print(f"Teste 4 passou!");
time.sleep(tempoTimer);