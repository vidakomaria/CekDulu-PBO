import _sqlite3
database = 'database.db'

con = _sqlite3.connect(database)
cursor = con.cursor()

class Paket :
    def __init__(self):
        pass

    def destinasi (self, destinasi):
        self.destinasi = destinasi
        sql = 'SELECT nama_paket, destinasi FROM paket WHERE destinasi LIKE \'%s\''
        sql = sql % (self.destinasi)
        cursor.execute(sql)
        result = cursor.fetchall()
        print('WISATA DAERAH', self.destinasi, '\nNAMA WISATA', '\tLOKASI')
        for data in result:
            print('{} DESTINASI: {}.'.format(data[0],data[1]))
        con.close()

def add_data_paket():
    add = [('1', 'Jojga1', '5.720.000', '4', 'Pantai Timang, Tebing Breksi, Sunset di Candi Ijo, Candi Borobudur, The Lost World Castle, Merapi Park, Malioboro, Keraton Yogyakarta, Tamansari, De Walik Museum',
            'Penginapan Hotel Selama 2 malam di Cordella Hotel,Breakfast di Hotel 2x,Kendaraan AC standar pariwisata,Driver as Guide,BBM,Parkir,Drop in dan drop off '
            '(Terminal/ Bandara/ Stasiun/ Hotel) di Yogyakarta, Tiket masuk destinasi sesuai jadwal,Free Antar Wisata Kuliner dan Wisata Oleh Oleh,Air mineral'),
           ('2', 'Jogja2', '6.352.000', '4',
            'Pantai Timang, Tebing Breksi, Sunset di Candi Ijo, Candi Borobudur, The Lost World Castle, Merapi Park, Malioboro, Keraton Yogyakarta, Tamansari, De Walik Museum',
            'Penginapan Hotel Selama 2 malam di The Alana Malioboro,Breakfast di Hotel 2x,Kendaraan AC standar pariwisata,Driver as Guide,BBM,Parkir,Drop in dan drop off '
            '(Terminal/ Bandara/ Stasiun/ Hotel) di Yogyakarta, Tiket masuk destinasi sesuai jadwal,Free Antar Wisata Kuliner dan Wisata Oleh Oleh,Air mineral'),
           ('3', ' Bali1', '5.640.000', '4 ',
            'Batu Bulan, Galuh Batik, Desa Celuk, Kintamani, Agrowisata Kopi Luwak, Tampak Siring, Tempat Oleh-oleh.',
            'Menginap 2 malam di Hotel Sense Seminyak, 2 kali transfer, Tiket masuk wisata, breakfast di hotel, driver sekalligus guide, kendaraan standart new.'),
           ('4', 'Bali2', '6.380.000', '4 ',
            'Pura Tanah Lot, Tanjung BenoaPantai Pandawa,Garuda Wisnu Kencana,Pura Luhur Uluwatu,Jimbaran,Krisna Bali Pusat Oleh-oleh',
            'Private Transport, Akomodasi 2 malam menginap di Hotel Amaris Duo Legian, tiket masuk wisata, makan sesuai program, air mineral, parkir dan tol, driver as guide'),
           ('5', 'Malang1', '4.830.000', '2 ',
            'Air terjun coban rondo, taman labirin, jatim park 2, museum satwa, wisata petik apel, museum angkut, alun-alun batu, BNS, tempat oleh-oleh, Menginap di El Hotel/Whiz Prime'),
           ('5', 'Malang1', '6.900.000', '4',
            'Air terjun coban rondo, taman labirin, jatim park 2, museum satwa, wisata petik apel, museum angkut, alun-alun batu, BNS, tempat oleh-oleh, Menginap di El Hotel/Whiz Prime')
           ]
    cursor.executemany('INSERT INTO paket (id_paket, nama_paket, harga, kapasitas, destinasi, fasilitas ) VALUES (?,?,?,?,?,?);',(add), )
    con.commit()
    con.close()
add_data_paket()