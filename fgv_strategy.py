import requests
import re
from bs4 import BeautifulSoup

import pages_set

def last_message(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features="lxml")

    m_dates = []
    messages = []

    for c in soup.select('td:nth-child(2)'):
        messages.append(c.string)

    for c in soup.select('td:nth-child(1)'):
        m_dates.append(c.string)
    
    return f'última mensagem - data:{m_dates[1]}\nmensagem: {messages[0]}'


def print_messages():

    pages = pages_set.get_pages('fgv')

    for p in pages:

        m = last_message(p)

        print(f'de {p.split("/")[-1]}:\n{m}\n')

if __name__ == '__main__':

    url = 'https://conhecimento.fgv.br/concursos/concursocgu21'

    r = last_message(url)

    print(r) 

