from bs4 import BeautifulSoup
import requests

# This code for looking a starter url which is IMDB website for movies.
starter_url = "https://www.imdb.com/"
r = requests.get(starter_url)
data = r.text
soup = BeautifulSoup(data)
counter = 0

# After scrapping all the urls from the website IMDB we will look at the first 15 and save it in a text file.
with open('all_urls.txt', 'w') as f:
    for link in soup.find_all('a'):
        print(link.get('href'))
        f.write(str(link.get('href')) + '\n\n')
        if counter > 15:
            break
        counter += 1
print("end of crawler")

# This code looks at the url for which we want the data to be scraped to create the knowledge base.
# I have taken here the list of top-rated movies from IMDB.
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    count = len(movies)
    print("Total number of movies in IMDB rating list: ", count)

    file1 = open("IMDB Movie Ratings.txt", "w")

    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text
        # strip=True here removes newlines, tabs, spaces etc.
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text

        print(rank, name, year, rating)

        new = rank + name + year + rating
        file1.write(new)

except Exception as e:
    print(e)

file1.close()
