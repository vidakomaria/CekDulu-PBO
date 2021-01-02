import _sqlite3
import admin as data_admin
import tempat_wisata as obj_wisata

database = 'database.db'
con = _sqlite3.connect(database)
cursor = con.cursor()

#membuat tabel data user
def add_tabel_user ():
    con.execute(
        "CREATE TABLE IF NOT EXISTS data_user (username varchar , password varchar )"
    )

def add_tabel_wisata ():
    con.execute(
        "CREATE TABLE IF NOT EXISTS tempat_wisata "
        "(kode_obj int, nama_objek varchar, lokasi varchar, "
        "daerah varchar, harga_tiket int, kategori varchar)")

def add_tabel_hotel ():
    con.execute(
        "CREATE TABLE IF NOT EXISTS data_hotel "
        "(id_hotel int, nama varchar, alamat varchar, kota varchar, provinsi varchar, kapasitas int, harga int, kelas varchar)")

def add_tempat_wisata ():
    #add_wisata = obj_wisata.Wisata('001')
    #cek_wisata = con.execute('SELECT * FROM tempat_wisata WHERE kode_obj = ?', (add_wisata.get_kode_obj(),))
    db_tWisata = 'INSERT INTO tempat_wisata (kode_obj, nama_objek, lokasi, daerah, harga_tiket, kategori) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'
    db_tWisata = db_tWisata % ('001', 'nama', 'lokasi', 'daerah', 'hrg', 'kategor')
    cursor.execute(db_tWisata)
    con.commit()
    con.close()

def add_tempat_wisata():
    add = [('1', 'The Lost World Castle', 'Kepuharjo, Cangkringan, Kabupaten Sleman', 'Yogyakarta', '25.000','Wisata Edukasi'),
           ('2', 'Candi Prambanan', 'Bokoharjo, Kec. Prambanan, Kabupaten Sleman', 'Yogyakarta', '40.000', 'Wisata Edukasi'),
           ('3', 'Upside Down World', 'Jl. Ring Road Utara, Maguwoharjo, Kec. Depok, Kab. Sleman', 'Yogyakarta','80.000', 'Wisata Fotografi'),
           ('4', 'Hutan Pinus Mangunan', 'Mangunan, Dlingo, Bantul', 'Yogyakarta', '2.500', 'Wisata Alam'),
           ('5', 'Kebun Buah Mangunan', 'Mangunan, Dlingo, Bantul', 'Yogyakarta', '5.000', 'Wisata Alam'),
           ('6', 'Pantai Parangtritis', 'Parangtritis, Kec. Kretek, Bantul', 'Yogyakarta', '10.000', 'Wisata Alam'),
           ('7', 'Bukit Paralayang', 'Giricahyo, Purwosari, Kabupaten Gunung Kidul', 'Yogyakarta', '5.000','Wisata Alam'),
           ('8', 'Pantai Depok', 'Parangtritis, Kec. Kretek, Bantul', 'Yogyakarta', '10.000', 'Wisata Alam'),
           ('9', 'Bali Zoo Park', 'Gianyar', 'Bali', '110.000 - 140.000', 'Wisata Edukasi '),
           ('10', 'Danau Beratan Bedugul', 'Tabanan', 'Bali', '20.000 - 30.000', 'Wisata Alam'),
           ('11', 'Sawah Terasering Tegalalang', 'Gianyar', 'Bali', '10.000', 'Wisata Alam'),
           ('13', 'Garuda Wisnu Kencana', 'Denpasar', 'Bali', '100.000 - 200.000', 'Wisata Budaya'),
           ('15', 'Tanah Lot', 'Tabanan', 'Bali', '15.000 - 20.000', 'Wisata Alam'),
           ('16', 'Kebun Raya Bedugul', 'Tabanan', 'Bali', '9.000', 'Wisata Alam'),
           ('17', 'Air Panas Banjar', 'Singaraja', 'Bali', '10.000 - 20.000', 'Wisata alam'),
           ('18', 'Air Terjun Les Buleleng', 'Buleleng', 'Bali', '20.000', 'Wisata alam'),
           ('19', 'Jatim Park 1', 'Jl. Kartika No. 2, Kota Batu', 'Malang', '100.000', 'Wisata Edupark'),
           ('20', 'Jatim Park 2', 'Jl. Oro Oro Ombo No.9', 'Malang', '120.000', 'Wisata Edupark'),
           ('21', 'Museum Angkut', 'Jl. Sultan Agung No.2, Ngaglik', 'Kota Wisata Batu', '100.000', 'Wisata Edukasi'),
           ('22', 'Air Terjun Coban Rondo', 'Kecamatan Pujon', 'Kota Wisata Batu', '15.000', 'Wisata Alam'),
           ('23', 'Air Panas Cangar', 'Desa Sumber Brantas, Kec. Bumiaji', 'Kota Wisata Batu', ' 10.000', 'Wisata Alam'),
           ('24', 'Dino Park Jatim Park 3', 'Jalan Raya Ir. Soekarno No.144, Beji Junrejo', 'Kota Wisata Batu','100.000', 'Wisata Bermain'),
           ('25', 'Selecta', 'Desa Tulungrejo, Kec. Bumiaji', 'Kota Wisata Batu', '25.000', 'Wisata Alam'),
           ('26', 'Pantai Senggigi', 'Senggigi, Batu Layar', 'Lombok', '15.000', 'Wisata Alam')]
    for i in range(len(add)):
        temp = (add[i][0])
        cek_wisata = con.execute('SELECT * FROM tempat_wisata WHERE kode_obj = ?', (temp,))
        if cek_wisata.fetchall is None:
            cursor.executemany(
                'INSERT INTO tempat_wisata (kode_obj, nama_objek, lokasi, daerah, harga_tiket, kategori) VALUES (?,?,?,?,?,?);',
                (add), )
            con.commit()
            con.close()
        else:
            print('kode objek sudah ada')

