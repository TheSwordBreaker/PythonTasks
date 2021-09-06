import requests
import json
import concurrent.futures
import os

from bs4 import BeautifulSoup


BASE_URL = "https://www.rottentomatoes.com/"
MAX_THREADS = 30
FILE_PATH = "data/new_movie.json"
FILE_PATH = os.path.join(os.getcwd(), FILE_PATH)


def getMovieDetails(url):
    movieHtml = requests.get(url)
    soup = BeautifulSoup(movieHtml.content, "html.parser")
    movieHtmlData = soup.find("div", attrs={"id": "mainColumn"})
    name = movieHtmlData.find(
        "h1", attrs={"data-qa": "score-panel-movie-title"}).get_text()
    name = name.strip()
    # print(name)
    audienceScore = movieHtmlData.find(
        "score-board", attrs={"class": "scoreboard"})["audiencescore"]
    tomatometerScore = movieHtmlData.find(
        "score-board", attrs={"class": "scoreboard"})["tomatometerscore"]

    # print(audienceScore, tomatometerScore)
    desc = movieHtmlData.find("div", attrs={"id": "movieSynopsis"}).get_text()
    desc = desc.strip()

    # print(name, audienceScore, tomatometerScore)
    releaseDate = movieHtmlData.find(
        "ul", attrs={"class": "content-meta"}).find("time")

    if releaseDate != None:
        releaseDate = releaseDate.get_text()
        releaseDate = releaseDate.strip()

    print(f"Saving info of {name } { releaseDate} ")

    movie = {"Title": name,
             "AUDIENCE SCORE ": audienceScore,
             "TOMATOMETER": tomatometerScore,
             "Release Date": releaseDate,
             "Synopsis": desc
             }
    movie = json.dumps(movie)
    movies = [movie]
    temp = ""

    with open(FILE_PATH, "r") as f:
        temp = f.read()

    # print(temp)
    if temp != "":
        temp = json.loads(temp)
        # print(temp)
        movies = temp + movies

    with open(FILE_PATH, "w") as f:
        f.write(json.dumps(movies))

    # print(movie)

    # print("####")


def getMoviesList(url):
    moviesHtml = requests.get(url)
    soup = BeautifulSoup(moviesHtml.content, "html.parser")
    moviesList = soup.find_all(
        "div", attrs={"class": "ordered-layout__list"})[0]
    names = moviesList.find_all("span", attrs={"class": "p--small"})

    urls = moviesList.find_all("a", attrs={"slot": "caption"})

    urls = ["https://www.rottentomatoes.com" + x["href"] for x in urls]

    print("\n".join(urls[:3]))
    print(f"Total  Movies: { len(urls) }")

    return urls


def main():
    print("Getting latest Movie form rotten tomamto")
    moviesUrls = getMoviesList(BASE_URL)
    movieData = []

    if not os.path.exists(FILE_PATH):
        os.mkdir("data")
        print("Data File is No exist. creating file ")
        f = open(FILE_PATH, "w")
        f.write("")
        f.close()

    threads = min(MAX_THREADS, len(moviesUrls))
    print("Starting to scrap data for movies")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(getMovieDetails, moviesUrls)

    # for movieUrl in moviesUrls:
    #     movieData += [getMovieDetails(movieUrl)]
    # print(movieData)

    # getMovieDetails(
    #     "https://www.rottentomatoes.com/m/Queenpins")

    print("Work Completed !!!")


if __name__ == '__main__':
    main()
