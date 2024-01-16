import subprocess

# downloads wikidata from https://dumps.wikimedia.org/wikidatawiki/entities/

command = f'axel -n 10 https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2'
print(command)
subprocess.run(command, shell=True)

command = f'bunzip2 latest-all.json.bz2'
print(command)
subprocess.run(command, shell=True)
