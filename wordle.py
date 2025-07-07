import requests

def show(line):
    show = ""
    
    for d in range (6):
        for u in range (5):
            show += line[d][u]
            if u == 4:
                print(show)
                show = ""

def system(word,wordbase,pos,line):
    array = []
    arraybase = []
    countbase = []

    for l1 in word:
        array.append(f" {l1} ")
    for l2 in wordbase:
        arraybase.append(f" {l2} ")

    for l3 in wordbase:
        countbase.append(arraybase.count(f" {l3} "))
    for l4 in (5):
        countbase[l4]
    print(arraybase,"\n",countbase)
    
    for lettpos in range (5):
        if array[lettpos] == arraybase[lettpos]:
            array[lettpos] = f"\033[92m{array[lettpos]}\033[0m"
    
    for i in range (5):
        line[pos][i] = array[i]
    show(line)
    pos += 1

def wordle():
    url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/es/es_50k.txt"

    response = requests.get(url)
    response.raise_for_status()

    words = []

    line = [
        [" _ "," _ "," _ "," _ "," _ "],
        [" _ "," _ "," _ "," _ "," _ "],
        [" _ "," _ "," _ "," _ "," _ "],
        [" _ "," _ "," _ "," _ "," _ "],
        [" _ "," _ "," _ "," _ "," _ "],
        [" _ "," _ "," _ "," _ "," _ "]
    ]
    pos = 0
    imprimir = True

    for word in response.text.split():
        if imprimir:
            words.append(word)
            imprimir = False
        else:
            imprimir = True

    wordbase = input("Palabra base: ")

    show(line)

    while True:
        word = input("\n:")

        if word in words or word == wordbase:
            system(word,wordbase,pos,line)
            if word == wordbase:
                print("\n \033[93mGanaste pibe\033[0m")
                break
        else:
            print("no se encuentra la palabra")
wordle()
