def single_root_words(root_word, *other_words) :
    same_words = []
    for i in other_words :
        i_ = i.lower()
        if i_ in root_word.casefold() or root_word.casefold() in i_ :
            same_words.append(i)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))