import requests
from bs4 import BeautifulSoup

URL="https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")

# print(soup.prettify())
all_movies=soup.find_all(name="h3",class_="jsx-1913936986")
print(all_movies)

movie_titles=[movie.getText() for movie in all_movies]

print(movie_titles[::-1])

# movies=movie_titles[::-1]

# with open("movies.txt",mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")