#!/usr/bin/env python

from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytube import YouTube
import time, os


def download(url, path):
    options = Options()
    options.headless = True

    browser = webdriver.Chrome(options=options)

    browser.get(url)
    time.sleep(10)
    page = browser.page_source
    browser.quit()

    soup = bs4(page)

    titles = soup.find_all('span', attrs={'id': 'video-title'})
    content = soup.find_all('a', attrs={'class': 'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})

    links = []

    for i in range(len(content)):
        print(titles[i]['title'])

        partial_link = content[i]['href']
        partial_link = partial_link.split('&l')[0]

        link = f'https://www.youtube.com{partial_link}'
        print(link)

        links.append(link)
        print('===============================================================')

    for yt_link in links:
        yt = YouTube(yt_link)
        try:
            yt.streams.filter(subtype='mp4').first().download(path)
        except FileNotFoundError:
            os.makedirs(path)
            yt.streams.filter(subtype='mp4').first().download(path)

    print('\nDownloads successful, enjoy!')


if __name__ == '__main__':
    url = input('\nEnter url of YouTube playlist to download:\n')
    path = input('\nEnter path to download playlist to: \n/')

    download(url, path)
