from words import *
from definition import *
x_words=words()
string_word=x_words.get_words()
word_list=x_words.clean_word_list(string_word)
word_def=definition()
for i in word_list:
    word_def.get_definition(i)



