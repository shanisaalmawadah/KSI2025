echo "import mysql.connector
def koneksi():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='nama_database'
    )
print('Koneksi ke database berhasil!')" > database.py
