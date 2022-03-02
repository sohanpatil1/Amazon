import requests
from bs4 import BeautifulSoup
import csv
import os

def writetocsv(text):
    with open("/Users/sohanpatil/Documents/VSWorkspace/Python_Parser_FAQ/FAQ_Testing.csv", 'a') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        for i in text:
            writer.writerow([i])
        writer.writerow("")

def onelifaq():
    li  = soup.find('ul', class_="list--faq")
    text = []
    count=0

    for i in li:
        i = i.text
        if(len(i) == 1):
            continue
        print(i)
        text.append(i)
        print("\n------")
        count = count+1
    writetocsv(text)

def multilifaq():
    count=0
    text = []
    all  = soup.findAll('ul', class_="list--faq")
    for li in all:
        for i in li:
            i = i.text
            if(len(i) == 1):
                continue
            print(i)
            text.append(i)
            print("\n------")
            count = count+1
    writetocsv(text)

def multiliacc():
    count=0
    text = []
    all  = soup.findAll('ul', class_="list--accordion")
    for li in all:
        for i in li:
            i = i.text
            if(len(i) == 1):
                continue
            print(i)
            text.append(i)
            print("\n------")
            count = count+1
    writetocsv(text)


if __name__ == "__main__":
    page = requests.get("https://orientation.ucdavis.edu/faq")
    soup = BeautifulSoup(page.content, 'lxml')
    #onelifaq()
    #multilifaq()
    multiliacc()
    
