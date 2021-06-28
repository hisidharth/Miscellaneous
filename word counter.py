example_paragraph = "ha ha ha ha ha L9 L9 L9 L9 XD XD XD XD XD"
example_paragraph_lower = example_paragraph.lower()

example_word_list = example_paragraph_lower.split(" ")

def counter(s):
    a=dict()
    for c in s:
        if c not in a:
            a[c]=1
        else:
            a[c]+=1
    return a


def rev (dic):
    bar={}
    for word in dic:
        if dic[word] not in bar:
            bar[dic[word]]=[word]
        else:
            bar[dic[word]].append(word)
    return bar
def sort(dic):
    sorted_dic = dict(sorted(dic.items()))
    return sorted_dic
print(example_paragraph_lower)
frequency_dictionary = counter(example_word_list)
print(frequency_dictionary)
frequency_dictionary=rev(frequency_dictionary)
print(frequency_dictionary)
frequency_dictionary= sort(frequency_dictionary)
print(frequency_dictionary)
answer=input("What word would you like to know the frequency of?")
z=counter(example_word_list)
if answer in z:
    print(z[answer])


