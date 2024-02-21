import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#exercicio 1
cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#exercicio 2
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "JESSICA", 31, "SISTEMAS DE INFORMAÇÃO")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "MARIA", 30, "ADMINISTRAÇÃO")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "JUDITE", 20, "CIÊNCIAS DA COMPUTAÇÃO")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "JULIO", 33, "ENGENHARIA")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "THAMIRES", 19, "DIREITO")')

#exercicio3
#a)
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados:
    print(alunos)

#b)
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for alunos in dados:
    print(alunos)   
 
#c)
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "ENGENHARIA" ORDER BY nome DESC')
for alunos in dados:
    print(alunos)

#d)
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in dados:
    print(alunos)

#exercicio 4
#a)
cursor.execute('UPDATE alunos SET idade = 18 WHERE id = 1')

#b)
cursor.execute('DELETE FROM alunos WHERE id = 3')

#exercicio 5
cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo DECIMAL(18,2))')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "JOAO APARECIDO", 55 , 50000)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "MARIA JOSE", 60 , 15000)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "PEDRO ZAMARIAN", 82 , 20000)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "JULIO FREITAS", 40 , 3500)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "ANA JULIA AMORIM", 35 , 850)')

#exercicio 6
#a)
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for clientes in dados:
    print(clientes)

#b)
dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
for clientes in dados:
    print(clientes)

#c)
dados = cursor.execute('SELECT MAX(saldo),* FROM clientes')
for clientes in dados:
    print(clientes)

#d)
dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
for clientes in dados:
    print(clientes)

#7)
#a)
cursor.execute('UPDATE clientes SET saldo = 28500 WHERE id = 4')

#b)
cursor.execute('DELETE FROM clientes WHERE id = 3')

#8)
cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT FOREKEY REFERENCES clientes(id), produto VARCHAR(100), valor DECIMAL(18,2))')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 2, "DESKTOP ABC123" , 2500.89)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 5, "NOTEBOOK SAMSUNG XYZ" , 3765.99)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 1, "MOUSE LOGITECH BLUETOOTH" , 245.99)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 2, "TECLADO SEM FIO DELL" , 159.78)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (5, 3, "TABLET SAMSUNG MM3E" , 459.77)')

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for compras_clientes in dados:
    print(compras_clientes)

conexao.commit()
conexao.close