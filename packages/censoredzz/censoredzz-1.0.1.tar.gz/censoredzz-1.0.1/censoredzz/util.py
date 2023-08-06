# remove repeating letters
import re
def remove_recurring_letters(sentence):
    words = sentence.split()
    modified_sentence = []
    for word in words:
        modified_word = re.sub(r"(.)\1+", r"\1", word)
        modified_sentence.append(modified_word)
    return ' '.join(modified_sentence)

