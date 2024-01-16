# Word Corpus

Scripts that extract a word corpus from OpenStreetMap, Wikipedia, and Wikidata targeting South-East Asian and Indic languages.

## Data License

* OpenStreetMap-derived data is licensed under the Open Data Commons Open Database License (ODbL). See https://www.openstreetmap.org/copyright
* Wikipedia-derived data is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA). See https://en.wikipedia.org/wiki/Wikipedia:Copyrights
* Wididata-derived data is licensed under the Creative Commons CC0 License. See https://www.wikidata.org/wiki/Wikidata:Licensing

## Downloads

* Devanagari: TODO ADD LINK
* Myanmar: TODO ADD LINK

Need some other language or script? Please open an Issue on GitHub...

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

Generate word corpus with:

```bash
python3 generate_corpus.py
```
