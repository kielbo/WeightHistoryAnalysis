import sqlite3
from datetime import date


class Database:
    """Klasa do obslugi bazy danych sqlite3,  podstawowe działania:
        1.Tworzenie bazy
        2.Dodawanie rekordu
        3.Wyswietlanie zawartości
        4.usuwanie rekordu
        5.Aktualizacja
        """

    def __init__(self,db_name):
        """Konstruktor przyjmuje jeden argument i na jego podstawie tworzy bazę danych jeśli nie istnieje już baza o takiej nazwie. Nastepnie tworzy polączenie z bazą. Baza musi się znajdować w tym samym folderze co program"""
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS fat (id INTEGER PRIMARY KEY,day DATE,weight INTEGER )")
        self.conn.commit()

    def insert(self,weight,today=date.today()):
        """nowy wpis w bazie danych"""
        self.cur.execute("INSERT INTO fat VALUES (NULL,?,?)",(today,weight))
        self.conn.commit()

    def view(self):
        """zwraca zawartosc bazy danych"""
        self.cur.execute("SELECT * FROM fat")
        rows = self.cur.fetchall() 
        self.conn.commit()
        return rows

    def delete(self,id):
        """usuwa rekord po id"""
        self.cur.execute("DELETE FROM fat WHERE id=?",(id,)) #jesli nie da sie "," za parametrem id wyrzuci bład. Nie jestep pewien dlaczego. SPRAWDZiĆ!
        self.conn.commit()

    def update(self,id,weight,date):
        """aktualizuje wybrany wpis o podane wartosci"""
        #if date == None:
        #    date=self.today
        self.cur.execute("UPDATE fat SET day=?, weight=? where id=?",(date,weight,id))
        self.conn.commit()

    def __del__(self):
        """Destruktor zamyka połączenie z bazą danych"""
        self.conn.close()


#xd= Database("fat.db")
#xd.insert(8888)
#print(xd.view())
#xd.update(5,"2020-01-01",80)
#print(xd.view())
#xd.delete(4)
#print(xd.view())

