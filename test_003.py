#Arrumar a função que deverá identificar se as letras de uma palavra estão contidas nas frases que serão passadas 
#como parâmetro nos testes. Caso a palavra exista na frase deverá retornar True, do contrário retornará False. 

def funcaoContemPalavra(texto, palavra):
    texto_modificado = texto.replace('-', ' ')
    palavra_texto = texto_modificado.split()
    if palavra in palavra_texto:
        return True
    else:
        return False












##Tests:
def test_answer01():
  res = funcaoContemPalavra("era uma vez", "vez");
  assert(res) == True, f'Esperava encontrar True e encontrou {res}';

def test_answer02():
  res = funcaoContemPalavra("o gato roeu a roupa do rei de roma", "gema");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';

def test_answer03():
  res = funcaoContemPalavra("eu gosto de jogar video-game", "video");
  assert(res) == True, f'Esperava encontrar True e encontrou {res}';

def test_answer04():
  res = funcaoContemPalavra("matilda tem uma vassoura", "uma");
  assert(res) == True, f'Esperava encontrar True e encontrou {res}';


def test_answer05():
  res = funcaoContemPalavra("a garota gostava de usar batom", "garoto");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';

def test_answer06():
  res = funcaoContemPalavra("sonic corre rapido demais", "correu");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';


def test_answer07():
  res = funcaoContemPalavra("calculos sao muito dificeis", "muitos");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';


def test_answer08():
  res = funcaoContemPalavra("havia muitos carros na rua", "carro");
  assert(res) == False, f'Esperava encontrar False e encontrou {res}';