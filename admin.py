import _sqlite3
database = 'database.db'


con = _sqlite3.connect(database)
cursor = con.cursor()

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username (self):
        return self.username

    def get_password (self):
        return self.password

    def set_default (self):
        cek_admin = con.execute('SELECT * FROM data_user WHERE username=?', (Admin.get_username(self),))
        if cek_admin.fetchall() is None :
            db = 'INSERT INTO data_user (username, password) VALUES (\'%s\',\'%s\')'
            db = db % ('admin', 'admin')
            cursor.execute(db)
            con.commit()
            con.close()
        else:
            print('data sudah ada')

    def del_admin (self, id_admin):
        self.id_del = id_admin
        sql = 'DELETE FROM data_user WHERE username=?'
        cursor.execute(sql, (self.id_del,))
        con.commit()

    def daftar_data_admin (self):
        sql = "SELECT * FROM data_user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data)
        con.close()



con.close()

