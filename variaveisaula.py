#Uma classe para o Objeto Usuario que precisamos.
class Produto:
  def __init__(self, nome:str, descricao:str, tipo:str, valor:float):
    self.nome = nome;
    self.descricao = descricao;
    self.tipo = tipo;
    self.valor = valor;

produtosonic = Produto("Sonic", "Personagem de Jogo", "Video Game", 0.50);
produtosonic2 = Produto("Sonic 2", "Personagem de Jogo", "Video Game", 7.00);
produtosonic3 = Produto("Sonic 3", "Personagem de Jogo", "Video Game", 8.00);
produtosonic4 = Produto("Sonic 4", "Personagem de Jogo", "Video Game", 1000.00);
produtosonic5 = Produto("Sonic 5", "Personagem de Jogo", "Video Game", 0.08); 

produtosSonic = [
    Produto("Sonic", "Personagem de Jogo", "Video Game", 0.8880),
    Produto("Sonic 2", "Personagem de Jogo", "Video Game", 2000.00),
    Produto("Sonic 3", "Personagem de Jogo", "Video Game", 3000.00),
    Produto("Sonic 4", "Personagem de Jogo", "Video Game", 4000.00),
    Produto("Sonic 5", "Personagem de Jogo", "Video Game", 5000.00),
    Produto("Sonic 6", "Personagem de Jogo", "Video Game", 6000.00),
    Produto("Sonic 7", "Personagem de Jogo", "Video Game", 7000.00),
    Produto("Sonic 8", "Personagem de Jogo", "Video Game", 8000.00),
    Produto("Sonic 9", "Personagem de Jogo", "Video Game", 9000.00),
    Produto("Sonic 10", "Personagem de Jogo", "Video Game", 10000.00),
]


totalvalores= 0.00;
totalvalores = produtosonic.valor + produtosonic2.valor + produtosonic3.valor + produtosonic4.valor + produtosonic5.valor;
print("total de valores calculados na mao: ", totalvalores);

totalvaloreslista = 0.00;
for produto in produtosSonic:
    totalvaloreslista += produto.valor;
print("total de valores calculados na lista: ", totalvaloreslista);





def calcular_total_produtos(produtos):
    total = 0.00
    for produto in produtos:
        total += produto.valor
    return total


# Exemplo de uso da função
total_valores = calcular_total_produtos(produtosSonic);
print("Total de valores calculados na lista com a função: ", total_valores);
# Função para calcular o total de valores dos produtos



#tema criar uma função que recebe uma lista e retorna a média dos valores dos produtos.