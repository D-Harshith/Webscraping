import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
empires_response_html = response.text
soup = BeautifulSoup(empires_response_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
# # print(movie_titles)
# # movie_titles = []
# # for movie in all_movies:
# #     movie_titles.append(movie.getText())
# # print(movie_titles)
# # The error due to it is not finding h3 (title) from website.
movies = movie_titles[::-1]
with open("movies.txt", mode="w") as file:
    for m in movies:
        file.write(f"{m}\n")
