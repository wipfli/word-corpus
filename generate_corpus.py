from glob import glob
from bisect import bisect_left, insort

def get_mask(unicode_ranges):

    mask = {}

    for i in range(2**16):
        mask[i] = False

        for r in unicode_ranges:
            if unicode_ranges[r]['first_including'] <= i <= unicode_ranges[r]['last_including']:
                mask[i] = True
    
    return mask

def get_words(mask):

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

    # wikidata
    filenames = sorted(glob('wikidata/words/*'))

    # wikipedia
    filenames += sorted(glob('wikipedia/words/*'))

    file_i = 0
    for filename in filenames:

        print(f'reading {file_i} of {len(filenames)}: {filename}...')
        file_i += 1

        with open(filename) as f:
            while True:
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

name = 'Devanagari'

unicode_ranges = {
    'Devanagari': {'first_including': 0x0900, 'last_including': 0x097F},
    'Devanagari Extended': {'first_including': 0xA8E0, 'last_including': 0xA8FF},
}

mask = get_mask(unicode_ranges)

words = get_words(mask)

print(len(words))

total_len = 0
for word in words:
    total_len += len(word)
print('total_len', total_len)
print('avg len', total_len / len(words))
