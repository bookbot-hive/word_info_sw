# Word Info SW

This library grabs multiple information of a Swahili word. Given a word, the library returns a Python dictionary containing:

| Key           | Value                     |
| ------------- | ------------------------- |
| `word`        | Word                      |
| `syllable`    | Word with syllable breaks |
| `ipa`         | IPA of word               |
| `description` | Description of word       |

## Installation

```sh
git clone https://github.com/bookbot-hive/word_info_sw.git
pip install word_info_sw/
```

## Usage

```py
from word_info_sw import get_word_info

print(get_word_info(["shule", "kiatu", "anapenda", "mtoto", "kisu", "mbwa", "tumbo", "mayai", "nyuma"], include_description=True))
>> [{'word': 'shule', 'syllable': 'shu.le', 'ipa': 'ʃu.lɛ', 'description': 'Shule ni mahali ambapo watoto hujifunza kusoma, kuandika na mambo mengine muhimu. Inajulikana pia kama skuli.'}, 
{'word': 'kiatu', 'syllable': 'ki.a.tu', 'ipa': 'ki.ɑ.tu', 'description': 'Kiatu ni kitu unachovaa mguuni ili kulinda miguu. Majina mengine ni viatu au raba.'},
{'word': 'anapenda', 'syllable': 'a.na.pe.nda', 'ipa': 'ɑ.nɑ.pɛ.ⁿɗɑ', 'description': '"Anapenda" ni neno la Kiswahili linalomaanisha mtu huyo anafurahia au anaipenda kitu. Maneno mengine ni "anapenda" and "anafurahia".'},
{'word': 'mtoto', 'syllable': 'm.to.to', 'ipa': 'm.tɔ.tɔ', 'description': 'Mtoto ni kijana mdogo ambaye hajakua mtu mzima. Majina mengine ni kijana mdogo au kitoto.'},
{'word': 'kisu', 'syllable': 'ki.su', 'ipa': 'ki.su', 'description': 'Kisu ni chombo cha kukata chakula. Ina ncha kali. Synonyma: cha mkate, panga ndogo.'},
{'word': 'mbwa', 'syllable': 'mbwa', 'ipa': 'ᵐɓwɑ', 'description': 'Mbwa ni mnyama rafiki wa binadamu, ana miguu minne na hupenda kucheza. Synonym: penjwa.'},
{'word': 'tumbo', 'syllable': 'tu.mbo', 'ipa': 'tu.ᵐɓɔ', 'description': 'Tumbo ni sehemu ya mwili ambapo chakula huenda baada ya kuliwa. Pia huitwa kiwili.'},
{'word': 'mayai', 'syllable': 'ma.ya.i', 'ipa': 'mɑ.jɑ.i', 'description': 'Mayai ni vitu vinavyotoka kwa ndege kama kuku, ambavyo tunapika na kula. Sinonim: viini.'},
{'word': 'nyuma', 'syllable': 'nyu.ma', 'ipa': 'nju.mɑ', 'description': '"Nyuma" inamaanisha sehemu ya nyuma ya kitu au mtu. Neno jingine ni "kigongo."'}]

print(get_word_info(['Usomaji', 'umekuwa', 'mafanikio', 'kwa', 'jumla', 'mahitaji', 'ya', 'mambo', 'ya', 'kusoma', 'yametokea', 'na', 'maduka', 'ya', 'vitabu', 'yaliyojaa', 'vitabu', 'yameonekana', 'kukidhi'], include_description=True))
>> [{'word': 'usomaji', 'syllable': 'u.so.ma.ji', 'ipa': 'u.sɔ.mɑ.ʄi', 'description': 'Usomaji ni kitendo cha kuangalia maneno kwenye kitabu na kuelewa maana yake. (Pia: Kusoma)'},
{'word': 'umekuwa', 'syllable': 'u.me.ku.wa', 'ipa': 'u.mɛ.ku.wɑ', 'description': '"Umekuwa" ni kusema umeendelea au umepanda hadhi. Maneno mengine ni kama "umekua" au "umekomaa".'},
{'word': 'mafanikio', 'syllable': 'ma.fa.ni.ki.o', 'ipa': 'mɑ.fɑ.ni.ki.ɔ', 'description': 'Mafanikio ni kufanikisha jambo unalotamani au kufanya vizuri. Maneno mengine ni ushindi, ufanisi.'},
{'word': 'kwa', 'syllable': 'kwa', 'ipa': 'kwɑ', 'description': '"Kwa" ina maana ya kuelekeza mahali, wakati, au sababu. Sinafawa: hadi, kwa ajili ya, kutokana na.'},
{'word': 'jumla', 'syllable': 'ju.mla', 'ipa': 'ʄu.mlɑ', 'description': 'Kwa Kiswahili, "jumla" inamaanisha idadi yote kwa pamoja. Synonyms: "kiasi chote," "ukamilifu."'},
{'word': 'mahitaji', 'syllable': 'ma.hi.ta.ji', 'ipa': 'mɑ.hi.tɑ.ʄi', 'description': 'Mahitaji ni vitu ambavyo mtu anahitaji ili kuishi, kama chakula, maji, na mavazi. (Synonyms: haja, kiinua)'},
{'word': 'ya', 'syllable': 'ya', 'ipa': 'jɑ', 'description': '"Ya" in Kiswahili ina maana ya "kitu cha" au "mali ya." Synonyms: "cha," "za."'},
{'word': 'mambo', 'syllable': 'ma.mbo', 'ipa': 'mɑ.ᵐɓɔ', 'description': '"Mambo" ni neno la Kiswahili linalomaanisha mawazo, mambo mazuri au hali. Linaweza pia kuitwa "hali."'},
{'word': 'ya', 'syllable': 'ya', 'ipa': 'jɑ', 'description': '"Ya" ni neno la kuunganisha vitu viwili. Inaweza kuwa na maana ya "la," "zilinazohusiana na," au "inayomilikiwa na."'},
{'word': 'kusoma', 'syllable': 'ku.so.ma', 'ipa': 'ku.sɔ.mɑ', 'description': 'Kusoma ni kujifunza kwa kubahatisha na kuelewa maneno kwenye vitabu. Maneno mengine: kusoma vitabu.'},
{'word': 'yametokea', 'syllable': 'ya.me.to.ke.a', 'ipa': 'jɑ.mɛ.tɔ.kɛ.ɑ', 'description': '"Yametokea" maana yake ni kitu kimefanyika au kimetukia. Maneno sawa ni kama "imejiri" au "limetendeka."'},
{'word': 'na', 'syllable': 'na', 'ipa': 'nɑ', 'description': '"Na" ni neno linalomaanisha "pamoja na" au "na". Sina viambishi vingine.'},
{'word': 'maduka', 'syllable': 'ma.du.ka', 'ipa': 'mɑ.ɗu.kɑ', 'description': '"Maduka" ni sehemu za kuuza vitu kama nguo na chakula. Synonyms: duka, biashara.'},
{'word': 'ya', 'syllable': 'ya', 'ipa': 'jɑ', 'description': '"Ya" inamaanisha "kitu kimoja ni cha kingine." Sawa na "la", "za," au "wa" kutegemea sentensi.'},
{'word': 'vitabu', 'syllable': 'vi.ta.bu', 'ipa': 'vi.tɑ.ɓu', 'description': 'Vitabu ni maandiko yaliyo na hadithi na picha, kama vile masomo au burudani. Sinonimo: machapisho, magazeti.'},
{'word': 'yaliyojaa', 'syllable': 'ya.li.yo.jaa', 'ipa': 'jɑ.li.jɔ.ʄɑɑ', 'description': '"Yaliyojaa" kwa Kiswahili ina maana ya kitu kilicho kamili na kimejaa. Maneno mengine ni "kimejaa" na "kimetapakaa".'},
{'word': 'vitabu', 'syllable': 'vi.ta.bu', 'ipa': 'vi.tɑ.ɓu', 'description': 'Vitabu ni vitu ambavyo tunasoma ili kujifunza na kujiburudisha. Synonyms: maqurasa, vitini.'},
{'word': 'yameonekana', 'syllable': 'ya.me.o.ne.ka.na', 'ipa': 'jɑ.mɛ.ɔ.nɛ.kɑ.nɑ', 'description': '"Yameonekana" inamaanisha kitu kimeweza kuonekana kwa macho. Kisawe ni "yamejionyesha."'},
{'word': 'kukidhi', 'syllable': 'ku.ki.dhi', 'ipa': 'ku.ki.ði', 'description': 'Kukidhi maana yake ni kutimiza mahitaji au matarajio. Maneno mengine ni kama kuelekea au kufikia.'}]
```

## Algorithm

1. Getting Syllable Breaks of Word
   1. Syllabize using algorithm.
2. Getting IPA of Word
   1. Phonemize word using [gruut](https://github.com/rhasspy/gruut).
3. Getting Word description
   1. Using GPT-4 API, generate the word description using the prompt *"Define, in Kiswahili, \"{word}\" within 12 to 20 words for a 5 year old"*.