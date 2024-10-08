# Modul Kontrol PID untuk Kursus Laboratorium Fisika

## Gambaran Umum

**Modul Kontrol PID** dikembangkan menggunakan **mikrokontroler ATMega** yang terintegrasi dengan **Python**. Modul ini dirancang untuk membantu siswa dalam **Kursus Laboratorium Fisika** memahami cara kerja sistem kontrol PID, baik dari segi perangkat keras maupun fisika dasar.

Sistem ini menggunakan mikrokontroler ATMega sebagai komponen perangkat keras utama, memanfaatkan **PWM Inverting** untuk mengontrol sinyal aktuator. Data dari mikrokontroler ditransmisikan ke monitor serial, di mana data tersebut diproses menggunakan Python untuk menghasilkan grafik dan menganalisis perilaku sistem. Selain itu, siswa dapat menyesuaikan sinyal kontrol melalui antarmuka.

## Fitur

- **Sistem Kontrol PID**: Demonstrasi praktis tentang bagaimana pengontrol PID beroperasi.
- **Visualisasi Data Real-Time**: Data ditransmisikan dari mikrokontroler ke Python untuk menghasilkan grafik dan analisis secara real-time.
- **Antarmuka Ramah Pengguna**: Dibangun menggunakan pustaka Python Tkinter, antarmuka ini memungkinkan siswa, bahkan yang tidak familiar dengan Python, untuk berinteraksi dengan sistem secara efektif.
- **Sinyal Kontrol yang Dapat Disesuaikan**: Siswa dapat memodifikasi sinyal kontrol melalui antarmuka grafis untuk mengamati efeknya terhadap perilaku sistem.

## Teknologi yang Digunakan

- **Mikrokontroler ATMega**: Berfungsi sebagai komponen perangkat keras utama.
- **Python**: Digunakan untuk pemrosesan dan visualisasi data.
- **Serial USB**: penghubung antara microcontroller dan komputer.
- **PWM Inverting**: mengontrol sinyal aktuator.

## Cara Penggunaan
- Anda memerlukan Civ-AVR untuk menjalakankan program dan membentuk file hex untuk di burning ke dalam microcontroller ATMega
- **Realy_PID.py** dan **Relay.c** merupakan pemrograman untuk modul kontroler on-off
- **PID.py** dan **PID Controller.c** merupakan pemrograman untuk modul kontroler pid
- Setalah melakukan instalansi perangkat keras, hubungkan kabel serial ke port komputer anda, lalu ubah variabel ***PORT*** sesuai port yang digunakan.

## Persyaratan

Untuk menjalankan proyek ini, Anda perlu library berikut. Anda dapat menginstalnya menggunakan pip:

```bash
pip install -r requirements.txt
```
