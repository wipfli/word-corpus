from wikis import wikis
import subprocess

# downloads wiki dumps from https://dumps.wikimedia.org/backup-index.html

date = '20240101'

for wiki in wikis:
    filename = f'{wiki}-{date}-pages-articles-multistream.xml'
    url = f'https://dumps.wikimedia.org/{wiki}/{date}/{filename}.bz2'

    command = f'axel -n 10 {url}'
    print(command)
    subprocess.run(command, shell=True)

    command = f'bunzip2 {filename}.bz2'
    print(command)
    subprocess.run(command, shell=True)

    command = f'cat {filename} >> wikipedia.txt'
    print(command)
    subprocess.run(command, shell=True)

    command = f'rm {filename}'
    print(command)
    subprocess.run(command, shell=True)
