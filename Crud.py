import sqlite3


conexao = sqlite3.connect('escola.db')

cursor = conexao.cursor()

print(' conexão concluída')

cursor.execute('''

    CREATE TABLE IF NOT EXISTS alunos (
    
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT NOT NULL,

        idade INTEGER NOT NULL,

        email TEXT NOT NULL
    
    
    );

''')

'''
cursor.execute("INSERT INTO alunos ('nome','idade','email')VALUES (?,?,?)",('Lucas',15,'lucas2030@gmail.com'))
cursor.execute("INSERT INTO alunos ('nome','idade','email')VALUES (?,?,?)",('Julia',14,'Julia2090@gmail.com'))
cursor.execute("INSERT INTO alunos ('nome','idade','email')VALUES (?,?,?)",('Heloisa',17,'heloisa7080@gmail.com'))
cursor.execute("INSERT INTO alunos ('nome','idade','email')VALUES (?,?,?)",('Guilherme',14,'Guilherme7060@gmail.com'))
cursor.execute("INSERT INTO alunos ('nome','idade','email')VALUES (?,?,?)",('Kauan',15,'kauan1040@gmail.com')) 
'''
conexao.commit()

conexao.close()
'''---------------------------------------------------'''
conexao = sqlite3.connect('escola.db')


cursor = conexao.cursor()


consulta = cursor.execute("SELECT nome, idade, email FROM alunos")
print()

print("★-ALUNOS DA ESCOLA MIRAGE-★")

for lista in consulta.fetchall():

    print(f'''-----------------------

     ALUNO(A): {lista[0]} 

     IDADE: {lista[1]} 

     EMAIL: {lista[2]}
     -----------------------''') 

conexao.close()
'''-------------------------------------------------------'''
conexao = sqlite3.connect('escola.db')


cursor = conexao.cursor()

cursor.execute ("UPDATE alunos SET idade = ? WHERE  id = ?" , ('16' , 4))
conexao.commit()
conexao.close()
'''------------------------------------------------------------'''
conexao = sqlite3.connect('escola.db')


cursor = conexao.cursor()

cursor.execute ("DELETE FROM alunos WHERE id = ?" , (3,))
conexao.commit()
conexao.close()
