from bisect import bisect_left, insort
import subprocess

def get_mask(unicode_ranges):

    mask = {}

    for i in range(2**16):
        mask[i] = False

        for r in unicode_ranges:
            if unicode_ranges[r]['first_including'] <= i <= unicode_ranges[r]['last_including']:
                mask[i] = True
    
    return mask

def get_words(mask, folder, script_name):

    words = []

    def add(word):
        index = bisect_left(words, word)

        if index < len(words) and words[index] == word:
            # word already in words, do nothing
            pass
        else:
            # word not yet in words, add it
            insort(words, word)

    current_word = ''

    filename = f'{folder}/{folder}-corpus-with-duplicates.txt'

    with open(filename) as f:
        line_i = 0
        while True:
            if line_i % 1_000_000 == 0:
                print(f'reading line {int(line_i / 1_000_000)}M, {int(len(words) / 1_000)}k {script_name} words, {filename}...')
            line_i += 1

            line = f.readline()
            if not line:
                break
            line = line.strip()
            for letter in line:
                
                if ord(letter) < 2 ** 16 and mask[ord(letter)]:
                    current_word += letter
                else:
                    if len(current_word) > 0:
                        add(current_word)
                        current_word = ''
            add(current_word)
            current_word = ''
    
    return words


def filter_by_script(folder, script_name, unicode_ranges):

    mask = get_mask(unicode_ranges)
    words = get_words(mask, folder, script_name)

    out_filename = f'{folder}/{folder}-{script_name}-corpus.txt'
    print(f'writing {out_filename}...')
    
    with open(out_filename, 'w', encoding='utf-8', errors='replace') as f:
        for word in words:
            f.write(f'{word}\n')
    
    command = f'zip -r {out_filename}.zip {out_filename}'
    print(command)
    subprocess.run(command, shell=True)




# script_name = 'devanagari'
# unicode_ranges = {
#     'Devanagari': {'first_including': 0x0900, 'last_including': 0x097F},
#     'Devanagari Extended': {'first_including': 0xA8E0, 'last_including': 0xA8FF},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'myanmar'
# unicode_ranges = {
#     'Myanmar': {'first_including': 0x1000, 'last_including': 0x109F},
#     'Myanmar Extended-B': {'first_including': 0xA9E0, 'last_including': 0xA9FF},
#     'Myanmar Extended-A': {'first_including': 0xAA60, 'last_including': 0xAA7F},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


script_name = 'khmer'
unicode_ranges = {
    'Khmer': {'first_including': 0x1780, 'last_including': 0x17FF},
    'Khmer Symbols': {'first_including': 0x19E0, 'last_including': 0x19FF}
}
filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)
