# Copyright 2016 Tesora, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


charset = {"big5": ["big5_chinese_ci", "big5_bin"],
           "dec8": ["dec8_swedish_ci", "dec8_bin"],
           "cp850": ["cp850_general_ci", "cp850_bin"],
           "hp8": ["hp8_english_ci", "hp8_bin"],
           "koi8r": ["koi8r_general_ci", "koi8r_bin"],
           "latin1": ["latin1_swedish_ci",
                      "latin1_german1_ci",
                      "latin1_danish_ci",
                      "latin1_german2_ci",
                      "latin1_bin",
                      "latin1_general_ci",
                      "latin1_general_cs",
                      "latin1_spanish_ci"],
           "latin2": ["latin2_general_ci",
                      "latin2_czech_cs",
                      "latin2_hungarian_ci",
                      "latin2_croatian_ci",
                      "latin2_bin"],
           "swe7": ["swe7_swedish_ci", "swe7_bin"],
           "ascii": ["ascii_general_ci", "ascii_bin"],
           "ujis": ["ujis_japanese_ci", "ujis_bin"],
           "sjis": ["sjis_japanese_ci", "sjis_bin"],
           "hebrew": ["hebrew_general_ci", "hebrew_bin"],
           "tis620": ["tis620_thai_ci", "tis620_bin"],
           "euckr": ["euckr_korean_ci", "euckr_bin"],
           "koi8u": ["koi8u_general_ci", "koi8u_bin"],
           "gb2312": ["gb2312_chinese_ci", "gb2312_bin"],
           "greek": ["greek_general_ci", "greek_bin"],
           "cp1250": ["cp1250_general_ci",
                      "cp1250_czech_cs",
                      "cp1250_croatian_ci",
                      "cp1250_bin",
                      "cp1250_polish_ci"],
           "gbk": ["gbk_chinese_ci", "gbk_bin"],
           "latin5": ["latin5_turkish_ci", "latin5_bin"],
           "armscii8": ["armscii8_general_ci", "armscii8_bin"],
           "utf8": ["utf8_general_ci",
                    "utf8_bin",
                    "utf8_unicode_ci",
                    "utf8_icelandic_ci",
                    "utf8_latvian_ci",
                    "utf8_romanian_ci",
                    "utf8_slovenian_ci",
                    "utf8_polish_ci",
                    "utf8_estonian_ci",
                    "utf8_spanish_ci",
                    "utf8_swedish_ci",
                    "utf8_turkish_ci",
                    "utf8_czech_ci",
                    "utf8_danish_ci",
                    "utf8_lithuanian_ci",
                    "utf8_slovak_ci",
                    "utf8_spanish2_ci",
                    "utf8_roman_ci",
                    "utf8_persian_ci",
                    "utf8_esperanto_ci",
                    "utf8_hungarian_ci",
                    "utf8_sinhala_ci",
                    "utf8_german2_ci",
                    "utf8_croatian_ci",
                    "utf8_unicode_520_ci",
                    "utf8_vietnamese_ci",
                    "utf8_general_mysql500_ci"
                    ],
           "utf8mb4": ["utf8mb4_0900_ai_ci"],
           "ucs2": ["ucs2_general_ci",
                    "ucs2_bin",
                    "ucs2_unicode_ci",
                    "ucs2_icelandic_ci",
                    "ucs2_latvian_ci",
                    "ucs2_romanian_ci",
                    "ucs2_slovenian_ci",
                    "ucs2_polish_ci",
                    "ucs2_estonian_ci",
                    "ucs2_spanish_ci",
                    "ucs2_swedish_ci",
                    "ucs2_turkish_ci",
                    "ucs2_czech_ci",
                    "ucs2_danish_ci",
                    "ucs2_lithuanian_ci",
                    "ucs2_slovak_ci",
                    "ucs2_spanish2_ci",
                    "ucs2_roman_ci",
                    "ucs2_persian_ci",
                    "ucs2_esperanto_ci",
                    "ucs2_hungarian_ci",
                    "ucs2_sinhala_ci",
                    "ucs2_german2_ci",
                    "ucs2_croatian_ci",
                    "ucs2_unicode_520_ci",
                    "ucs2_vietnamese_ci",
                    "ucs2_general_mysql500_ci"
                    ],
           "cp866": ["cp866_general_ci", "cp866_bin"],
           "keybcs2": ["keybcs2_general_ci", "keybcs2_bin"],
           "macce": ["macce_general_ci", "macce_bin"],
           "macroman": ["macroman_general_ci", "macroman_bin"],
           "cp852": ["cp852_general_ci", "cp852_bin"],
           "latin7": ["latin7_general_ci",
                      "latin7_estonian_cs",
                      "latin7_general_cs",
                      "latin7_bin"],
           "utf8mb4": ["utf8mb4_general_ci",
                       "utf8mb4_bin",
                       "utf8mb4_unicode_ci",
                       "utf8mb4_icelandic_ci",
                       "utf8mb4_latvian_ci",
                       "utf8mb4_romanian_ci",
                       "utf8mb4_slovenian_ci",
                       "utf8mb4_polish_ci",
                       "utf8mb4_estonian_ci",
                       "utf8mb4_spanish_ci",
                       "utf8mb4_swedish_ci",
                       "utf8mb4_turkish_ci",
                       "utf8mb4_czech_ci",
                       "utf8mb4_danish_ci",
                       "utf8mb4_lithuanian_ci",
                       "utf8mb4_slovak_ci",
                       "utf8mb4_spanish2_ci",
                       "utf8mb4_roman_ci",
                       "utf8mb4_persian_ci",
                       "utf8mb4_esperanto_ci",
                       "utf8mb4_hungarian_ci",
                       "utf8mb4_sinhala_ci",
                       "utf8mb4_german2_ci",
                       "utf8mb4_croatian_ci",
                       "utf8mb4_unicode_520_ci",
                       "utf8mb4_vietnamese_ci"],
           "cp1251": ["cp1251_general_ci",
                      "cp1251_bulgarian_ci",
                      "cp1251_ukrainian_ci",
                      "cp1251_bin",
                      "cp1251_general_cs"],
           "utf16": ["utf16_general_ci",
                     "utf16_bin",
                     "utf16_unicode_ci",
                     "utf16_icelandic_ci",
                     "utf16_latvian_ci",
                     "utf16_romanian_ci",
                     "utf16_slovenian_ci",
                     "utf16_polish_ci",
                     "utf16_estonian_ci",
                     "utf16_spanish_ci",
                     "utf16_swedish_ci",
                     "utf16_turkish_ci",
                     "utf16_czech_ci",
                     "utf16_danish_ci",
                     "utf16_lithuanian_ci",
                     "utf16_slovak_ci",
                     "utf16_spanish2_ci",
                     "utf16_roman_ci",
                     "utf16_persian_ci",
                     "utf16_esperanto_ci",
                     "utf16_hungarian_ci",
                     "utf16_sinhala_ci",
                     "utf16_german2_ci",
                     "utf16_croatian_ci",
                     "utf16_unicode_520_ci",
                     "utf16_vietnamese_ci"],
           "utf16le": ["utf16le_general_ci",
                       "utf16le_bin"],
           "cp1256": ["cp1256_general_ci", "cp1256_bin"],
           "cp1257": ["cp1257_general_ci",
                      "cp1257_lithuanian_ci",
                      "cp1257_bin"],
           "utf32": ["utf32_general_ci",
                     "utf32_bin",
                     "utf32_unicode_ci",
                     "utf32_icelandic_ci",
                     "utf32_latvian_ci",
                     "utf32_romanian_ci",
                     "utf32_slovenian_ci",
                     "utf32_polish_ci",
                     "utf32_estonian_ci",
                     "utf32_spanish_ci",
                     "utf32_swedish_ci",
                     "utf32_turkish_ci",
                     "utf32_czech_ci",
                     "utf32_danish_ci",
                     "utf32_lithuanian_ci",
                     "utf32_slovak_ci",
                     "utf32_spanish2_ci",
                     "utf32_roman_ci",
                     "utf32_persian_ci",
                     "utf32_esperanto_ci",
                     "utf32_hungarian_ci",
                     "utf32_sinhala_ci",
                     "utf32_german2_ci",
                     "utf32_croatian_ci",
                     "utf32_unicode_520_ci",
                     "utf32_vietnamese_ci"],
           "binary": ["binary"],
           "geostd8": ["geostd8_general_ci", "geostd8_bin"],
           "cp932": ["cp932_japanese_ci", "cp932_bin"],
           "eucjpms": ["eucjpms_japanese_ci", "eucjpms_bin"],
           "gb18030": ["gb18030_chinese_ci",
                       "gb18030_bin",
                       "gb18030_unicode_520_ci"]}

