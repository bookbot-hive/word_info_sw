from gruut import sentences
from typing import List, Dict
import re

VALID_SYLLABLES = set(
    [
        "mbwa",
        "mbwe",
        "mbwi",
        "ndwa",
        "ndwe",
        "ndwi",
        "ngwa",
        "ngwe",
        "ngwi",
        "njwa",
        "njwe",
        "njwi",
        "nywa",
        "nywe",
        "shwa",
        "shwe",
        "shwi",
        "chwa",
        "chwe",
        "chwi",
        "pwa",
        "pwe",
        "pwi",
        "pwo",
        "swa",
        "swe",
        "swi",
        "twa",
        "twe",
        "twi",
        "zwa",
        "zwe",
        "zwi",
        "cha",
        "che",
        "chi",
        "cho",
        "chu",
        "dha",
        "dhe",
        "dhi",
        "dho",
        "dhu",
        "gha",
        "ghe",
        "ghi",
        "gho",
        "ghu",
        "kha",
        "khe",
        "kho",
        "khu",
        "mba",
        "mbe",
        "mbi",
        "mbo",
        "mbu",
        "nda",
        "nde",
        "ndi",
        "ndo",
        "ndu",
        "nga",
        "nge",
        "ngi",
        "ngo",
        "ngu",
        "ng'a",
        "ng'e",
        "ng'o",
        "nja",
        "nje",
        "nji",
        "njo",
        "nju",
        "nya",
        "nye",
        "nyi",
        "nyo",
        "nyu",
        "sha",
        "she",
        "shi",
        "sho",
        "shu",
        "tha",
        "the",
        "thi",
        "tho",
        "thu",
        "vya",
        "vye",
        "vyo",
        "bwa",
        "bwe",
        "bwi",
        "gwa",
        "gwe",
        "gwi",
        "jwa",
        "jwe",
        "jwi",
        "kwa",
        "kwe",
        "kwi",
        "lwa",
        "lwe",
        "lwi",
        "mwa",
        "mwe",
        "mwi",
        "nza",
        "nze",
        "nzi",
        "nzo",
        "nzu",
        "ba",
        "be",
        "bi",
        "bo",
        "bu",
        "da",
        "de",
        "di",
        "do",
        "du",
        "fa",
        "fe",
        "fi",
        "fo",
        "fu",
        "ga",
        "ge",
        "gi",
        "go",
        "gu",
        "ha",
        "he",
        "hi",
        "ho",
        "hu",
        "ja",
        "je",
        "ji",
        "jo",
        "ju",
        "ka",
        "ke",
        "ki",
        "ko",
        "ku",
        "la",
        "le",
        "li",
        "lo",
        "lu",
        "ma",
        "me",
        "mi",
        "mo",
        "mu",
        "na",
        "ne",
        "ni",
        "no",
        "nu",
        "pa",
        "pe",
        "pi",
        "po",
        "pu",
        "ra",
        "re",
        "ri",
        "ro",
        "ru",
        "sa",
        "se",
        "si",
        "so",
        "su",
        "ta",
        "te",
        "ti",
        "to",
        "tu",
        "va",
        "ve",
        "vi",
        "vo",
        "vu",
        "wa",
        "we",
        "wi",
        "wo",
        "wu",
        "ya",
        "ye",
        "yi",
        "yo",
        "yu",
        "za",
        "ze",
        "zi",
        "zo",
        "zu",
        "a",
        "e",
        "i",
        "o",
        "u",
        "b",
        "d",
        "f",
        "k",
        "m",
        "n",
        "s",
    ]
)


def get_word_info(words: List[str]) -> List[Dict[str, str]]:
    """
    Gets multiple information of a word.

    Returns a dictionary of:
    | Key           | Value                     |
    | ------------- | ------------------------- |
    | `word`        | Word                      |
    | `syllable`    | Word with syllable breaks |
    | `ipa`         | IPA of word               |

    Args:
        words (List[str]):
            Strings of words.

    Returns:
        List[Dict[str, str]]:
            List of dictionaries containing the word's information.
    """
    results = []

    for word in words:
        word = word.lower().replace("’", "'")
        ipa = get_ipa(word)

        if word.isnumeric():
            syllable = word
        else:
            syllable = get_syllable(word)

        ipa = syllabize_ipa(syllable, ipa)

        row = {
            "word": word,
            "syllable": syllable,
            "ipa": ipa,
        }
        results.append(row)
    return results


def get_ipa(word: str) -> str:
    """Phonemizes a word using gruut.

    Args:
        word (str): Word to phonemize.

    Returns:
        str: Whitespace-separated IPAs.
    """
    ipa = []
    for words in sentences(word, lang="sw"):
        for word in words:
            phonemes = word.phonemes[:]

            # NOTE: gruut doesn't handle "ng'" /ŋ/
            # we need to fix e.g. ng'ombe -> /ŋombe/ instead of /ᵑgombe/
            NG_GRAPHEME = "ng'"
            NG_PRENASALIZED_PHONEME = "ᵑg"
            NG_PHONEME = "ŋ"
            if NG_GRAPHEME in word.text:
                ng_graphemes = re.findall(f"{NG_GRAPHEME}?", word.text)
                ng_phonemes_idx = [i for i, p in enumerate(phonemes) if p == NG_PRENASALIZED_PHONEME]
                assert len(ng_graphemes) == len(ng_phonemes_idx)
                for i, g in zip(ng_phonemes_idx, ng_graphemes):
                    phonemes[i] = NG_PHONEME if g == NG_GRAPHEME else phonemes[i]

            ipa += phonemes

    ipa = " ".join(ipa)
    return ipa


