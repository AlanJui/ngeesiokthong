# Neovim 操作指引

## 漢字拼音

基本上，使用「台羅拼音」做為字典的「拼音碼」。但需略做調整如
下：

- tsh: chh
- ts: ch
- ∅: q （無「聲母」的拼音碼，需以 q 字母前導）

## 字典

### 改聲母 tsh

```sh
:%s/tsh/ch/g
```

### 改聲母 ts

```sh
:%s/ts/c/g
```

### 改無聲母拼音

```
要	qai7		需要
會使得	qe7 sai2 tit4		可以
這樣	cit4 qiunn7		這樣
```

若拼音有 2 個以上，自第 2 個拼音開始，拼音開始前，皆有一個空
白字元，可用以下方式進行置換：

```sh
:%s/\v ([aeiou])/ q\1/g
```

但第一個拼音，其前有個 tab 字元，則下指令置換的方法，變更如
下：

```sh
:%s/\v\t([aeiou])/\tq\1/g
```

## 變更格式

### 將聲母置前

替換：

```sh
- xform/;l/柳]/
```

變更成：

```sh
- xform/;l/\[柳;/
```

正規式：

```sh
:%s/\v([\u4e00-\u9fff])\]/\[\1;/g
```

### 將韻母置後

替換：

```sh
- xform/;ai(\d)/\[皆;$1/
```

變更成：

```sh
- xform/;ai(\d)/皆;$1/
```

正規式：

```sh
:%s/\v\[([\u4e00-\u9fff])/\1;/g
```

### 韻母解析正規式一

([aeiou])(m?n\*h?g?p?t?k?)([1234578])

## 解析

### 韻母解析正規式一

([aeiou])(m?n\*h?g?p?t?k?)([1234578])

- m? : 這表示前面的字母 "m" 可以出現 0 次或 1 次，因此它是可
  選的。
- n\* : 這表示前面的字母 "n" 可以出現 0 次或多次，因此它可以
  出現多次或完全不出現。
- h? : 這表示前面的字母 "h" 可以出現 0 次或 1 次，因此它是可
  選的。
- g? : 這表示前面的字母 "g" 可以出現 0 次或 1 次，因此它是可
  選的。
- p? : 這表示前面的字母 "p" 可以出現 0 次或 1 次，因此它是可
  選的。
- t? : 這表示前面的字母 "t" 可以出現 0 次或 1 次，因此它是可
  選的。
- k? : 這表示前面的字母 "k" 可以出現 0 次或 1 次，因此它是可
  選的。

以下符號的意義：

- ? : 前面的元素可以出現 0 次或 1 次。
- - : 前面的元素可以出現 0 次或多次。

這個正規表達式由三個捕獲群組組成，分別對應元音、一系列可能的
字母，以及數字。以下是符合這個正規表達式的舉例：

- am3
- ehn1
- ongh8
- ig7
- uhk6
- ap2
- uit4
- anh5
- ek7
- ohp8

### 韻母解析正規式二

([aeo])([iueo])([1234578])

- ai1
- eu3
- oa5
- oa6
- ei7
- ao2
- ae4
- io1
- ei2
- oa4
- ua6
- ae7
- oi3
- ae5
- io4
- oi7
- ee6
- ai4
- ua2
- uo8

- xform/([aeiou])(m?n\*h?g?p?t?k?)([1234578])/$1$3$2/
- xform/([aeo])([iueo])([1234578])/$1$3$2/

  - "xform a1 a"
  - "xform e1 e"
  - "xform i1 i"
  - "xform u1 u"
  - "xform o1 o"
  - "xform a2 á"
  - "xform e2 é"
  - "xform i2 í"
  - "xform u2 ú"
  - "xform o2 ó"
  - "xform a3 à"
  - "xform e3 è"
  - "xform i3 ì"
  - "xform u3 ù"
  - "xform o3 ò"
  - "xform a4 a"
  - "xform e4 e"
  - "xform i4 i"
  - "xform u4 u"
  - "xform o4 o"
  - "xform a5 â"
  - "xform e5 ê"
  - "xform i5 î"
  - "xform u5 û"
  - "xform o5 ô"
  - "xform a7 ā"
  - "xform e7 ē"
  - "xform i7 ī"
  - "xform u7 ū"
  - "xform o7 ō"
  - "xform a8 a̍"
  - "xform e8 e̍"
  - "xform i8 i̍"
  - "xform u8 u̍"
  - "xform o8 o̍"

### 鼻化符號顯示成上標

- xform/nn(h?)(\d|\>)/ⁿ$1$2/

## 其它

### 輸入「空集合」符號

在 Neovim 可使用 Unicode 來輸入特殊符號。空集合符號的
Unicode 碼是 U+2205。

操作方法：

1. 進入「插入」模式。

2. 按 Ctrl-V 鍵，接著輸入 u 字母，然後輸入四個十六進位數字
   2205，這樣就會插入空集合符號。

liat8 是台羅拼音， l 是聲母 iat 是韻母 8 是調號

聲母的羅馬拼音字母有以下這些： l p ph k kh t th ts tsh j s q
b g h

韻母的羅馬拼音字母有以下這些： a ann ah annh ai ainn ak am
an ang ap ap au auh e enn eh ennh ik ing i inn ia iann iah
iannh iak iam ian iang iap iat iau iaunn iauh ih im in io
ioh iok iong ip it iu iunn iunnh m mh ng ngh o onn oo ua
uann uah uai uainn uan uang uat ue ueh oh onnh ok om ong u
uh ui un ut

調號的羅馬拼音字母有以下這些： 1 2 3 4 5 6 7 8

則 preedit_format 的 xform 該怎麼寫，才能解析到(韻母)(調號)(
聲母)？
