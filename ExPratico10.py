# Elabore um banco de dados e implemente dados de um setor de logística de bebidas.
# A tabela deve possuir os campos código, marca da bebida, tipo da bebida, data de validade,
# indicação se é alcóolico ou não (boolenao) e o preço. Os dados devem ser preenchidos do teclado.
# O seu código deve ter as operações de CRUD, tradicionais em BD

import sqlite3

def inserir(marca, tipo, datavalidade, alcoolico, preco ):
    print(marca,"\n", tipo,"\n", datavalidade,"\n", alcoolico,"\n", preco,"\n")
    tabela.execute("""
                    INSERT INTO logistica(marca, tipo, datavalidade, alcoolico, preco)
                    VALUES (?,?,?,?,?)
                    """, (marca, tipo, datavalidade,alcoolico, preco)
                   )
    print("Valores inseridos com sucesso !")
    connection.commit()

def consulta(cons):
    if cons ==1:
        template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
        templatelinha= "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
        for i in tabela.execute("""SELECT * FROM logistica ORDER BY marca """):
            print(templatelinha.format(*i))
        print("\n")

    elif cons == 2:
        template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
        templatelinha = "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
        for i in tabela.execute("""SELECT * FROM logistica ORDER BY tipo """):
            print(templatelinha.format(*i))
        print("\n")

    elif cons == 3:
        template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
        templatelinha = "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
        for i in tabela.execute("""SELECT * FROM logistica ORDER BY datavalidade """):
            print(templatelinha.format(*i))
        print("\n")

    elif cons == 4:
        template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
        templatelinha = "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
        for i in tabela.execute("""SELECT * FROM logistica ORDER BY alcoolico """):
            print(templatelinha.format(*i))
        print("\n")

    elif cons == 5:
        template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
        templatelinha = "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
        for i in tabela.execute("""SELECT * FROM logistica ORDER BY preco """):
            print(templatelinha.format(*i))
        print("\n")

    elif cons == 6:
        template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
        templatelinha = "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
        for i in tabela.execute("""SELECT * FROM logistica ORDER BY marca """):
            print(templatelinha.format(*i))
        print("\n")

    elif cons == 7:
        sql_search = "SELECT * FROM logistica WHERE marca = ?"
        templatelinha = "{0:^6} | {1:12} | {2:13} | {3:^9} | {4:^10} | R${5:^5}"
        for i in tabela.fetchall():
            print(i)
        for i in tabela.execute(sql_search, [(input("Digite a marca da bebida: "))]):
            template = "{0:<5} | {1:^12} | {2:13} | {3:<9} | {4:>10} | {5:>8} "
            print(template.format("CODIGO", "MARCA", "TIPO", "VALIDADE", "ALCOOLICO", "PREÇO"))
            print(templatelinha.format(*i))


        #print(tabela.fetchall())
        print("Operação realizada com sucesso !\n")

def atualizar():
    atua=int(input("Digite uma escolha para atualizar: \nMarca [1] - Tipo[2] - Validade[3] - Alcoolico[4] - Preço[5] - Troca tudo [6]"))
    if atua == 1:
        id = int(input("Digite o Codigo da Bebida: "))
        tabela.execute("""UPDATE logistica SET marca = ? WHERE codigo = ?""", (input("Digite a nova marca do produto: "), id))
        connection.commit()
        print("Operação feita com sucesso !")

    if atua == 2:
        id = int(input("Digite o Codigo da Bebida: "))
        tabela.execute("""UPDATE logistica SET tipo = ? WHERE codigo = ?""", (input("Digite o novo tipo do produto: "), id))
        connection.commit()
        print("Operação feita com sucesso !")

    if atua == 3:
        id = int(input("Digite o Codigo da Bebida: "))
        tabela.execute("""UPDATE logistica SET datavalidade = ? WHERE codigo = ?""", (input("Digite a nova validade do produto: "), id))
        connection.commit()
        print("Operação feita com sucesso !")

    if atua == 4:
        id = int(input("Digite o Codigo da Bebida: "))
        tabela.execute("""UPDATE logistica SET marca = ? WHERE alcoolico = ?""", (input("Digite a nova alcoolismo do produto - [0]Não - [1] Sim: "), id))
        connection.commit()
        print("Operação feita com sucesso !")

    if atua == 5:
        id = int(input("Digite o Codigo da Bebida: "))
        tabela.execute("""UPDATE logistica SET marca = ? WHERE preco = ?""", (input("Digite o novo preço do produto: "), id))
        connection.commit()
        print("Operação feita com sucesso !")

    if atua == 6:
        id = int(input("Digite o Codigo da Bebida: "))
        tabela.execute("""UPDATE logistica SET marca = ? , tipo = ? , datavalidade = ?, alcoolico = ?, preco =? 
                        WHERE codigo = ?""",
                       (input("Digite a nova marca do produto: "),
                        (input("Digite o novo tipo do produto: ")),
                        (input("Digite a nova validade do produto: ")),
                        (input("Alcoolico [0]Não - [1]Sim : ")),
                        input("Digite o preço: "),id))

        connection.commit()
        print("Operação feita com sucesso !")

def deletar(delet):
    tabela.execute("""DELETE FROM logistica WHERE codigo = ?""", str(delet))
    connection.commit()
    print("Operação feita com sucesso !")

#Criando arquivo bd
connection = sqlite3.connect("bebidas")
tabela = connection.cursor()

# Criando a tabela
#tabela.execute("""CREATE TABLE logistica (
#    codigo  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#    marca TEXT NOT NULL,
#    tipo TEXT NOT NULL,
#    datavalidade DATE,
#    alcoolico BOOL,
#    preco REAL
#    );
#    """)

# Menu
op=int(1)
while op!=0:
    op = int(input("Selecione uma opção: \n[1] Cadastro de bebidas \n[2]Consulta \n[3]Atualizar \n[4]Deletar \n[0]Para sair\n"))

    #Cadastro
    if op==1:
        reg =1
        while reg!=0:
            print("#"*20, "CADASTRO DE BEBIDAS", "#"*20)
            marca = input("Digite a marca da bebida: ")
            tipo = input("Digite o tipo da bebida: ")
            datavalidade = input("Digite a validade: ")
            alcoolico = bool(input("Digite se é alcoolica: [0]Não - [1]Sim"))
            preco = float(input("Digite o preço: R$\n"))

            inserir(marca, tipo, datavalidade, alcoolico, preco)
            reg=int(input("Para sair digite [0], para continuar o cadastro qualquer outro numero: "))

    #Consulta
    elif op==2:
        cons = 1
        while cons!=0 and cons<=6:
            cons=int(input("Consulte por: [1]Marca - [2]Tipo - [3]Validade - [4]Alcoolica - [5]Preço - [6]Codigo - [7]Por nome - [0]Para retornar"))
            consulta(cons)

    #Atualizar dados
    elif op==3:
        atu =1
        print("Selecione o ID a ser alterado: ")
        exibir = tabela.execute("""SELECT * FROM logistica""")
        for i in exibir.fetchall():
            print(i)
        atualizar()

    #Deletar dados
    elif op==4:
        delet = 1
        while delet !=0:
            exibir = tabela.execute("""SELECT * FROM logistica""")
            for i in exibir.fetchall():
                print(i)
            delet = input("Para excluir uma coluna digite seu Codigo | Para excluir todos os dados digite [all] | Para sair digite [0]...\n")
            deletar(delet)
            break

