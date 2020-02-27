#!/usr/local/bin/python3

import argparse
from requests import get
from bs4 import BeautifulSoup as bs


def main(link):
    parsed_html = bs(get(link).content, 'html.parser')
    links = fetch_links(parsed_html)
    print("=> Downloading {} images".format(len(links)))
    download(links)


def fetch_links(html):
    print('=> Fetching Links')
    a_tags = html.select("a.gallerythumb")
    return list(
        map(
            lambda a: 'https://baseurl.com' + a["href"], a_tags
        )
    )


def fetch_image_source(link):
    html = bs(get(link).content, 'html.parser')
    image = html.select_one('#image-container img')
    return image["src"]


def download(links):
    images = list(map(fetch_image_source, links))
    for image in images:
        image_file = get(image)
        file_name = "".join(image.split("/")[-1:])
        open(file_name, "wb").write(image_file.content)
        print("* {}".format(file_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download from website")
    parser.add_argument("link", help="The link with the id")
    args = parser.parse_args()
    main(args.link)
