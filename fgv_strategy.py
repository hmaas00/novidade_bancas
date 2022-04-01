import requests
import re
from bs4 import BeautifulSoup



def ultima_mensagem(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features="lxml")

    datas = []
    mensagens = []

    for c in soup.select('td:nth-child(2)'):
        mensagens.append(c.string)

    for c in soup.select('td:nth-child(1)'):
        datas.append(c.string)
    
    return f'última mensagem - data:{datas[1]}\nmensagem: {mensagens[0]}'


if __name__ == '__main__':

    url = 'https://conhecimento.fgv.br/concursos/concursocgu21'

    r = ultima_mensagem(url)

    print(r) 

