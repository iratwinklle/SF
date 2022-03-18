def changetext(text):
    '''убираем все знаки из текста'''
    for i in '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~':
        text = text.replace(i, '')
        return text.split()

def words_with_3_letts(text):
    '''список всех слов с 3 буквами'''
    words_3 = []
    for word in text:
        if len(word) >= 3:
            words_3.append(word)
    return words_3

def most_common_words(text):
    '''самое часто встречающееся'''
    most_common_word = set()
    qty_words = 0
    for item in text:
        if text.count(item) > qty_words:
            most_common_word = set()
            most_common_word.add(item)
            qty_words = text.count(item)
        elif text.count(item) == qty_words:
            most_common_word.add(item)
    return most_common_word

def all_english_words(text):
    ''' сравнение букв в словах списка с буквами в списке русских букв если НЕ совпадает - добавляет слово
    в словарь английских слов'''
    all_english_words = []
    rus_alphabet = 'абвгдеёжзийклмнопрстуфхчщъыьэюяАБВГЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯ'
    for i in rus_alphabet:
        for item in text:
            for w in item:
                if i != w:
                    all_english_words.append(item)
    return all_english_words

def most_lenght(text):
    '''самоее длинное слово'''
    most_lenght = 0
    most_large_word = set()
    for word in text:
        if len(word) > most_lenght:
            most_large_word = set()
            most_large_word.add(word)
            most_lenght = len(word)
        elif len(word) == most_lenght:
            most_large_word.add(word)
    return most_large_word

namefile = input("Введите имя файла, который надо открыть:")
import string
# namefile = 'harry.txt'
with open(namefile, encoding='utf8') as f:
    text = f.read()  #читаем файл в строку

cleartext = changetext(text)  #список без знаков
all_3_letters = words_with_3_letts(cleartext)
most_common = most_common_words(all_3_letters)
all_english = all_english_words(cleartext)
lenghter = most_lenght(all_english)

print('Список самых частых слов в файле {} длинной более трёх символов: {}'.format(namefile, most_common))
print('В файле {} самое длинное слово на английском:{}'.format(namefile, lenghter))