# 中州韻（RIME）輸入法

## 解析字典

字典檔案 taigi_yu.han.dict.yaml ：

```sh
# Rime dictionary
# encoding: utf-8

---
name: taigi_yu.han
version: "0.2"
sort: by_weight
use_preset_vocabulary: false
...
一	ciD8
一	iD4
一刀兩斷	iD4 tø1 dioG2 tuaD7
一下	ciD8 e7
一月日	ciD8 gue8 ziD8
一日到暗	ciD8 ziD8 kU3 aB3
一世人	ciD8 si3 daG5
一半	ciD8 pNua3
一半个仔	ciD8 pNua3 e5 a2
一半日仔	ciD8 pNua3 ziD8 a2
一四界	ciD8 si3 ke3
一旦	iD4 taD3
一生	iD4 siøG1
一目𥍉仔	ciD8 baG8 dNi4 a2
一甲子	ciD8 ka4 ci2
一百空一	ciD8 pa4 KoG3 iD4
一來	iD4 dI5
.......
```

用於解析「字典」的指令集：

```sh
speller:
  alphabet: '1qaz2wsxedcrfvtgbyhnujm8ik,9ol.0p;/- 43657'
  initials: '1qaz2wsxedcrfvtgbyhnujm8ik,9ol.0p;/-7'
  finals: ' 43567'
  delimiter: "'"
  use_space: true
  algebra:
    # 變調
    - derive/1/7/  # 第一調 → 第七調
    - derive/2/1/  # 第二調 → 第一調
    - derive/3/2/  # 第三調 → 第二調
    - derive/7/3/  # 第七調 → 第三調
    - derive/5/7/  # 第五調 → 第七調
    - derive/5/3/  # 第五調 → 第三調
    - derive/(?<![BDG])4/2/  # -ㆷ 第四調 → 第二調
    - derive/(?<![BDG])8/3/  # -ㆷ 第八調 → 第三調
    - xform/[48]/0/  # 入聲調（第四調、第八調）合併
    # 音變
    - derive/z/d/         # ㆡ、ㆢ → ㄌ
    - derive/z(N?i)/g$1/  # ㆢ → ㆣ
    - derive/iaD/ieD/  # ㄧㄢ、ㄧㄚㆵ → ㄧㄢ、ㄧㆤㆵ
    - derive/ieD/eD/   # ㄧㄢ、ㄧㆤㆵ → ㆤㄣ、ㆤㆵ
    # 方言差
    - derive/Ne/Ni/    # ㆥ → ㆪ
    - derive/Niu/Nio/  # ㄧㆫ → ㄧㆧ
    # 方音符號會分 ㆢㄐㄑㄒ 和 ㆡㄗㄘㄙ
    #- xform/z(N?i)/Z$1/  # 毋過咱共 ㆢ 和 ㆡ 合併矣
    - xform/c(N?i)/j$1/  # ㄐㄧ
    - xform/C(N?i)/J$1/  # ㄑㄧ
    - xform/s(N?i)/S$1/  # ㄒㄧ
    # 方音符號會分 ㄇㄋㄫ 和 ㆠㄌㆣ
    - derive/bN/m/  # ㄇ
    - derive/dN/n/  # ㄋ
    - derive/gN/q/  # ㄫ
    - derive/bG/mG/  # ㄇㆭ
    - derive/dG/nG/  # ㄋㆭ
    # 鼻音
    - xform/N([iu]?[iuaoeIU])/$1N/  # 鼻音拍佇後壁
    - derive/([iuaoeIU])N/$1$1/     # 拍兩擺韻母來拍鼻音
    # 注音
    - derive/øG/G/  # 用 ㄧㆭ 來拍 ㄧㄥ（併入）
    - derive/(?<!i)oG/uG/  # 用 ㄨㆭ（注音的 ㄨㄥ）來拍 ㆲ
    - derive/ioG/BG/       # 用 ㆬㆭ（注音的 ㄩㄥ）來拍 ㄧㆲ
    # 入聲調
    - derive/([iao])B0/$1p0/   # 用 ㄚㄅ． 來拍 ㄚㆴ
    - derive/([iuae])D0/$1t0/  # 用 ㄚㄉ． 來拍 ㄚㆵ
    - derive/([iaoø])G0/$1k0/  # 用 ㄚㄍ． 來拍 ㄚㆻ
    # 方音韻母
    - derive/oB/aB/  # ㆦㆬ、ㆰ（併入）
    - derive/aB/M/   # ㄚㆬ、ㆰ
    - xform/aD/L/    # ㄢ
    - xform/aG/Q/    # ㄤ
    - derive/oG/Y/   # ㆦㆭ、ㆲ
    # 簡拼
    - abbrev/[iu]?[iuaoeIU]N/N/  # 用 ｎ 代表所有的鼻音母音
    - abbrev/[iuaoøeIUMLQYBDG]+0/0/  # 用 ． 代表所有的入聲韻母
    - abbrev/^([pPbmtTdnkKgqcCzsjJSh]).+$/$1/  # 會當干焦拍聲母
    - abbrev/^(\D+)([123579])$/$1/  # 除了第四調、第八調，調號會當免拍
    - abbrev/^([pPbmtTdnkKgqcCzsjJSh]).+(\d)$/$1$2/  # 會當干焦拍子音+調號
    - xlit|pPmbtTndkKhjJSgqzcCsiuBaoøMIeUYLDQGN123570|1qaz2wsxedcrfvtgbyhnujm8ik,9ol.0p;/- 43657|
```

