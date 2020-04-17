#!/usr/local/bin/python3

import argparse
from os import mkdir, path
from functools import reduce
from requests import get
from bs4 import BeautifulSoup as bs


base_url = 'https://baseurl.com'


def main(id):
    link = '{}/g/{}'.format(base_url, id)
    parsed_html = bs(get(link).content, 'html.parser')
    title = fetch_title(parsed_html)
    links = fetch_links(parsed_html)
    print("=> Downloading {} images".format(len(links)))
    download(title, links)


def fetch_title(html):
    try:
        spans = html.select('h1.title span')
        title = ''.join([
            span.string
            for span in spans
            if isinstance(span.string, str)
        ])
        mkdir(title)
        return title
    except FileExistsError:
        print('=> Already downloaded file...')
        raise SystemExit


def fetch_links(html):
    print('=> Fetching Links')
    a_tags = html.select("a.gallerythumb")
    return [
        base_url + a['href']
        for a in a_tags
    ]


def fetch_image_source(link):
    html = bs(get(link).content, 'html.parser')
    image = html.select_one('#image-container img')
    return image["src"]


def download(title, links):
    images = list(map(fetch_image_source, links))
    for index, image in enumerate(images):
        image_file = get(image)
        extention = ''.join(image.split(".")[-1:])
        file_path = f'{title}/{index:03}.{extention}'
        open(file_path, "wb").write(image_file.content)
        print("* {}".format(file_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download from website")
    parser.add_argument(
        "id", help="unique number in link")
    args = parser.parse_args()
    main(args.id)