def add_hotel():
    add = [('1','Victory Guesthouse', 'Jl. Raya Kledokan No.11, Senturan, Depok', 'Sleman', 'Yogyakarta', '12', '190.000/room', '1'),
           ('2', 'Allstay Hotel', 'Jl. Wahid Hasyim No. 41', 'Sleman', 'Yogyakarta', '30', '400.400/room', '3'),
           ('3', 'Royal Ambarrrukmo Yogyakarta', 'Jl. Laksda Adisucipto No.81, Depok', 'Sleman', 'Yogyakarta', '133',
            '1.388.000/room', '5'),
           (
           '4', 'Hotel Amaris Duo Legian', 'Jl. Batu Pageh Gg. Melani Legian', 'Denpasar', 'Bali', '24', '347.650/room',
           '2'),
           ('5', 'Hotel Sense Seminyak', 'Jl Kayu Jati No.16, Seminyak', 'Denpasar', 'Bali', '50', '521.000/room', '4'),
           (
           '6', 'Hotel Whiz Prime', 'Jl. Jenderal Basuki Rahmat No 85-87', 'Malang', 'Jawa Timur', '20', '350.000/room',
           '3'),
           ('7', 'El Hotel Grande Malang',
            'Jalan Bukit Palem Raya No 1&3, Green Hills Residence, Karangploso, Karangploso', 'Malang', 'Jawa Timur',
            '80', '345.000/room', '3')]

    for i in range(len(add)):
        temp = (add[i][0])
        cek_hotel = con.execute('SELECT * FROM data_hotel WHERE id_hotel = ?', (temp,))
        if cek_hotel.fetchall is None:
            cursor.executemany(
                'INSERT INTO data_hotel (id_hotel, nama, alamat, kota, provinsi, kapasitas, harga, kelas) VALUES (?,?,?,?,?,?,?,?);',
                (add), )
            con.commit()
            con.close()
        else:
            print('id hotel sudah ada')

