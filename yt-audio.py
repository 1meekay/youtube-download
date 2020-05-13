#!/usr/bin/env python

from pytube import YouTube
import time, os


def download(link, path):
    yt = YouTube(url)

    try:
        yt.streams.filter(only_audio=True, mime_type='audio/mp4').first().download(path)
    except FileNotFoundError:
        os.makedirs(path)
        yt.streams.filter(only_audio=True, mime_type='audio/mp4').first().download(path)

    print('\nDownload successful, enjoy!')


if __name__ == '__main__':
    url = input('\nEnter url of YouTube video to download:\n')
    path = input('\nEnter path to download playlist to: \n/')

    download(url, path)
