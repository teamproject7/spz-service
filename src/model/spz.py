import random
import re
import rstr

# https://sk.wikipedia.org/wiki/Eviden%C4%8Dn%C3%A9_%C4%8D%C3%ADslo_(vozidl%C3%A1_sveta)
# https://www.minv.sk/?vzory-tabuliek-s-evidencnym-cislom-pridelovane-na-vozidla
# https://autobild.cas.sk/clanok/200555/11-veci-ktore-zrejme-neviete-o-spz-kach/, Podľa jej údajov k 28. marcu 2015 bolo na Slovensku evidovaných celkovo 2 736 108 vozidiel.
# http://www.servis-auto-moto.sk/spz-ecv-tec-zoznam-okresov-slovenska/
okresy = [
    'BA', 'BL', 'MA', 'PK', 'SC',
    'TT', 'TA', 'DS', 'GA', 'HC', 'PN', 'SE', 'SI',
    'TN', 'BN', 'IL', 'MY', 'NM', 'PE', 'PB', 'PD', 'PU',
    'BB', 'BC', 'BS', 'BR', 'LC', 'DT', 'KA', 'PT', 'RA', 'RS', 'VK', 'ZV', 'ZC', 'ZH',
    'ZA', 'ZI', 'BY', 'CA', 'DK', 'KM', 'LM', 'MT', 'NO', 'RK', 'TR', 'TS',
    'NR', 'NI', 'KO', 'LV', 'NZ', 'SA', 'TO', 'ZM',
    'LE', 'PO', 'PV', 'BJ', 'HE', 'KK', 'ML', 'PP', 'SB', 'SV', 'SL', 'SP', 'SK', 'VT',
    'KE', 'KI', 'KS', 'GL', 'MI', 'RV', 'SO', 'SN', 'TV'
]

# 1. format z https://www.minv.sk/?vzory-tabuliek-s-evidencnym-cislom-pridelovane-na-vozidla
SPZ_SUFFIX_FORMAT = r'^[0-9]{3}[A-Z]{2}$'
SPZ_SEPARATOR = '-'
# 45 504 000
SPZ_TOTAL_COUNT = len(okresy) * 10 * 10 * 10 * 24 * 24


def meets_spz_format(spz):
    spz_parts = spz.split(SPZ_SEPARATOR)
    if len(spz_parts) != 2:
        return False

    valid_prefix = spz_parts[0] in okresy
    valid_suffix = bool(re.compile(SPZ_SUFFIX_FORMAT).search(spz_parts[1]))

    return (valid_prefix and valid_suffix)


def generate_spz():
    return "{}{}{}".format(random.choice(okresy), SPZ_SEPARATOR, rstr.xeger(SPZ_SUFFIX_FORMAT))
