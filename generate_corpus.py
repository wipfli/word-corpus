from glob import glob
import subprocess

def generate_corpus(folder):
    filenames = sorted(glob(f'{folder}/words/*'))
    out_filename = f'{folder}/{folder}-corpus-with-duplicates.txt'

    command = f'rm -rf {out_filename} {out_filename}.zip'
    print(command)
    subprocess.run(command, shell=True)
    
    for filename in filenames:
        command = f'cat {filename} >> {out_filename}'
        print(command)
        subprocess.run(command, shell=True)
    
    command = f'zip -r {out_filename}.zip {out_filename}'
    print(command)
    subprocess.run(command, shell=True)

generate_corpus(folder='osm')
generate_corpus(folder='wikipedia')
generate_corpus(folder='wikidata')
