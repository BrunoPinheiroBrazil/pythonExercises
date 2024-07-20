'''
Tarefa 1:   Explicar o que a f1 está fazendo e dar o nome correto a ela
Resposta Tarefa 1: linha 8 é um laço for vc fez com que ele fosse ate a metade e depois no outro ele so verifica se a outra  metade e =.
na linha 10: ele verifica se a posição 0 e = a ultima se nao for ela da flse e para da true e necessario fazer todo o loop verificando se todos os caracteris são iguais. 
Tarefa 2:   Escrever a mesma funcão, porém de uma maneira mais "pythonica"
            Dica, da pra escrever em uma linha :)
Resposta Tarefa 2: fiz oq vc  me pediu coloquei em uma unica linha demorei um pouco mais que o previsto pq estava dando erro ai fui atras de pesquisar tudo oque poderia ser.
 Tudo que esta dentro do [] faz com que inverta a sequencia como uma string. explicando melhor o str==str[::-1] verifica se é igula a stringui  é igual a sua versão invertida.
 Tudo isso e possivel pq em python se utiliza funcionalidades internas otimizando o python como operaçoes como strings.
'''
def f1(str:str) -> bool:
   return str == str[::-1]
def test_1():
    assert(f1("ana")) == True

def test_2():
    assert(f1("teste")) == False

def test_3():
    assert(f1("malayalam")) == True

def test_4():
    assert(f1("malayalam")) == True