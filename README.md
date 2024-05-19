# project6_datasphere7_Data Analytics with Hadoop
## Study Case

Di proyek sebelumnya anda telah membuat batch processing untuk data migrasi. Sebagai tambahan, anda diminta untuk membuat tabel data mart yang nantinya akan digunakan oleh data analis untuk membuat dashboard report order setiap bulannya. Proses yang dilakukan tidak boleh lebih dari 1 jam.

## Tools  
- Postgres (via Docker or direct install)
- Hadoop versi &lt; 3.2.1 - Script Project 3
- Batch Processing
- GUI Postgres (Pgadmin, Dbeaver, dll) (optional)

##task tersebut sebagai berikut:

1. Extract data source ke database postgres (skip, sudah ada di project 3).
2. Buatlah file DWH `dim_orders` dengan menggunakan hadoop.
3. Buatlah data mart `total_orders_based_on_month` dengan MapReduce, data diambil dari DWH.

## Step by Step

1. Proyek ini melanjutkan proyek sebelumnya terkait batch processing. (Silakan dibuka script yang telah disiapkan sebelumnya)
2. Buatlah flow diagram ETL yang akan dibuat
3. Tambahkan koneksi json hadoop
4. Buatlah script koneksi hadoop
5. Define datetime now
6. Buatlah script data dummy DWH ke local terlebih dahulu
7. Buatlah script upload data ke hadoop sebagai DWH
8. Buatlah script transform dengan menggunakan MapReduce
9. Sesuaikan output yang diminta
