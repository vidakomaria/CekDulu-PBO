import _sqlite3
database = 'database.db'

con = _sqlite3.connect(database)
cursor = con.cursor()

class Hotel:
    def __init__(self, idHotel):
        self.idHotel =idHotel

    def get_idHotel (self)
        return self.idHotel

    def detail_hotel (self):
        sql = 'SELECT * FROM data_hotel WHERE id_hotel LIKE \'%s\''
        sql = sql % (self.idHotel)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print('NAMA HOTEL \t:',data[1],
                  '\nALAMAT \t:',data[2],data[3],data[4],
                  '\nKAPASITAS \t:',data[5],
                  '\nHARGA \t: Rp.',data[6],
                  '\nKELAS  \t:',data[7])
        con.close()

    def daftar_hotel (self):
        sql = "SELECT nama, kota FROM data_hotel"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0],data[1])
        con.close()


class Kelas (Hotel):
    def daftar_wisata (self, kelas):
        self.kelas = kelas
        sql = 'SELECT nama, kota FROM data_hotel WHERE kelas LIKE \'%s\''
        sql = sql % (self.kelas)
        cursor.execute(sql)
        result = cursor.fetchall()
        print('HOTEL KELAS', self.kelas,'\nNAMA','\tLOKASI')
        for data in result:
            print(data[0], '\t', data[1])
        con.close()



con.close()