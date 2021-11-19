import sqlite3


def criaTabela(banco): 
    query1 = """ 
                   CREATE TABLE "usuario" (
                           "game_id" INTEGER NOT NULL
                           "username" TEXT NOT NULL,
                           "email" TEXT NOT NULL PRIMARY KEY,
                           "bio" TEXT,
                           FOREIGN KEY (game_id) REFERENCES game (id) 
                   ); 
                   """
    query2 = """ 
                   CREATE TABLE "game" (
                           "id" INTEGER PRIMARY KEY AUTOINCREMENT  
                           "title" TEXT NOT NULL,
                           "developer" TEXT,
                           "publisher" TEXT,
                           "playing" BOOLEAN NOT NULL CHECK (playing IN (0, 1)),
                           "mainquest" BOOLEAN NOT NULL CHECK (mainquest IN (0, 1)), 
                           "mainquestPlus" BOOLEAN NOT NULL CHECK (mainquestPlus IN (0, 1)), 
                           "complete" BOOLEAN NOT NULL CHECK (complete IN (0, 1))  
                   ); 
                   """
    try: 
        conn = sqlite3.connect(banco) 
        cursor = conn.cursor() 
        cursor.execute(query2) 
        cursor.execute(query1)
        print("Tabela criada")
        cursor.close()
        conn.close() 
    except sqlite3.Error as e: 
        print("Erro ao criar tabela: ", sqlite3.Error) 
    return 