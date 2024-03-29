from gruut import sentences
from typing import List, Dict

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
        word = word.lower()
        ipa = get_ipa(word)

        if word.isnumeric():
            syllable = word
        else:
            syllable = get_syllable(word)

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
    ipa = " ".join([p for phns in sentences(word, lang="sw") for phn in phns for p in phn.phonemes])
    return ipa


def get_syllable(word: str) -> str:
    vowels = set("aeiou")
    semi_vowels = set("yw")
    nasals = set("mn")
    syllables = []
    current_syllable = ""

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
                and i == len(word) - 1
                and current_syllable
                and current_syllable[0] not in vowels
                and current_syllable[0] not in semi_vowels
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

    # TODO: check if all syllables are valid
    # for syllable in syllables:
    #     if syllable not in VALID_SYLLABLES:
    #         print("Warning: Invalid syllable found: " + syllable)

    return ".".join(syllables)


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