collation = {"big5_chinese_ci": "big5",
             "big5_bin": "big5",
             "dec8_swedish_ci": "dec8",
             "dec8_bin": "dec8",
             "cp850_general_ci": "cp850",
             "cp850_bin": "cp850",
             "hp8_english_ci": "hp8",
             "hp8_bin": "hp8",
             "koi8r_general_ci": "koi8r",
             "koi8r_bin": "koi8r",
             "latin1_german1_ci": "latin1",
             "latin1_swedish_ci": "latin1",
             "latin1_danish_ci": "latin1",
             "latin1_german2_ci": "latin1",
             "latin1_bin": "latin1",
             "latin1_general_ci": "latin1",
             "latin1_general_cs": "latin1",
             "latin1_spanish_ci": "latin1",
             "latin2_czech_cs": "latin2",
             "latin2_general_ci": "latin2",
             "latin2_hungarian_ci": "latin2",
             "latin2_croatian_ci": "latin2",
             "latin2_bin": "latin2",
             "swe7_swedish_ci": "swe7",
             "swe7_bin": "swe7",
             "ascii_general_ci": "ascii",
             "ascii_bin": "ascii",
             "ujis_japanese_ci": "ujis",
             "ujis_bin": "ujis",
             "sjis_japanese_ci": "sjis",
             "sjis_bin": "sjis",
             "hebrew_general_ci": "hebrew",
             "hebrew_bin": "hebrew",
             "tis620_thai_ci": "tis620",
             "tis620_bin": "tis620",
             "euckr_korean_ci": "euckr",
             "euckr_bin": "euckr",
             "koi8u_general_ci": "koi8u",
             "koi8u_bin": "koi8u",
             "gb2312_chinese_ci": "gb2312",
             "gb2312_bin": "gb2312",
             "greek_general_ci": "greek",
             "greek_bin": "greek",
             "cp1250_general_ci": "cp1250",
             "cp1250_czech_cs": "cp1250",
             "cp1250_croatian_ci": "cp1250",
             "cp1250_bin": "cp1250",
             "cp1250_polish_ci": "cp1250",
             "gbk_chinese_ci": "gbk",
             "gbk_bin": "gbk",
             "latin5_turkish_ci": "latin5",
             "latin5_bin": "latin5",
             "armscii8_general_ci": "armscii8",
             "armscii8_bin": "armscii8",
             "utf8_general_ci": "utf8",
             "utf8_bin": "utf8",
             "utf8_unicode_ci": "utf8",
             "utf8_icelandic_ci": "utf8",
             "utf8_latvian_ci": "utf8",
             "utf8_romanian_ci": "utf8",
             "utf8_slovenian_ci": "utf8",
             "utf8_polish_ci": "utf8",
             "utf8_estonian_ci": "utf8",
             "utf8_spanish_ci": "utf8",
             "utf8_swedish_ci": "utf8",
             "utf8_turkish_ci": "utf8",
             "utf8_czech_ci": "utf8",
             "utf8_danish_ci": "utf8",
             "utf8_lithuanian_ci": "utf8",
             "utf8_slovak_ci": "utf8",
             "utf8_spanish2_ci": "utf8",
             "utf8_roman_ci": "utf8",
             "utf8_persian_ci": "utf8",
             "utf8_esperanto_ci": "utf8",
             "utf8_hungarian_ci": "utf8",
             "utf8_sinhala_ci": "utf8",
             "utf8_german2_ci": "utf8",
             "utf8_croatian_ci": "utf8",
             "utf8_unicode_520_ci": "utf8",
             "utf8_vietnamese_ci": "utf8",
             "utf8_general_mysql500_ci": "utf8",
             "utf8mb4_0900_ai_ci": "utf8mb4",
             "ucs2_general_ci": "ucs2",
             "ucs2_bin": "ucs2",
             "ucs2_unicode_ci": "ucs2",
             "ucs2_icelandic_ci": "ucs2",
             "ucs2_latvian_ci": "ucs2",
             "ucs2_romanian_ci": "ucs2",
             "ucs2_slovenian_ci": "ucs2",
             "ucs2_polish_ci": "ucs2",
             "ucs2_estonian_ci": "ucs2",
             "ucs2_spanish_ci": "ucs2",
             "ucs2_swedish_ci": "ucs2",
             "ucs2_turkish_ci": "ucs2",
             "ucs2_czech_ci": "ucs2",
             "ucs2_danish_ci": "ucs2",
             "ucs2_lithuanian_ci": "ucs2",
             "ucs2_slovak_ci": "ucs2",
             "ucs2_spanish2_ci": "ucs2",
             "ucs2_roman_ci": "ucs2",
             "ucs2_persian_ci": "ucs2",
             "ucs2_esperanto_ci": "ucs2",
             "ucs2_hungarian_ci": "ucs2",
             "ucs2_sinhala_ci": "ucs2",
             "ucs2_german2_ci": "ucs2",
             "ucs2_croatian_ci": "ucs2",
             "ucs2_unicode_520_ci": "ucs2",
             "ucs2_vietnamese_ci": "ucs2",
             "ucs2_general_mysql500_ci": "ucs2",
             "cp866_general_ci": "cp866",
             "cp866_bin": "cp866",
             "keybcs2_general_ci": "keybcs2",
             "keybcs2_bin": "keybcs2",
             "macce_general_ci": "macce",
             "macce_bin": "macce",
             "macroman_general_ci": "macroman",
             "macroman_bin": "macroman",
             "cp852_general_ci": "cp852",
             "cp852_bin": "cp852",
             "latin7_estonian_cs": "latin7",
             "latin7_general_ci": "latin7",
             "latin7_general_cs": "latin7",
             "latin7_bin": "latin7",
             "utf8mb4_general_ci": "utf8mb4",
             "utf8mb4_bin": "utf8mb4",
             "utf8mb4_unicode_ci": "utf8mb4",
             "utf8mb4_icelandic_ci": "utf8mb4",
             "utf8mb4_latvian_ci": "utf8mb4",
             "utf8mb4_romanian_ci": "utf8mb4",
             "utf8mb4_slovenian_ci": "utf8mb4",
             "utf8mb4_polish_ci": "utf8mb4",
             "utf8mb4_estonian_ci": "utf8mb4",
             "utf8mb4_spanish_ci": "utf8mb4",
             "utf8mb4_swedish_ci": "utf8mb4",
             "utf8mb4_turkish_ci": "utf8mb4",
             "utf8mb4_czech_ci": "utf8mb4",
             "utf8mb4_danish_ci": "utf8mb4",
             "utf8mb4_lithuanian_ci": "utf8mb4",
             "utf8mb4_slovak_ci": "utf8mb4",
             "utf8mb4_spanish2_ci": "utf8mb4",
             "utf8mb4_roman_ci": "utf8mb4",
             "utf8mb4_persian_ci": "utf8mb4",
             "utf8mb4_esperanto_ci": "utf8mb4",
             "utf8mb4_hungarian_ci": "utf8mb4",
             "utf8mb4_sinhala_ci": "utf8mb4",
             "utf8mb4_german2_ci": "utf8mb4",
             "utf8mb4_croatian_ci": "utf8mb4",
             "utf8mb4_unicode_520_ci": "utf8mb4",
             "utf8mb4_vietnamese_ci": "utf8mb4",
             "cp1251_bulgarian_ci": "cp1251",
             "cp1251_ukrainian_ci": "cp1251",
             "cp1251_bin": "cp1251",
             "cp1251_general_ci": "cp1251",
             "cp1251_general_cs": "cp1251",
             "utf16_general_ci": "utf16",
             "utf16_bin": "utf16",
             "utf16_unicode_ci": "utf16",
             "utf16_icelandic_ci": "utf16",
             "utf16_latvian_ci": "utf16",
             "utf16_romanian_ci": "utf16",
             "utf16_slovenian_ci": "utf16",
             "utf16_polish_ci": "utf16",
             "utf16_estonian_ci": "utf16",
             "utf16_spanish_ci": "utf16",
             "utf16_swedish_ci": "utf16",
             "utf16_turkish_ci": "utf16",
             "utf16_czech_ci": "utf16",
             "utf16_danish_ci": "utf16",
             "utf16_lithuanian_ci": "utf16",
             "utf16_slovak_ci": "utf16",
             "utf16_spanish2_ci": "utf16",
             "utf16_roman_ci": "utf16",
             "utf16_persian_ci": "utf16",
             "utf16_esperanto_ci": "utf16",
             "utf16_hungarian_ci": "utf16",
             "utf16_sinhala_ci": "utf16",
             "utf16_german2_ci": "utf16",
             "utf16_croatian_ci": "utf16",
             "utf16_unicode_520_ci": "utf16",
             "utf16_vietnamese_ci": "utf16",
             "utf16le_general_ci": "utf16le",
             "utf16le_bin": "utf16le",
             "cp1256_general_ci": "cp1256",
             "cp1256_bin": "cp1256",
             "cp1257_lithuanian_ci": "cp1257",
             "cp1257_bin": "cp1257",
             "cp1257_general_ci": "cp1257",
             "utf32_general_ci": "utf32",
             "utf32_bin": "utf32",
             "utf32_unicode_ci": "utf32",
             "utf32_icelandic_ci": "utf32",
             "utf32_latvian_ci": "utf32",
             "utf32_romanian_ci": "utf32",
             "utf32_slovenian_ci": "utf32",
             "utf32_polish_ci": "utf32",
             "utf32_estonian_ci": "utf32",
             "utf32_spanish_ci": "utf32",
             "utf32_swedish_ci": "utf32",
             "utf32_turkish_ci": "utf32",
             "utf32_czech_ci": "utf32",
             "utf32_danish_ci": "utf32",
             "utf32_lithuanian_ci": "utf32",
             "utf32_slovak_ci": "utf32",
             "utf32_spanish2_ci": "utf32",
             "utf32_roman_ci": "utf32",
             "utf32_persian_ci": "utf32",
             "utf32_esperanto_ci": "utf32",
             "utf32_hungarian_ci": "utf32",
             "utf32_sinhala_ci": "utf32",
             "utf32_german2_ci": "utf32",
             "utf32_croatian_ci": "utf32",
             "utf32_unicode_520_ci": "utf32",
             "utf32_vietnamese_ci": "utf32",
             "binary": "binary",
             "geostd8_general_ci": "geostd8",
             "geostd8_bin": "geostd8",
             "cp932_japanese_ci": "cp932",
             "cp932_bin": "cp932",
             "eucjpms_japanese_ci": "eucjpms",
             "eucjpms_bin": "eucjpms",
             "gb18030_chinese_ci": "gb18030",
             "gb18030_bin": "gb18030",
             "gb18030_unicode_520_ci": "gb18030"}
