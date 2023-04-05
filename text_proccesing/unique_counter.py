import re

story = 'DOWN THE RABBIT HOLE. Alice had sat on the bank by her sis-ter till she was tired. ' \
        'Once or twice she had looked at the book her sis-ter held in her hand, ' \
        'but there were no pict-ures in it, "and what is the use of a book," thought Alice, ' \
        '"with-out pict-ures?" She asked her-self as well as she could, ' \
        'for the hot day made her feel quite dull, if it would be worth while ' \
        'to get up and pick some dai-sies to make a chain. ' \
        'Just then a white rab-bit with pink eyes ran close by her. '


def count_word(any_story):
    dict_count_word = {}
    ch_any_story = re.sub(r'[^a-zA-Z ]', '', any_story).lower().split()
    s_any_story = set(ch_any_story)
    for i in s_any_story:
        dict_count_word[i] = ch_any_story.count(i)
    print(dict_count_word)