## 解析及處理鍵盤輸入

```sh
translator:
  dictionary: taigi_yu
  prism: taigi_tps
  spelling_hints: 3
  comment_format:
    - xform/^/\t→ /
    - xform/'/ /
    - xlit|pPbtTdkKgcCzshiuaoøeIUBDGN|ㄅㄆㆠㄉㄊㄌㄍㄎㆣㄗㄘㆡㄙㄏㄧㄨㄚㆦㄜㆤㄞㄠㆬㄣㆭｎ|
    # 方音符號會分 ㆢㄐㄑㄒ 和 ㆡㄗㄘㄙ
    - xform/ㄗ((ｎ)?ㄧ)/ㄐ$1/
    - xform/ㄘ((ｎ)?ㄧ)/ㄑ$1/
    - xform/ㆡ((ｎ)?ㄧ)/ㆢ$1/
    - xform/ㄙ((ｎ)?ㄧ)/ㄒ$1/
    # 方音符號會分 ㄇㄋㄫ 和 ㆠㄌㆣ
    - xform/ㆠｎ/ㄇ/
    - xform/ㄌｎ/ㄋ/
    - xform/ㆣｎ/ㄫ/
    - xform/ㆠㆭ/ㄇㆭ/
    - xform/ㄌㆭ/ㄋㆭ/
    # 入聲調
    - xform/(?<=ㄧ|ㄚ|ㆦ)ㆬ([48])/ㆴ$1/
    - xform/(?<=ㄧ|ㄨ|ㄚ)ㄣ([48])/ㆵ$1/
    - xform/(?<=ㄚ|ㆦ|ㄜ)ㆭ([48])/ㆻ$1/
    - xform/(?<!ㆴ|ㆵ|ㆻ)([48])/ㆷ$1/
    # 鼻音
    - xform/ｎ((ㄧ|ㄨ)?(ㄧ|ㄨ|ㄚ|ㆦ|ㆤ|ㄞ|ㄠ))/$1ｎ/
    - xform/ㄧｎ/ㆪ/
    - xform/ㄨｎ/ㆫ/
    - xform/ㄚｎ/ㆩ/
    - xform/ㆦｎ/ㆧ/
    - xform/ㆤｎ/ㆥ/
    - xform/ㄞｎ/ㆮ/
    - xform/ㄠｎ/ㆯ/
    # 韻母
    - xform/ㄚㆬ/ㆰ/
    - xform/ㆦㆬ/ㆱ/
    - xform/ㄚㄣ/ㄢ/
    - xform/ㄚㆭ/ㄤ/
    - xform/ㆦㆭ/ㆲ/
    - xform/ㄜㆭ/ㄥ/
    # 聲調
    - xlit|12357|ˉˋ˪ˊ˫|
    - xform/4//
    - xform/8/˙/
  preedit_format:
    - xform/ /ˉ/
    - xform/'/ /
    - xlit|1qaz2wsxedcrfvtgbyhnujm8ik,9ol.0p;/-43657|ㄅㄆㄇㆠㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㆣㄫㆡㄗㄘㄙㄧㄨㆬㄚㆦㄜㆰㄞㆤㄠㆲㄢㄣㄤㆭｎˋ˪ˊ˫．|
    # 拆韻母
    - xform/ㆰ/ㄚㆬ/
    - xform/ㄢ/ㄚㄣ/
    - xform/ㄤ/ㄚㆭ/
    - xform/ㆲ/ㆦㆭ/
    - xform/ㄨㆭ/ㆦㆭ/
    - xform/ㆬㆭ/ㄧㆦㆭ/
    - xform/ㄧㆭ/ㄧㄜㆭ/
    # 咱共 ㆢ 和 ㆡ 合併
    - xform/ㆡㄧ/ㆢㄧ/
    # 鼻音
    - xform/ㄧ(ㄧ|ｎ)/ㆪ/
    - xform/ㄨ(ㄨ|ｎ)/ㆫ/
    - xform/ㄚ(ㄚ|ｎ)/ㆩ/
    - xform/ㆦ(ㆦ|ｎ)/ㆧ/
    - xform/ㆤ(ㆤ|ｎ)/ㆥ/
    - xform/ㄞ(ㄞ|ｎ)/ㆮ/
    - xform/ㄠ(ㄠ|ｎ)/ㆯ/
    # 入聲調
    - xform/(ㄧ|ㄚ|ㆦ)(ㄅ|ㆬ)．/$1ㆴ/
    - xform/(ㄧ|ㄨ|ㄚ|ㆤ)(ㄉ|ㄣ)．/$1ㆵ/
    - xform/(ㄚ|ㆦ|ㄜ)(ㄍ|ㆭ)．/$1ㆻ/
    - xform/(ㄧ|ㄨ|ㄚ|ㆦ|ㄜ|ㆤ|ㄞ|ㄠ|ㆬ|ㆭ)．/$1ㆷ/
    # 合韻母
    - xform/ㄚㆬ/ㆰ/
    - xform/ㆦㆬ/ㆱ/
    - xform/ㄚㄣ/ㄢ/
    - xform/ㄚㆭ/ㄤ/
    - xform/ㆦㆭ/ㆲ/
    - xform/ㄜㆭ/ㄥ/
```

## 韻、聲、調

### 聲母

- l
- p
- ph
- k
- kh
- t
- th
- ts
- tsh
- j
- s
- q
- b
- g
- h
- ng

### 韻母

- a
- ann
- ah
- annh
- ai
- ainn
- ak
- am
- an
- ang
- ap
- ap
- au
- auh
- e
- enn
- eh
- ennh
- ik
- ing
- i
- inn
- ia
- iann
- iah
- iannh
- iak
- iam
- ian
- iang
- iap
- iat
- iau
- iaunn
- iauh
- ih
- im
- in
- io
- ioh
- iok
- iong
- ip
- it
- iu
- iunn
- iunnh
- m
- mh
- ng
- ngh
- o
- onn
- oo
- ua
- uann
- uah
- uai
- uainn
- uan
- uang
- uat
- ue
- ueh
- oh
- onnh
- ok
- om
- ong
- u
- uh
- ui
- un
- ut

### 調號

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
