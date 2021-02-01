import random

ORDER = 5
CHAR_OF_LYRICS = 1000

def setup(txt):
    count = 0
    ng = {}
    for index, character in enumerate(txt):
        gram = txt[index:index+ORDER]
        if gram not in ng:
            ng[gram] = []
        ng[gram].append(txt[index+ORDER:index+ORDER+1])
        
        if index == len(txt) - ORDER:
            break

    return ng


def markov(txt, ng):
    currentGram = txt[0:ORDER]
    result = currentGram

    for idx in range(CHAR_OF_LYRICS):
        possibilities = ng.get(currentGram)
        nextChar = random.choice(possibilities)
        result += nextChar
        currentGram = result[len(result)-ORDER:len(result)]

    return result


# reading .txt file to get lyrics into a string
file = open("lyrics.txt", "r")
lines = file.readlines()
lyrics = "".join(lines)
while lyrics.find("\n") != -1:
    lyrics = lyrics.replace("\n", " ")
file.close()

ngrams = setup(lyrics)
result = markov(lyrics, ngrams)
print(result)