import schedule
import time
import random
import os
from git import Repo, GitCommandError
from datetime import datetime

# Konfigurasi repository lokal Anda
repo_dir = 'D:\\GithubBOT'  # Ganti dengan path repository Anda
repo = Repo(repo_dir)
assert not repo.bare

# Fungsi untuk membuat commit
def make_commit():
    try:
        # Jumlah commit acak (1-5)
        num_commits = random.randint(1, 3)
        for _ in range(num_commits):
            # Buat perubahan acak di file untuk di-commit
            with open(os.path.join(repo_dir, 'random_file.txt'), 'a') as f:
                f.write(f'Commit at {datetime.now()}\n')

            # Tambahkan file ke staging area
            repo.index.add(['random_file.txt'])

            # Buat commit
            repo.index.commit(f'Random commit at {datetime.now()}')

        # Push ke remote repository
        origin = repo.remote(name='origin')
        origin.push()
        print('Pushed commits to remote repository.')

    except GitCommandError as e:
        print(f'Error during commit: {e}')

# Jadwalkan tugas setiap hari
schedule.every().day.at("10:40:30").do(make_commit)  # Ganti waktu sesuai kebutuhan

print("Scheduler is running...")

# Jalankan scheduler
while True:
    schedule.run_pending()
    time.sleep(1)