# Import statements
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from urllib.request import Request
import json


# Getting URL
my_url = input("Enter genius URL of artist: ")

# Setting a known brower user agent
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

# Opening up connection, grabbing the page
u_client = ureq(req)
page_html = u_client.read()
u_client.close()

# Does HTML parsing
page_soup = soup(page_html, "html.parser")

# Instantiating json to store lyrics
song_json = {}
song_json["Lyrics"] = []

# Grabs each songs from artist page
containers = page_soup.findAll("div", {"class": "mini_card_grid-song"})

# For each song, go to URL and grab lyrics
for container in containers:
    song_url = container.a["href"]
    req = Request(song_url, headers={'User-Agent': 'Mozilla/5.0'})
    u_client = ureq(req)
    song_page_html = u_client.read()
    u_client.close()
    song_page_soup = soup(song_page_html, "html.parser")
    page_lyrics = song_page_soup.findAll("div", {"class": "lyrics"})
    lyrics = page_lyrics[0].p.text.strip().split('\n')
    song_json["Lyrics"].append(lyrics)  # Storing lyrics in json
    
# Dumping lyrics into a json file
with open("lyricsdata.json", "w", encoding="utf-8") as file:
    json.dump(song_json, file, indent = 5, ensure_ascii = False)

print("Data extraction done.")
