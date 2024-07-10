'''
Tarefa 1:   Explicar o que a f1 está fazendo e dar o nome correto a ela
Tarefa 2:   Escrever a mesma funcão, porém de uma maneira mais "pythonica"
            Dica, da pra escrever em uma linha :)
'''
def f1(str:str) -> bool:
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

def test_1():
    assert(f1("ana")) == True

def test_2():
    assert(f1("teste")) == False

def test_3():
    assert(f1("malayalam")) == True

def test_4():
    assert(f1("malayalam")) == True