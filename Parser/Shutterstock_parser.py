import requests
from bs4 import BeautifulSoup
import wget
import os


def get_images(number_of_images, section='', folder_to='downloaded'):
    url = 'https://www.shutterstock.com/search'
    if section:
        url += '/' + section
    if folder_to[-1] != '/':
        folder_to += '/'
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    tag = soup.findAll("img", {"class": "z_g_h"})
    pics = []
    if not os.path.exists(folder_to):
        os.makedirs(folder_to)
    for i in range(number_of_images):
        if i >= len(tag):
            print("Exceeded max number")
            return
        wget.download(tag[i]['src'], out=folder_to + str(i) + '.jpg')
        pics.append((tag[i]['src'], tag[i]['alt']))
    return pics


if __name__ == '__main__':
    pics = get_images(10)
    print(pics)