from bs4 import BeautifulSoup
import requests
import random

symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
           '8', '9', '0']

def GetCitate(theme):
    try:
        response = requests.get('https://citaty.info/search/site/'+theme).text
        page = BeautifulSoup(response, "lxml")
        block = page.find(class_="field-item even last").text
        print(block)
        return block
    except Exception as e:
        return "Цитата не найдена"

def GetLink():
    word = ""
    for i in range(6):
        word+=random.choice(symbols)
    return word
