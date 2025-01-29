import sqlite3
import pytest


#Vamos pegar um exemplo de clientes para você entender melhor: 

#Primeiro criamos os dados
conn = sqlite3.connect(':memory:');

# Cria a tabela
cur = conn.cursor();
cur.execute('''CREATE TABLE Clientes
              (Nome text, CPF text, Idade integer, Genero text)''');

# Insere algumas linhas de dados no banco
cur.execute("""INSERT INTO Clientes VALUES 
            ('Fabian','00888820027',32,'M'),
            ('Bruno','00990930026',38,'M'),
            ('Pamela','89810030088',30,'F'),
            ('Eduardo','99934510024',45,'M'),
            ('Guilherme','80746971001',34,'M'),
            ('Jessica','03289302024',28,'F'),
            ('Mathias','46157777010',64,'M')""");

# Salva as alterações
conn.commit();

#==================================== Atualização Exemplo ===========================================================

#Criamos o Cursor, através da variável conn que é nossa variável de conexão com banco! 
curUpdate = conn.cursor();
  
#agora montamos a SQL query para atualizar um dado, no caso vamos atualizar a idade do Bruno para 39 anos agora:
commandSql = "UPDATE Clientes SET Idade = %i WHERE Nome = '%s'" %(39, "Bruno");

#Aqui nós mandamos o cursor executar o comando que montamos acima:
curUpdate.execute(commandSql);

#Importante sempre que vamos alterar dados do banco, temos que fazer o commit para atualizar o banco:
conn.commit();

#Por fim, fechamos o cursor que abrimos:
curUpdate.close();

#Agora para validar vou tentar achar os dados no banco de novo
cur = conn.cursor();

#Aqui estou tentando buscar a idade do cliente que se chama Bruno no banco:
cur.execute("SELECT Idade FROM Clientes WHERE Nome = 'Bruno'");

#Aqui estamos pegando 1 linha do retorno do cursor que abrimos. Após rodar o comando acima:
row = cur.fetchone();

#Agora vou jogar a coluna[0] do retorno da minha query de busca acima:
idadeEncontrada = row[0];

assert idadeEncontrada == 39 , f"Esperava encontrar a idade alterada do Bruno para '39' mas encontrou {idadeEncontrada}";

print("Encontrou a idade esperada! Teste passou!");

