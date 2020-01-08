import sqlite3
from datetime import date


class Database:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS fat (id INTEGER PRIMARY KEY,day DATE,weight INTEGER )")
        self.conn.commit()
        self.today = date.today()

    def insert(self,weight):
        """nowy wpis w bazie danych"""
        self.cur.execute("INSERT INTO fat VALUES (NULL,?,?)",(self.date,weight))
        self.conn.commit()

    def viev(self):
        """zwraca zawartosc bazy danych"""
        self.cur.execute("SELECT * FROM fat")
        self.rows = cur.fetchall() 
        self.conn.commit()
        return rows

    def delete(self,id):
        """usuwa rekord po id"""
        self.cur.execute("DELETE FROM fat WHERE id=?",(id,)) #jesli nie da sie , za parametrem id wyrzuci bład. Nie jestep pewien dlaczego. SPRAWDZiĆ!
        self.conn.commit()

    def update(self,id,date,weight):
        """aktualizuje wybrany wpis o podane wartosci"""
        self.cur.execute("UPDATE fat SET day=?, weight=? where id=?",(date,weight,id))
        self.conn.commit()

    def __del__(self):
        self.conn
#insert(today,100)
#update(3,today,90)
#print(viev())
