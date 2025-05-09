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

    words = set({})

    def add(word):
        words.add(word)

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
    
    return list(words)


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


# script_name = 'khmer'
# unicode_ranges = {
#     'Khmer': {'first_including': 0x1780, 'last_including': 0x17FF},
#     'Khmer Symbols': {'first_including': 0x19E0, 'last_including': 0x19FF}
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'bengali'
# unicode_ranges = {
#     'Bengali': {'first_including': 0x0980, 'last_including': 0x09FF},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'gurmukhi'
# unicode_ranges = {
#     'Gurmukhi': {'first_including': 0x0A00, 'last_including': 0x0A7F},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'telugu'
# unicode_ranges = {
#     'Telugu': {'first_including': 0x0C00, 'last_including': 0x0C7F},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'tamil'
# unicode_ranges = {
#     'Tamil': {'first_including': 0x0B80, 'last_including': 0x0BFF},
#     'Tamil Supplement': {'first_including': 0x11FC0, 'last_including': 0x11FFF},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'gujarati'
# unicode_ranges = {
#     'Gujarati': {'first_including': 0x0A80, 'last_including': 0x0AFF},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'kannada'
# unicode_ranges = {
#     'Kannada': {'first_including': 0x0C80, 'last_including': 0x0CFF},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'oriya'
# unicode_ranges = {
#     'Oriya': {'first_including': 0x0B00, 'last_including': 0x0B7F},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)


# script_name = 'malayalam'
# unicode_ranges = {
#     'Malayalam': {'first_including': 0x0D00, 'last_including': 0x0D7F},
# }
# filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
# filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)

script_name = 'arabic'
unicode_ranges = {
    'Arabic': {'first_including':  0x0600, 'last_including': 0x06FF},
    'Arabic Supplement': {'first_including':  0x0750, 'last_including': 0x077F},
    'Arabic Extended-B': {'first_including':  0x0870, 'last_including': 0x089F},
    'Arabic Extended-A': {'first_including':  0x08A0, 'last_including': 0x08FF},
    'Arabic Presentation Forms-A': {'first_including':  0xFB50, 'last_including': 0xFDFF},
    'Arabic Presentation Forms-B': {'first_including':  0xFE70, 'last_including': 0xFEFF},
    'Arabic Extended-C': {'first_including': 0x10EC0, 'last_including':0x10EFF},
    'Arabic Mathematical Alphabetic Symbols': {'first_including': 0x1EE00, 'last_including':0x1EEFF},
}
filter_by_script(folder='osm', script_name=script_name, unicode_ranges=unicode_ranges)
filter_by_script(folder='wikipedia', script_name=script_name, unicode_ranges=unicode_ranges)
filter_by_script(folder='wikidata', script_name=script_name, unicode_ranges=unicode_ranges)
