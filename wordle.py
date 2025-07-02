import requests
def show(line1,line2,line3,line4,line5,line6):
    print(f"\n|{line1[0]}{line1[1]}{line1[2]}{line1[3]}{line1[4]}{line1[5]}|")
    print(f"|{line2[0]}{line2[1]}{line2[2]}{line2[3]}{line2[4]}{line2[5]}|")
    print(f"|{line3[0]}{line3[1]}{line3[2]}{line3[3]}{line3[4]}{line3[5]}|")
    print(f"|{line4[0]}{line4[1]}{line4[2]}{line4[3]}{line4[4]}{line4[5]}|")
    print(f"|{line5[0]}{line5[1]}{line5[2]}{line5[3]}{line5[4]}{line5[5]}|")
    print(f"|{line6[0]}{line6[1]}{line6[2]}{line6[3]}{line6[4]}{line6[5]}|\n")

def wordle():
    url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/es/es_50k.txt"

    response = requests.get(url)
    response.raise_for_status()

    imprimir = True
    words = []

    line1 = [" _ "]*6
    line2 = [" _ "]*6
    line3 = [" _ "]*6
    line4 = [" _ "]*6
    line5 = [" _ "]*6
    line6 = [" _ "]*6
    pos = 0

    for word in response.text.split():
        if imprimir:
            words.append(word)
            imprimir = False
        else:
            imprimir = True
    
    show(line1,line2,line3,line4,line5,line6)

    word = input(": ")

    if word in words:
        for l in word:
            if pos == 0:
                for pos in range (5):
                    line1[pos] = l
wordle()
