#!/usr/local/bin/python3

import os
import argparse
from time import sleep
from requests import get
from bs4 import BeautifulSoup as bs


def main(link):
    parsed_html = bs(get(link).content, 'html.parser')
    chapters = fetch_chapters_from(parsed_html)
    download_chapters(chapters)


def fetch_chapters_from(html):
    print("=> Fetching chapters")
    chapters = list(map(lambda chapter: chapter["href"],
                        html.select(".wp-manga-chapter > a")))
    chapters.reverse()
    return chapters


def download_chapters(chapters):
    print("=> downloading {} chapters".format(len(chapters)))
    for chapter in chapters:
        folder = make_folder_for(chapter)
        if folder:
            images = fetch_images_from(chapter)
            download(images, folder)
            sleep(30)


def make_folder_for(chapter):
    folder_name = "".join(chapter.split("/")[-2:-1])
    if not os.path.exists(folder_name):
        print("\n=> Downloading {}".format(folder_name))
        os.mkdir(folder_name)
        return folder_name
    return None


def fetch_images_from(chapter):
    print("=> Parsing Images")
    parsed_chapter = bs(get(chapter).content, 'html.parser')
    return list(map(lambda img: "".join(img["src"].strip().split("?")[0]),
                    parsed_chapter.select(".wp-manga-chapter-img")))


def download(images, folder):
    print("=> Downloading {} images".format(len(images)))
    for image in images:
        file_name = "".join(image.split("/")[-1:])
        file_path = "{}/{}".format(folder, file_name)
        image_file = get(image)
        open(file_path, "wb").write(image_file.content)
        print("* {}".format(file_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download manhwa.")
    parser.add_argument("link", help="The link of the main page")
    args = parser.parse_args()
    main(args.link)
