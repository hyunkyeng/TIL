import requests
from datetime import datetime, timedelta
import os
import csv
import json
from pprint import pprint

time1 = datetime(2019, 1, 13)
time_1 = time1.strftime("%Y%m%d")

token = os.getenv("KOBIS_TOKEN")
L = []
L_name = []

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(10):
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={time_1}&weekGb=0&itemPerPage=10'
        req = requests.get(url).json()
        for i in range(10):
            movie_co = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"]
            tit = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieNm"]
            aud = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]["audiAcc"]
            recorded = time_1
            if movie_co not in L:
                writer.writerow({'movie_code': movie_co, 'title': tit, 'audience': aud, 'recorded_at': recorded})
                L.append(movie_co)
                L_name.append(tit)
        
        time1 = time1 - timedelta(days=7)
        time_1 = time1.strftime("%Y%m%d")

with open('boxoffice.csv', 'r', encoding='utf-8') as f:
   lines = f.readlines()
   for line in lines:
       print(line.strip().split(','))


with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', "movieNm", "movieNmEn", "movieNmOg", "prdtYear", "showTm", "genres", "directors", "watchGradeNm", "actor1", "actor2", "actor3")
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(len(L)):
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={L[i]}'
        req = requests.get(url).json()
        movie_code = L[i]
        movieNm = req["movieInfoResult"]["movieInfo"]["movieNm"]
        movieNmEn = req["movieInfoResult"]["movieInfo"]["movieNmEn"]
        movieNmOg = req["movieInfoResult"]["movieInfo"]["movieNmOg"]
        prdtYear = req["movieInfoResult"]["movieInfo"]["prdtYear"]
        showTm = req["movieInfoResult"]["movieInfo"]["showTm"]
        genres = req["movieInfoResult"]["movieInfo"]["genres"][0]["genreNm"]
        directors = req["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"]
        watchGradeNm = req["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]
        actor_plus = req["movieInfoResult"]["movieInfo"]["actors"]

        if len(actor_plus) < 3:
            if len(actor_plus) == 0:
                actor_1 = ''
                actor_2 = ''
                actor_3 = ''

            if len(actor_plus) == 1:
                actor_1 = actor_plus[0]["peopleNm"]
                actor_2 = ''
                actor_3 = ''

            if len(actor_plus) == 2:
                actor_1 = actor_plus[0]["peopleNm"]
                actor_2 = actor_plus[1]["peopleNm"]
                actor_3 = ''
        else:
            actor_1 = actor_plus[0]["peopleNm"]
            actor_2 = actor_plus[1]["peopleNm"]
            actor_3 = actor_plus[2]["peopleNm"]



        writer.writerow({'movie_code': movie_code, 'movieNm': movieNm, 'movieNmEn': movieNmEn, 'movieNmOg': movieNmOg, 'prdtYear': prdtYear, 'showTm': showTm, 'genres': genres, 'directors': directors, 'watchGradeNm': watchGradeNm, 'actor1': actor_1, 'actor2': actor_2, 'actor3': actor_3})


with open('movie.csv', 'r', encoding='utf-8') as f:
   lines = f.readlines()
   for line in lines:
       print(line.strip().split(','))





CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

naver_token = {'X-Naver-Client-Id': CLIENT_ID, 'X-Naver-Client-Secret': CLIENT_SECRET}



with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'image_url', 'text_link', 'user_score')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    zip_list = list(zip(L_name, L))
    for i in range(len(zip_list)):
        curl = f'https://openapi.naver.com/v1/search/movie.json?query={zip_list[i][0]}'
        req = requests.get(curl, headers=naver_token).json()
        movie_code = zip_list[i][1]
        image_url = req["items"][0]["image"]
        text_link = req["items"][0]["link"]
        user_score = req["items"][0]["userRating"]
        writer.writerow({'movie_code': movie_code, 'image_url': image_url, 'text_link': text_link, 'user_score': user_score})

with open('movie_naver.csv', 'r', encoding='utf-8') as f:
   lines = f.readlines()
   for line in lines:
       print(line.strip().split(','))