def get_syllable(word: str) -> str:
    vowels = set("aeiou")
    semi_vowels = set("yw")
    nasals = set("mn")
    prenasal_consonants = {
        "m": set("bv"),
        "n": set("dgjz"),
    }
    syllables = []
    current_syllable = ""

    # Replace "ng'" with a "ŋ" character
    word = word.replace("ng'", "ŋ")

    for i, char in enumerate(word[::-1]):
        # vowels indicate the start of a new syllable
        if char in vowels:
            # restart the current syllable if it's a vowel,
            # unless current syllable is a nasal, or is the same repeated vowel
            if current_syllable and current_syllable not in nasals and current_syllable != char:
                syllables.insert(0, current_syllable)
                current_syllable = ""
            # start a new syllable with the vowel
            current_syllable = char + current_syllable
        else:
            # if it's a nasal, add it to the current syllable and start a new one
            # only valid if nasal is the first letter in the word
            if (
                char in nasals
                and i == len(word) - 1  # check if first
                and current_syllable
                and current_syllable[0] not in vowels  # not followed a vowel
                and current_syllable[0] not in semi_vowels  # not followed a semi-vowel
                and current_syllable[0] not in prenasal_consonants[char]  # not followed by a prenasal consonant
            ):
                syllables.insert(0, current_syllable)
                current_syllable = char
            else:
                # continue current syllable
                if current_syllable:
                    current_syllable = char + current_syllable
                # start a new one
                else:
                    current_syllable = char

        # check if it's the last character in the word to ensure the last syllable is added
        if i == len(word) - 1 and current_syllable:
            syllables.insert(0, current_syllable)

    # Replace "ŋ" back with "ng'"
    syllables = [syl.replace("ŋ", "ng'") for syl in syllables]

    return ".".join(syllables)


def syllabize_ipa(syllable: str, ipa: str):
    grapheme = syllable
    phonemes = ipa.split()
    num_phonemes = len(phonemes)
    num_char = len([c for c in grapheme if c != "."])
    # if phonemes and graphemes don't map 1:1
    # remap to make 1:1
    if num_phonemes != num_char:
        if "ð" in phonemes and "dh" in grapheme:
            grapheme = grapheme.replace("dh", "ð")
        if "θ" in phonemes and "th" in grapheme:
            grapheme = grapheme.replace("th", "θ")
        if "t͡ʃ" in phonemes and "ch" in grapheme:
            grapheme = grapheme.replace("ch", "t")
        if "ɣ" in phonemes and "gh" in grapheme:
            grapheme = grapheme.replace("gh", "ɣ")
        if "x" in phonemes and "kh" in grapheme:
            grapheme = grapheme.replace("kh", "x")
        if "ʃ" in phonemes and "sh" in grapheme:
            grapheme = grapheme.replace("sh", "ʃ")
        if "ⁿɗ͡ʒ" in phonemes and "nj" in grapheme:
            grapheme = grapheme.replace("nj", "ⁿ")
        if "ⁿz" in phonemes and "nz" in grapheme:
            grapheme = grapheme.replace("nz", "ⁿ")
        if "ŋ" in phonemes and "ng'" in grapheme:
            grapheme = grapheme.replace("ng'", "ŋ")
        if "ᵑg" in phonemes and "ng" in grapheme:
            grapheme = grapheme.replace("ng", "ᵑ")
        if "ᶬv" in phonemes and "mv" in grapheme:
            grapheme = grapheme.replace("mv", "ᶬ")
        if "ᵐɓ" in phonemes and "mb" in grapheme:
            grapheme = grapheme.replace("mb", "ᵐ")
        if "ⁿɗ" in phonemes and "nd" in grapheme:
            grapheme = grapheme.replace("nd", "ⁿ")

    # insert . where . is in syllable
    dot_indices = [i for i, c in enumerate(grapheme) if c == "."]
    for i in dot_indices:
        phonemes.insert(i, ".")
    phonemes = "".join(phonemes)

    return phonemes


if __name__ == "__main__":
    print(get_word_info(["saa"]))
    print(get_word_info(["shule", "kiatu", "anapenda", "mtoto", "kisu", "mbwa", "tumbo", "mayai", "nyuma"]))
    print(
        get_word_info(
            [
                "Usomaji",
                "umekuwa",
                "mafanikio",
                "kwa",
                "jumla",
                "mahitaji",
                "ya",
                "mambo",
                "ya",
                "kusoma",
                "yametokea",
                "na",
                "maduka",
                "ya",
                "vitabu",
                "yaliyojaa",
                "vitabu",
                "yameonekana",
                "kukidhi",
            ]
        )
    )
