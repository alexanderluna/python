from requests import get
from bs4 import BeautifulSoup as bs

titles = [
    'One Piece',
]


def main():
    link = "https://nyaa.si/user/HorribleSubs"
    parsed = bs(get(link, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0"}).content, 'html.parser')
    print(parsed)
    for row in parsed.findAll('tr'):
        episode = searchForEpisode(row)
        if episode:
            torrent = getTorrentFrom(row)
            download(torrent, episode)


def searchForEpisode(row):
    for a in row.findAll('a'):
        a = a.string
        if a is not None and "720" in a and any(anime in a for anime in titles):
            print(a)
            return a


def getTorrentFrom(row):
    for a in row.findAll('a'):
        if "torrent" in a['href']:
            return a['href']


def download(torrentUrl, episode):
    filePath = "/Users/alexander/Downloads/_tmp/_torrents/"
    filename = filePath + episode + ".torrent"
    torrent = get("https://nyaa.si" + torrentUrl)
    open(filename, 'wb').write(torrent.content)


if __name__ == "__main__":
    main()
