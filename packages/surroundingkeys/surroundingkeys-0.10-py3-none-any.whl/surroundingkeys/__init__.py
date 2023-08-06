from collections import defaultdict

from cachetools.func import lru_cache
import pandas as pd
import os
from a_pandas_ex_closest_neighbours import pd_add_closest_neighbours

pd_add_closest_neighbours()


def convert_to_dict(di):
    if isinstance(di, dict) or (
        hasattr(di, "items") and hasattr(di, "keys") and hasattr(di, "values")
    ):
        di = {k: convert_to_dict(v) for k, v in di.items()}
    return di


@lru_cache
def get_unicode_name(letter):
    return "U+" + hex(ord(str(letter).lower()))[2:].zfill(4).upper()


def show_all_keyboards():
    for name, ident in allkeyb:
        print(ident.ljust(20) + f"{name}")


@lru_cache
def get_next_letters(letter, keyboard):
    r"""
    A utility function to find the closest neighboring keys of a given letter on a specific keyboard layout.

    Parameters:
    -----------
    letter : str
        The letter for which to find the neighboring keys.
    keyboard : str
        The keyboard layout identifier. Should be one of the identifiers shown when you call show_all_keyboards().

    Returns:
    --------
    dict
        A dictionary containing the neighboring keys of the input letter on the specified keyboard layout.
        The dictionary has the following structure:
        {
            'input_letter': {
                'side': [list of letters on the left and right sides],
                'top': [list of letters above the input letter],
                'bottom': [list of letters below the input letter]
            }
        }
        If no neighboring keys are found or the input letter is not available on the specified keyboard layout,
        the corresponding list will be empty.

    Example:
    --------
        from surroundingkeys import get_next_letters, show_all_keyboards
        for letter in 'Oi, tudo bem?':
            result = get_next_letters(letter=letter, keyboard="kbdbr_1")
            print(result)
            print(letter)
        {'O': {'side': ['I', 'P'], 'top': ['9', '0'], 'bottom': ['K', 'L']}}
        O
        {'i': {'side': ['u', 'o'], 'top': ['8', '9'], 'bottom': ['j', 'k']}}
        i
        {',': {'side': ['m', '.'], 'top': ['k', 'l'], 'bottom': []}}
        ,
        {' ': {'side': [], 'top': [], 'bottom': []}}

        {'t': {'side': ['r', 'y'], 'top': ['5', '6'], 'bottom': ['f', 'g']}}
        t
        {'u': {'side': ['y', 'i'], 'top': ['7', '8'], 'bottom': ['h', 'j']}}
        u
        {'d': {'side': ['s', 'f'], 'top': ['e', 'r'], 'bottom': ['x', 'c']}}
        d
        {'o': {'side': ['i', 'p'], 'top': ['9', '0'], 'bottom': ['k', 'l']}}
        o
        {' ': {'side': [], 'top': [], 'bottom': []}}

        {'b': {'side': ['v', 'n'], 'top': ['g', 'h'], 'bottom': []}}
        b
        {'e': {'side': ['w', 'r'], 'top': ['3', '4'], 'bottom': ['s', 'd']}}
        e
        {'m': {'side': ['n', ','], 'top': ['j', 'k'], 'bottom': []}}
        m
        {'?': {'side': [], 'top': [], 'bottom': []}}
        ?


    Note:
    -----
    This function uses a cache (LRU cache) to speed up repeated calls with the same inputs.
    """

    letteroriginal = letter
    letter = letter.lower()
    filepath = os.path.join(
        os.sep.join((__file__.split(os.sep)[:-1])), keyboard + ".pkl"
    )
    if not os.path.exists(filepath):
        show_all_keyboards()
        raise ValueError("Please choose a valid keyboard")
    df2 = pd.read_pickle(filepath)
    changeorder = False

    if len(df2.height.unique()) > 1:
        changeorder = True
    df = df2.loc[df2[1].str.startswith("U+")].reset_index(drop=True)
    if changeorder:
        maxtoaugment = df.loc[~(df.y == df.y.max()), "y"].max()

        df.loc[df.y == maxtoaugment, "y"] += 100

    letteronkeyboard = df.loc[df[1].str[:6] == get_unicode_name(letter)]
    dfwithoutletter = df.loc[df.index.drop(letteronkeyboard.index)]

    allresults = []
    for name, group in dfwithoutletter.groupby("y"):
        try:
            min_neighbour, max_neighbour = group.x.s_find_closest_neighbours(
                value=letteronkeyboard.x.iloc[0],
                convertdtypes=False,
                accept_exact_match=True,
            )
        except Exception:
            return {letteroriginal: {"side": [], "top": [], "bottom": []}}
        try:
            allresults.append(group.loc[min_neighbour.lower_index.iloc[0]])
        except Exception as fe:
            pass
        try:
            allresults.append(group.loc[max_neighbour.upper_index.iloc[0]])
        except Exception as fe:
            pass
    dfn = pd.concat(allresults, axis=1).T
    allsurroundingkeys = [dfn.loc[dfn.y == letteronkeyboard.y.iloc[0]][:2].copy()]
    dfn = dfn.drop(allsurroundingkeys[-1].index)
    allsurroundingkeys[-1] = allsurroundingkeys[-1].assign(letterpos="side")

    try:
        allsurroundingkeys.append(
            dfn.loc[
                dfn.y
                == (
                    dfn.loc[dfn.y < letteronkeyboard.y.iloc[0]]
                    .sort_values(by="y", ascending=False)[:1]
                    .y.iloc[0]
                )
            ].copy()
        )
        dfn = dfn.drop(allsurroundingkeys[-1].index)
        allsurroundingkeys[-1] = allsurroundingkeys[-1].assign(letterpos="top")

    except Exception:
        pass

    try:
        allsurroundingkeys.append(
            dfn.loc[
                dfn.y
                == (
                    dfn.loc[dfn.y > letteronkeyboard.y.iloc[0]]
                    .sort_values(by="y", ascending=True)[:1]
                    .y.iloc[0]
                )
            ].copy()
        )
        allsurroundingkeys[-1] = allsurroundingkeys[-1].assign(letterpos="bottom")

    except Exception:
        pass

    allsurroundingkeystog = pd.concat(allsurroundingkeys)
    allsurroundingkeystog["letterfinal"] = allsurroundingkeystog[1].apply(
        lambda x: eval(r'"\u' + x[2:6] + '"')
    )

    finaldict = defaultdict(list)
    for key in ["side", "top", "bottom"]:
        finaldict[key].extend(
            allsurroundingkeystog.loc[
                allsurroundingkeystog.letterpos == key
            ].letterfinal.to_list()
        )
        if letteroriginal.isupper():
            finaldict[key] = [x.upper() for x in finaldict[key]]
    return {letteroriginal: convert_to_dict(finaldict)}


