# Word Corpus

Scripts that extract a word corpus from OpenStreetMap, Wikipedia, and Wikidata targeting South-East Asian and Indic languages.

## Data License

* OpenStreetMap-derived data is licensed under the Open Data Commons Open Database License (ODbL). See https://www.openstreetmap.org/copyright
* Wikipedia-derived data is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA). See https://en.wikipedia.org/wiki/Wikipedia:Copyrights
* Wikidata-derived data is licensed under the Creative Commons CC0 License. See https://www.wikidata.org/wiki/Wikidata:Licensing

## Downloads

Download corpus with duplicates. These files contain only non-Latin/Greek/Cyrillic/CJK text as defined in the file [latin_greek_cyrillic_cjk.py](latin_greek_cyrillic_cjk.py).

* [osm-corpus-with-duplicates.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/osm-corpus-with-duplicates.txt.zip) (19M)
* [wikipedia-corpus-with-duplicates.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/wikipedia-corpus-with-duplicates.txt.zip) (816M)
* [wikidata-corpus-with-duplicates.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/wikidata-corpus-with-duplicates.txt.zip) (118M)

### Single Scripts

Download corpus for a single script without duplicates:

* Devanagari
  * [osm-devanagari-corpus.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/osm-devanagari-corpus.txt.zip) (197K)
  * [wikipedia-devanagari-corpus.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/wikipedia-devanagari-corpus.txt.zip) (94M)
  * [wikidata-devanagari-corpus.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/wikidata-devanagari-corpus.txt.zip) (1.2M)
* Myanmar
  * [osm-myanmar-corpus.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/osm-myanmar-corpus.txt.zip) (206K)
  * [wikipedia-myanmar-corpus.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/wikipedia-myanmar-corpus.txt.zip) (28M)
  * [wikidata-myanmar-corpus.txt.zip](https://pub-726b01260c98468a9387cc0dfcb7386b.r2.dev/wikidata-myanmar-corpus.txt.zip) (594K)

If you need some other language or script, please open an Issue on GitHub...

## Steps

Download data sources:

```bash
cd osm/
python3 download.py
cd ../wikidata/
python3 download.py
cd ../wikipedia/
python3 download.py
```

Extract non-Latin/Greek/Cyrillic/CJK text from sources with:

```bash
python3 extract.py
```

Generate word corpus with duplicates with:

```bash
python3 generate_corpus.py
```

Filter the corpus for a single script:

```bash
python3 filter_by_script.py
```
