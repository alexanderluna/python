#!/usr/bin/env python

import argparse
from time import sleep
from requests import get
from os import path, mkdir
from bs4 import BeautifulSoup as bs


def main(link):
    parsed_html = bs(get(link).content, 'html.parser')
    chapters = fetch_chapters_from(parsed_html)
    download_chapters(chapters)


def fetch_chapters_from(html) -> list[str]:
    print("=> Fetching chapters")
    chapters = list(map(lambda chapter: chapter["href"],
                        html.select("ul.list-chapters > a")))
    chapters.reverse()
    return chapters


def download_chapters(chapters: list[str]) -> None:
    print("=> downloading {} chapters".format(len(chapters)))
    for current_chapter, chapter in enumerate(chapters):
        folder = make_folder_for(current_chapter)
        if folder:
            images = fetch_images_from(chapter)
            download(images, folder)
            sleep(10)


def make_folder_for(chapter: int) -> str | None:
    folder_name = str(chapter).zfill(3)
    if path.exists(folder_name) or path.exists(f"{folder_name}.pdf"):
        return None
    print(f"\n=> Downloading {folder_name}")
    mkdir(folder_name)
    return folder_name


def fetch_images_from(chapter: str) -> list[str]:
    print("=> Parsing Images")
    parsed_chapter = bs(get(chapter).content, 'html.parser')
    return list(map(lambda img: img["data-src"],
                    parsed_chapter.select("#chapter-content > img")))


def download(images: list[str], folder: str) -> None:
    print(f"=> Downloading {len(images)} images")
    for index, image in enumerate(images):
        file_path = generate_file_path(index, image, folder)
        save_image(file_path, image)


def generate_file_path(index: int, image: str, folder: str) -> str:
    name = "".join(image.split("/")[-1:])
    return f"{folder}/{str(index).zfill(3)} {name}"


def save_image(file_path: str, image: str) -> None:
    image_file = get(image)
    open(file_path, "wb").write(image_file.content)
    print("* {}".format(file_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download manhwa.")
    parser.add_argument("link", help="The link of the main page")
    args = parser.parse_args()
    main(args.link)