def add_tabel_paket ():
    con.execute('CREATE TABLE IF NOT EXISTS paket '
                '(id_paket int, nama_paket varchar, harga int, kapasitas int, destinasi varchar, fasilitas varchar)')

def add_data_paket():
    add = [('1', 'Jojga1', '5.720.000', '4 Orang', 'Pantai Timang, Tebing Breksi, Sunset di Candi Ijo, Candi Borobudur, The Lost World Castle, Merapi Park, Malioboro, Keraton Yogyakarta, Tamansari, De Walik Museum',
            'Penginapan Hotel Selama 2 malam di Cordella Hotel,Breakfast di Hotel 2x,Kendaraan AC standar pariwisata,Driver as Guide,BBM,Parkir,Drop in dan drop off '
            '(Terminal/ Bandara/ Stasiun/ Hotel) di Yogyakarta, Tiket masuk destinasi sesuai jadwal,Free Antar Wisata Kuliner dan Wisata Oleh Oleh,Air mineral'),
           ('2', 'Jogja2', '6.352.000', '4 Orang',
            'Pantai Timang, Tebing Breksi, Sunset di Candi Ijo, Candi Borobudur, The Lost World Castle, Merapi Park, Malioboro, Keraton Yogyakarta, Tamansari, De Walik Museum',
            'Penginapan Hotel Selama 2 malam di The Alana Malioboro,Breakfast di Hotel 2x,Kendaraan AC standar pariwisata,Driver as Guide,BBM,Parkir,Drop in dan drop off '
            '(Terminal/ Bandara/ Stasiun/ Hotel) di Yogyakarta, Tiket masuk destinasi sesuai jadwal,Free Antar Wisata Kuliner dan Wisata Oleh Oleh,Air mineral'),
           ('3', ' Bali1', '5.640.000', '4 Orang',
            'Batu Bulan, Galuh Batik, Desa Celuk, Kintamani, Agrowisata Kopi Luwak, Tampak Siring, Tempat Oleh-oleh.',
            'Menginap 2 malam di Hotel Sense Seminyak, 2 kali transfer, Tiket masuk wisata, breakfast di hotel, driver sekalligus guide, kendaraan standart new.'),
           ('4', 'Bali2', '6.380.000', '4 Orang',
            'Pura Tanah Lot, Tanjung BenoaPantai Pandawa,Garuda Wisnu Kencana,Pura Luhur Uluwatu,Jimbaran,Krisna Bali Pusat Oleh-oleh',
            'Private Transport, Akomodasi 2 malam menginap di Hotel Amaris Duo Legian, tiket masuk wisata, makan sesuai program, air mineral, parkir dan tol, driver as guide'),
           ('5', 'Malang1', '4.830.000', '2 Orang',
            'Air terjun coban rondo, taman labirin, jatim park 2, museum satwa, wisata petik apel, museum angkut, alun-alun batu, BNS, tempat oleh-oleh, Menginap di El Hotel/Whiz Prime'),
           ('5', 'Malang1', '6.900.000', '4 Orang',
            'Air terjun coban rondo, taman labirin, jatim park 2, museum satwa, wisata petik apel, museum angkut, alun-alun batu, BNS, tempat oleh-oleh, Menginap di El Hotel/Whiz Prime')
           ]
    cursor.executemany('INSERT INTO paket (id_paket, nama_paket, harga, kapasitas, destinasi, fasilitas ) VALUES (?,?,?,?,?,?);',(add), )
    con.commit()
    con.close()



#sql = 'DELETE FROM tempat_wisata'
#cursor.execute(sql)
#add_tempat_wisata()
#con.execute('DROP TABLE paket')
#add_tabel_paket()
add_data_paket()

def menu_admin ():
    daftarAdmin = data_admin.Admin(None,None)
    daftarAdmin.daftar_data_admin()
    con.commit()

#add_tabel_wisata()

con.close()