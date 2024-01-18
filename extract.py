from os.path import getsize
import subprocess
from concurrent.futures import ProcessPoolExecutor

from latin_greek_cyrillic_cjk import ignore_mask

bytes_to_read = 1_000_000_000

def run(offset, folder, filename, encoding):

    f = open(f'{folder}/{filename}', encoding=encoding)
    f.seek(offset)

    words = set()
    current_word = ''

    index = int(offset / bytes_to_read)
    print(f'reading {folder} {index}...')
    content = f.read(bytes_to_read)
    content = content.strip()

    for letter in content:
        if ord(letter) < 2**16 and not ignore_mask[ord(letter)]:
            current_word += letter
        else:
            if len(current_word) > 0:
                words.add(current_word)
                current_word = ''
    words.add(current_word)
    

    out_filename = f'{folder}/words/{index}.txt'
    print(f'writing {out_filename}...')
    
    with open(out_filename, 'w', encoding='utf-8', errors='replace') as f:
        words_list = sorted(list(words))
        for word in words_list:
            f.write(f'{word}\n')

def extract(folder, filename, encoding):
    command = f'mkdir -p {folder}/words/'
    print(command)
    subprocess.run(command, shell=True)

    filesize = getsize(f'{folder}/{filename}')
    offsets = range(0, filesize, bytes_to_read)
    
    input_values = []
    for offset in offsets:
        input_values.append((offset, folder, filename, encoding))

    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(run, *zip(*input_values))

# extract(folder='osm', filename='planet-latest.osm', encoding='utf-8')
extract(folder='wikidata', filename='latest-all.json', encoding='unicode_escape')
#extract(folder='wikipedia', filename='wikipedia.txt', encoding='utf-8')
