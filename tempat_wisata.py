import _sqlite3
database = 'database.db'

con = _sqlite3.connect(database)
cursor = con.cursor()

class Wisata :
    def __init__(self, kode):
        self.kode_obyek = kode

    def get_kode_obj (self):
        return self.kode_obyek

    def daftar_wisata (self):
        sql = "SELECT nama_objek FROM tempat_wisata"
        cursor.execute(sql)
        result = cursor.fetchall()
        print('DAFTAR TEMPAT WISATA')
        for data in result:
            print ('{}'.format(data[0]))
        con.close()

    def detail_wisata (self):
        sql = 'SELECT * FROM tempat_wisata WHERE kode_obj LIKE \'%s\''
        sql = sql % (self.kode_obyek)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print('NAMA WISATA:\t',data[1],
                  '\nLOKASI:\t',data[2],data[3],
                  '\nHARGA TIKET MASUK: Rp.\t',data[4],
                  '\nKATEGORI WISATA:\t',data[5])
        con.close()

class Daerah (Wisata):
    def __init__(self):
        pass

    def daftar_wisata (self, daerah):
        self.daerah = daerah
        sql = 'SELECT nama_objek, lokasi FROM tempat_wisata WHERE daerah LIKE \'%s\''
        sql = sql % (self.daerah)
        cursor.execute(sql)
        result = cursor.fetchall()
        print('WISATA DAERAH',self.daerah,'\nNAMA WISATA','\tLOKASI')
        for data in result:
            print(data[0], '\t',data[1])
        con.close()

class Kategori (Wisata):
    #def __init__(self):
        #pass

    def daftar_wisata (self, kategori):
        self.kategori = kategori
        sql = 'SELECT nama_objek, daerah FROM tempat_wisata WHERE kategori LIKE \'%s\''
        sql = sql % (self.kategori)
        cursor.execute(sql)
        result = cursor.fetchall()
        print('DAFTAR KATEGORI', self.kategori, '\n============\nNAMA WISATA', '\tLOKASI')
        for data in result:
            print('{}, \t{}'.format(data[0],data[1]))
        con.close()

class HargaTiket (Wisata):
    def harga (self) :
        sql = 'SELECT nama_objek, daerah, harga_tiket FROM tempat_wisata'
        cursor.execute(sql)
        result = cursor.fetchall()
        print('DAFTAR HARGA')
        for data in result:
            print('{} , {} Rp. {}'.format(data[0],data[1],data[2]))
        con.close()


#Wisata.daftar_wisata(Wisata)
#Wisata.detail_wisata(Wisata)
#HargaTiket.harga(HargaTiket)
#Daerah.daftar_wisata(Daerah,'YOGYAKARTA')
#Kategori.daftar_wisata(Kategori,'WISATA EDUKASI')
#Default.add_tempat_wisata()
#con.execute('DROP TABLE tempat_wisata')
#con.commit()
con.close()