from polyglot.text import Word, Text

words = "həmişə bütün hüquq normalarda hər üç element olmur".split(" ")

for w in words:
    w = Word(w, language="az")
    print("{:<20}{}".format(w, w.morphemes))

"""

həmişə              ['həmişə']
bütün               ['bütün']
hüquq               ['hüquq']
normalarda          ['norma', 'larda']
hər                 ['hər']
üç                  ['üç']
element             ['element']
olmur               ['olmur']

"""


text = "həmişəbütünhüquqnormalardahərüçelementolmur"

splitted_text = Text(text)
splitted_text.language = "az"
print(splitted_text.morphemes)

"""

['həmişə', 'bütün', 'hüquq', 'norma', 'larda', 'hər', 'üç', 'element', 'olmur']

"""