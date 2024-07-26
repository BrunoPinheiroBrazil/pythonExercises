import pytest;

#A Aplicação é um código que valida de acordo com o input se o número de letras contidos na palavra é ímpar ou par.
#Escrever o código para validar se o número de letras na palavra é PAR ou Impar.
#Caso seja PAR, retornar a palavra "PAR" do contrário retornar a palavra "IMPAR". 

def validaPalavraParOuImpar(palavra:str):
 num_letras = len(palavra)
 if num_letras % 2 == 0:
    return "PAR"
 else:
    return "IMPAR";



















##Tests:
@pytest.mark.parametrize("test_input,expected", 
                         [
                            ("Mickey", "PAR"), 
                            ("Sonic", "IMPAR"), 
                            ("Eduardo", "IMPAR"),
                            ("Pateta", "PAR"),
                            ("Ovo", "IMPAR"),
                            ("ETERNAMENTE", "IMPAR"),
                            ("Tromboso", "PAR")
                         ])
def test_answer(test_input, expected):
    resposta = validaPalavraParOuImpar(test_input);
    assert resposta == expected, f"Esperava encontrar {expected}"