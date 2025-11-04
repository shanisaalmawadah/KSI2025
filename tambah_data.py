echo "from database import koneksi

def tambah_data(nama, umur):
    db = koneksi()
    cursor = db.cursor()
    sql = 'INSERT INTO users (nama, umur) VALUES (%s, %s)'
    cursor.execute(sql, (nama, umur))
    db.commit()
    print('Data berhasil ditambahkan!')
" > tambah_data.py
