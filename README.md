# Word Info SW

This library grabs multiple information of a Swahili word. Given a word, the library returns a Python dictionary containing:

| Key        | Value                     |
| ---------- | ------------------------- |
| `word`     | Word                      |
| `syllable` | Word with syllable breaks |
| `ipa`      | IPA of word               |

## Installation

```sh
git clone https://github.com/bookbot-hive/word_info_sw.git
pip install word_info_sw/requirements.txt
```

## Usage

```py
from word_info_sw import get_word_info

print(get_word_info(["shule", "kiatu", "anapenda", "mtoto", "kisu", "mbwa", "tumbo", "mayai", "nyuma"]))
>> [{'word': 'shule', 'syllable': 'shu.le', 'ipa': 'ʃ u l ɛ'},
{'word': 'kiatu', 'syllable': 'ki.a.tu', 'ipa': 'k i ɑ t u'},
{'word': 'anapenda', 'syllable': 'a.na.pe.nda', 'ipa': 'ɑ n ɑ p ɛ ⁿɗ ɑ'},
{'word': 'mtoto', 'syllable': 'm.to.to', 'ipa': 'm t ɔ t ɔ'},
{'word': 'kisu', 'syllable': 'ki.su', 'ipa': 'k i s u'},
{'word': 'mbwa', 'syllable': 'm.bwa', 'ipa': 'ᵐɓ w ɑ'},
{'word': 'tumbo', 'syllable': 'tu.mbo', 'ipa': 't u ᵐɓ ɔ'},
{'word': 'mayai', 'syllable': 'ma.ya.i', 'ipa': 'm ɑ j ɑ i'},
{'word': 'nyuma', 'syllable': 'nyu.ma', 'ipa': 'n j u m ɑ'}]

print(get_word_info(['Usomaji', 'umekuwa', 'mafanikio', 'kwa', 'jumla', 'mahitaji', 'ya', 'mambo', 'ya', 'kusoma', 'yametokea', 'na', 'maduka', 'ya', 'vitabu', 'yaliyojaa', 'vitabu', 'yameonekana', 'kukidhi']))
>> [{'word': 'usomaji', 'syllable': 'u.so.ma.ji', 'ipa': 'u s ɔ m ɑ ʄ i'},
{'word': 'umekuwa', 'syllable': 'u.me.ku.wa', 'ipa': 'u m ɛ k u w ɑ'},
{'word': 'mafanikio', 'syllable': 'ma.fa.ni.ki.o', 'ipa': 'm ɑ f ɑ n i k i ɔ'},
{'word': 'kwa', 'syllable': 'kwa', 'ipa': 'k w ɑ'},
{'word': 'jumla', 'syllable': 'ju.mla', 'ipa': 'ʄ u m l ɑ'},
{'word': 'mahitaji', 'syllable': 'ma.hi.ta.ji', 'ipa': 'm ɑ h i t ɑ ʄ i'},
{'word': 'ya', 'syllable': 'ya', 'ipa': 'j ɑ'},
{'word': 'mambo', 'syllable': 'ma.mbo', 'ipa': 'm ɑ ᵐɓ ɔ'},
{'word': 'ya', 'syllable': 'ya', 'ipa': 'j ɑ'},
{'word': 'kusoma', 'syllable': 'ku.so.ma', 'ipa': 'k u s ɔ m ɑ'},
{'word': 'yametokea', 'syllable': 'ya.me.to.ke.a', 'ipa': 'j ɑ m ɛ t ɔ k ɛ ɑ'},
{'word': 'na', 'syllable': 'na', 'ipa': 'n ɑ'},
{'word': 'maduka', 'syllable': 'ma.du.ka', 'ipa': 'm ɑ ɗ u k ɑ'},
{'word': 'ya', 'syllable': 'ya', 'ipa': 'j ɑ'},
{'word': 'vitabu', 'syllable': 'vi.ta.bu', 'ipa': 'v i t ɑ ɓ u'},
{'word': 'yaliyojaa', 'syllable': 'ya.li.yo.ja.a', 'ipa': 'j ɑ l i j ɔ ʄ ɑ ɑ'},
{'word': 'vitabu', 'syllable': 'vi.ta.bu', 'ipa': 'v i t ɑ ɓ u'},
{'word': 'yameonekana', 'syllable': 'ya.me.o.ne.ka.na', 'ipa': 'j ɑ m ɛ ɔ n ɛ k ɑ n ɑ'},
{'word': 'kukidhi', 'syllable': 'ku.ki.dhi', 'ipa': 'k u k i ð i'}]
```

## Algorithm

1. Getting Syllable Breaks of Word
   1. Syllabize using algorithm.
2. Getting IPA of Word
   1. Phonemize word using [gruut](https://github.com/rhasspy/gruut).