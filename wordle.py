import requests

def wordle():
    url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/es/es_50k.txt"

    response = requests.get(url)
    response.raise_for_status()

    imprimir = True
    words = []

    line1 = [" "]*5
    line2 = [" "]*5
    line3 = [" "]*5
    line4 = [" "]*5
    line5 = [" "]*5
    line6 = [" "]*5

    for word in response.text.split():
        if imprimir:
            words.append(word)
            imprimir = False
        else:
            imprimir = True
    
    word = input("Palabra: ")
    if word in words:
        print("si esta la palabra")
    
    print(f"")
wordle()