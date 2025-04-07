import requests
from bs4 import BeautifulSoup
import re
from time import sleep


list_card_url = []
headers ={
    'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; '
    'en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 '
    '(.NET CLR 3.5.30729)'
}

def get_url():
    for page in range(2,3):  # кол-во страниц (указать)

        url = f"https://spark-interfax.ru/map/nizhegorodskaya-oblast/{page}" #generator url page
        response = requests.get(url)
        soup=BeautifulSoup(response.text,'lxml') #html parser
        data = soup.find_all('li', class_="raiting-list__item") #поиск всех названий

        for i in data: #записываем в лист карточки
            info_company='https://spark-interfax.ru'+i.find('a').get('href')
            yield info_company

def array():

    for card_url in get_url():

        response = requests.get(card_url)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find('div', class_="padding-top-10") #url main card
        name = data.find('div',class_="company-characteristics__value", itemprop="legalName").text #parse name
        inn = data.find('span', class_="copy-to-clipboard js-copy-to-clipboard", itemprop="taxID").text #parse inn
        main_specialization = [el.get_text() for el in (data.find_all('div', class_="okved-list__name"))] #генератор parse специальность ОКВЭД
        # for el in main_specialization :
        #     print(el.get_text())
        additional_specialization = [el.get_text() for el in (data.find_all('div', class_="okved-list__item"))] #генератор parse доп.специальность ОКВЭД
        #print(additional_specialization)
        description = data.find('div',class_="company-description__text", itemprop="description").text #parse описание
        # Преобразуем списки в строки с разделителем (например, запятой)
        main_specialization_str = ', '.join(main_specialization)
        additional_specialization_str = ', '.join(additional_specialization)
        yield name, inn, main_specialization_str, additional_specialization_str, description
        #print(name,inn,main_specialization,additional_specialization,description, sep='\n')

    #     if reguest.status_code == '200':

