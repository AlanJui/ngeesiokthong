# 定義聲調轉換字典
tone_mapping = {
    'a': {'a': '1', 'á': '2', 'à': '3', 'â': '5', 'ă': '6', 'ā': '7', '̍': '8'},
    'e': {'e': '1', 'é': '2', 'è': '3', 'ê': '5', 'ě': '6', 'ē': '7', '̍': '8'},
    'i': {'i': '1', 'í': '2', 'ì': '3', 'î': '5', 'ǐ': '6', 'ī': '7', '̍': '8'},
    'oo': {'oo': '1', 'óo': '2', 'òo': '3', 'ôo': '5', 'ǒo': '6', 'ōo': '7', '̍o': '8'},
    'o': {'o': '1', 'ó': '2', 'ò': '3', 'ô': '5', 'ǒ': '6', 'ō': '7', '̍': '8'},
    'u': {'u': '1', 'ú': '2', 'ù': '3', 'û': '5', 'ǔ': '6', 'ū': '7', '̍': '8'},
    'm': {'m': '1', 'ḿ': '2', 'm̀': '3', 'm̂': '5', 'm̌': '6', 'm̄': '7', 'm̍': '8'},
    'ng': {'ng': '1', 'ńg': '2', 'ǹ': '3', 'n̂gh': '5', 'ňg': '6', 'n̄g': '7', 'n̍g': '8'},
}

def convert_syllable(syllable):
    # 定義可以為母音的羅馬字母
    vowel_letters = ['a', 'e', 'i', 'oo', 'o', 'u', 'm', 'ng']

    # 對每種可能的母音情況進行檢查
    for v in vowel_letters:
        for tone, tone_set in tone_mapping[v].items():
            if tone in syllable:
                new_syllable = syllable.replace(tone, v) + tone_set
                return new_syllable

    return syllable  # 如果找不到母音，保持原樣


def convert_pinyin(pinyin):
    new_pinyin = []
    syllables = pinyin.split('-')
    for syllable in syllables:
        if syllable == '':
            new_pinyin.append('')
        else:
            tone = convert_syllable(syllable)
            new_pinyin.append(tone)
    return ' '.join(new_pinyin)


# 讀取詞庫檔案
with open('su_khoo.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 轉換並輸出結果
with open('su_khoo_new.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        chinese, pinyin = line.strip().split('\t')
        new_pinyin = convert_pinyin(pinyin)
        new_line = f'{chinese}\t{new_pinyin}'
        file.write(new_line + '\n')

print("轉換完成")