allkeyb = [
    ("ADLaM", "kbdadlm"),
    ("Albanian", "kbdal"),
    ("Arabic (101)", "kbda1"),
    ("Arabic (102)", "kbda2"),
    ("Arabic (102) AZERTY", "kbda3"),
    ("Armenian Eastern (Legacy)", "kbdarme"),
    ("Armenian Phonetic", "kbdarmph"),
    ("Armenian Typewriter", "kbdarmty"),
    ("Armenian Western (Legacy)", "kbdarmw"),
    ("Assamese - INSCRIPT", "kbdinasa"),
    ("Azerbaijani (Standard)", "kbdazst"),
    ("Azerbaijani Cyrillic", "kbdaze"),
    ("Azerbaijani Latin", "kbdazel"),
    ("Bangla", "kbdinben"),
    ("Bangla - INSCRIPT", "kbdinbe2"),
    ("Bangla - INSCRIPT (Legacy)", "kbdinbe1"),
    ("Bashkir", "kbdbash"),
    ("Belarusian", "kbdblr"),
    ("Belgian (Comma)", "kbdbene"),
    ("Belgian (Period)", "kbdbe_1"),
    ("Belgian French", "kbdbe_2"),
    ("Bosnian (Cyrillic)", "kbdbhc"),
    ("Buginese", "kbdbug"),
    ("Bulgarian", "kbdbulg"),
    ("Bulgarian (Latin)", "kbdus_1"),
    ("Bulgarian (Phonetic Traditional)", "kbdbgph1"),
    ("Bulgarian (Phonetic)", "kbdbgph"),
    ("Bulgarian (Typewriter)", "kbdbu"),
    ("Canadian French", "kbdca"),
    ("Canadian French (Legacy)", "kbdfc"),
    ("Canadian Multilingual Standard", "kbdcan"),
    ("Central Atlas Tamazight", "kbdtzm"),
    ("Central Kurdish", "kbdkurd"),
    ("Cherokee Nation", "kbdcher"),
    ("Cherokee Phonetic", "kbdcherp"),
    ("Chinese (Simplified) - US", "kbdus_2"),
    ("Chinese (Simplified, Singapore) - US", "kbdus_3"),
    ("Chinese (Traditional) - US", "kbdus_4"),
    ("Chinese (Traditional, Hong Kong S.A.R.) - US", "kbdus_5"),
    ("Chinese (Traditional, Macao S.A.R.) - US", "kbdus_6"),
    ("Czech", "kbdcz"),
    ("Czech (QWERTY)", "kbdcz1"),
    ("Czech Programmers", "kbdcz2"),
    ("Danish", "kbdda"),
    ("Devanagari - INSCRIPT", "kbdindev"),
    ("Divehi Phonetic", "kbddiv1"),
    ("Divehi Typewriter", "kbddiv2"),
    ("Dutch", "kbdne"),
    ("Dzongkha", "kbddzo"),
    ("English (India)", "kbdinen"),
    ("Estonian", "kbdest"),
    ("Faeroese", "kbdfo"),
    ("Finnish", "kbdfi"),
    ("Finnish with Sami", "kbdfi1_1"),
    ("French", "kbdfr"),
    ("Futhark", "kbdfthrk"),
    ("Georgian (Ergonomic)", "kbdgeoer"),
    ("Georgian (Legacy)", "kbdgeo"),
    ("Georgian (MES)", "kbdgeome"),
    ("Georgian (Old Alphabets)", "kbdgeooa"),
    ("Georgian (QWERTY)", "kbdgeoqw"),
    ("German", "kbdgr"),
    ("German (IBM)", "kbdgr1"),
    ("Gothic", "kbdgthc"),
    ("Greek", "kbdhe"),
    ("Greek (220)", "kbdhe220"),
    ("Greek (220) Latin", "kbdhela2"),
    ("Greek (319)", "kbdhe319"),
    ("Greek (319) Latin", "kbdhela3"),
    ("Greek Latin", "kbdgkl"),
    ("Greek Polytonic", "kbdhept"),
    ("Greenlandic", "kbdgrlnd"),
    ("Guarani", "kbdgn"),
    ("Gujarati", "kbdinguj"),
    ("Hausa", "kbdhau"),
    ("Hawaiian", "kbdhaw"),
    ("Hebrew", "kbdheb"),
    ("Hebrew (Standard)", "kbdhebl3"),
    ("Hindi Traditional", "kbdinhin"),
    ("Hungarian", "kbdhu"),
    ("Hungarian 101-key", "kbdhu1"),
    ("Icelandic", "kbdic"),
    ("Igbo", "kbdibo"),
    ("Inuktitut - Latin", "kbdiulat"),
    ("Inuktitut - Naqittaut", "kbdinuk2"),
    ("Irish", "kbdir"),
    ("Italian", "kbdit"),
    ("Italian (142)", "kbdit142"),
    ("Japanese", "kbdjpn"),
    ("Javanese", "kbdjav"),
    ("Kannada", "kbdinkan"),
    ("Kazakh", "kbdkaz"),
    ("Khmer", "kbdkhmr"),
    ("Khmer (NIDA)", "kbdkni"),
    ("Korean", "kbdkor"),
    ("Kyrgyz Cyrillic", "kbdkyr"),
    ("Lao", "kbdlao"),
    ("Latin American", "kbdla"),
    ("Latvian", "kbdlv"),
    ("Latvian (QWERTY)", "kbdlv1"),
    ("Latvian (Standard)", "kbdlvst"),
    ("Lisu (Basic)", "kbdlisub"),
    ("Lisu (Standard)", "kbdlisus"),
    ("Lithuanian", "kbdlt1"),
    ("Lithuanian IBM", "kbdlt"),
    ("Lithuanian Standard", "kbdlt2"),
    ("Luxembourgish", "kbdsf_1"),
    ("Macedonian (North Macedonia)", "kbdmac"),
    ("Macedonian (North Macedonia) - Standard", "kbdmacst"),
    ("Malayalam", "kbdinmal"),
    ("Maltese 47-Key", "kbdmlt47"),
    ("Maltese 48-Key", "kbdmlt48"),
    ("Maori", "kbdmaori"),
    ("Marathi", "kbdinmar"),
    ("Mongolian (Mongolian Script)", "kbdmonmo"),
    ("Mongolian Cyrillic", "kbdmon"),
    ("Myanmar (Phonetic order)", "kbdmyan_1"),
    ("Myanmar (Visual order)", "kbdmyan_2"),
    ("Nepali", "kbdnepr"),
    ("New Tai Lue", "kbdntl"),
    ("N’Ko", "kbdnko"),
    ("Norwegian", "kbdno"),
    ("Norwegian with Sami", "kbdno1"),
    ("NZ Aotearoa", "kbdmaori_nzaotearoa"),
    ("Odia", "kbdinori"),
    ("Ogham", "kbdogham"),
    ("Ol Chiki", "kbdolch"),
    ("Old Italic", "kbdoldit"),
    ("Osage", "kbdosa"),
    ("Osmanya", "kbdosm"),
    ("Pashto (Afghanistan)", "kbdpash"),
    ("Persian", "kbdfa"),
    ("Persian (Standard)", "kbdfar"),
    ("Phags-pa", "kbdphags"),
    ("Polish (214)", "kbdpl"),
    ("Polish (Programmers)", "kbdpl1"),
    ("Portuguese", "kbdpo"),
    ("Portuguese (Brazil ABNT)", "kbdbr_1"),
    ("Portuguese (Brazil ABNT2)", "kbdbr_2"),
    ("Punjabi", "kbdinpun"),
    ("Romanian (Legacy)", "kbdro"),
    ("Romanian (Programmers)", "kbdropr"),
    ("Romanian (Standard)", "kbdrost"),
    ("Russian", "kbdru"),
    ("Russian - Mnemonic", "kbdrum"),
    ("Russian (Typewriter)", "kbdru1"),
    ("Sakha", "kbdyak"),
    ("Sami Extended Finland-Sweden", "kbdsmsfi"),
    ("Sami Extended Norway", "kbdsmsno"),
    ("Scottish Gaelic", "kbdgae"),
    ("Serbian (Cyrillic)", "kbdycc"),
    ("Serbian (Latin)", "kbdycl"),
    ("Sesotho sa Leboa", "kbdnso_1"),
    ("Setswana", "kbdnso_2"),
    ("Sinhala", "kbdsn1"),
    ("Sinhala - Wij 9", "kbdsw09"),
    ("Slovak", "kbdsl"),
    ("Slovak (QWERTY)", "kbdsl1"),
    ("Slovenian", "kbdcr_1"),
    ("Sora", "kbdsora"),
    ("Sorbian Extended", "kbdsorex"),
    ("Sorbian Standard", "kbdsors1"),
    ("Sorbian Standard (Legacy)", "kbdsorst"),
    ("Spanish", "kbdsp"),
    ("Spanish Variation", "kbdes"),
    ("Standard", "kbdcr_2"),
    ("Swedish", "kbdsw"),
    ("Swedish with Sami", "kbdfi1_2"),
    ("Swiss French", "kbdsf_2"),
    ("Swiss German", "kbdsg"),
    ("Syriac", "kbdsyr1"),
    ("Syriac Phonetic", "kbdsyr2"),
    ("Tai Le", "kbdtaile"),
    ("Tajik", "kbdtajik"),
    ("Tamil", "kbdintam"),
    ("Tamil 99", "kbdtam99"),
    ("Tamil Anjal", "kbdinen_tamilanjal"),
    ("Tatar", "kbdtt102"),
    ("Tatar (Legacy)", "kbdtat"),
    ("Telugu", "kbdintel"),
    ("Thai Kedmanee", "kbdth0"),
    ("Thai Kedmanee (non-ShiftLock)", "kbdth2"),
    ("Thai Pattachote", "kbdth1"),
    ("Thai Pattachote (non-ShiftLock)", "kbdth3"),
    ("Tibetan (PRC)", "kbdtiprc"),
    ("Tibetan (PRC) - Updated", "kbdtiprd"),
    ("Tifinagh (Basic)", "kbdtifi"),
    ("Tifinagh (Extended)", "kbdtifi2"),
    ("Traditional Mongolian (Standard)", "kbdmonst"),
    ("Turkish F", "kbdtuf"),
    ("Turkish Q", "kbdtuq"),
    ("Turkmen", "kbdturme"),
    ("Ukrainian", "kbdur"),
    ("Ukrainian (Enhanced)", "kbdur1"),
    ("United Kingdom", "kbduk"),
    ("United Kingdom Extended", "kbdukx"),
    ("United States-Dvorak", "kbddv"),
    ("United States-Dvorak for left hand", "kbdusl"),
    ("United States-Dvorak for right hand", "kbdusr"),
    ("United States-International", "kbdusx"),
    ("Urdu", "kbdurdu"),
    ("US", "kbdus_7"),
    ("US English Table for IBM Arabic 238_L", "kbdusa"),
    ("Uyghur", "kbdughr1"),
    ("Uyghur (Legacy)", "kbdughr"),
    ("Uzbek Cyrillic", "kbduzb"),
    ("Vietnamese", "kbdvntc"),
    ("Wolof", "kbdwol"),
    ("Yoruba", "kbdyba"),
]
