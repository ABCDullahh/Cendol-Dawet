GitHub Commit Bot
=================

Deskripsi
---------
Bot ini secara otomatis membuat commit acak ke repository GitHub setiap hari pada waktu yang ditentukan. Bot ini menggunakan Python dan dijalankan menggunakan Task Scheduler di Windows untuk memastikan berjalan 24/7 tanpa perlu komputer lokal.

Persyaratan
-----------
1. Python 3.x
2. Git
3. Modul Python: schedule, gitpython
4. Repository GitHub yang sudah dikloning ke lokal

Instalasi
---------
1. **Install Python** (jika belum terinstall):
    - Unduh dan instal Python dari [python.org](https://www.python.org/downloads/).
    - Pastikan untuk mencentang opsi "Add Python to PATH" selama instalasi.

2. **Install Git**:
    - Unduh dan instal Git dari [git-scm.com](https://git-scm.com/downloads).

3. **Install modul Python yang dibutuhkan**:
    - Buka Command Prompt atau PowerShell dan jalankan perintah berikut:
      ```sh
      pip install schedule gitpython
      ```

4. **Clone repository GitHub ke direktori lokal**:
    - Buka Command Prompt dan jalankan perintah berikut, ganti `username` dan `repo` dengan username dan nama repository GitHub Anda:
      ```sh
      git clone https://github.com/username/repo.git C:\path\to\your\repo
      ```

5. **Navigasi ke direktori repository**:
    ```sh
    cd C:\path\to\your\repo
    ```

6. **Konfigurasi remote repository** (jika diperlukan):
    ```sh
    git remote add origin https://github.com/username/repo.git
    git fetch
    git branch -u origin/main
    ```
