<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "kampus"; // nama database kamu

// Membuat koneksi
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Mengecek koneksi
if (!$conn) {
    die("Koneksi gagal: " . mysqli_connect_error());
}
echo "Koneksi ke database berhasil!";
?>
