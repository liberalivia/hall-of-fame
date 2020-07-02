import requests
from bs4 import BeautifulSoup

def multiscrape(username):

    def myscrape(site, size, name):

        # here is the form data
        data = {
            'nick' : username,
            'hallsize' : size
        }

        # Get the page
        # use .post
        # send the data
        url = site
        response = requests.post(url, data=data)
        doc = BeautifulSoup(response.text, 'html.parser')

        # look for what I want
        container = doc.find(id="MainContainer")
        content = container.find(id="pageContent")

        # it is in a table, which I am sure there are easy ways to parse, but I do know that it is always inside the first <th> tag
        userdata = content.find_all("th")
        alltime = userdata[0]

        # now I am going to turn it into a string, so that I can cut off the <th> tags!
        answer = str(alltime)
        print(name,"",answer[4:-5])

    # yes, I could probably find a way to use a function to generate all these too
    myscrape("https://www.puzzle-nonograms.com/hall.php", 0, "5x5 nonograms")
    myscrape("https://www.puzzle-nonograms.com/hall.php", 1, "10x10 nonograms")
    myscrape("https://www.puzzle-nonograms.com/hall.php", 2, "15x15 nonograms")
    myscrape("https://www.puzzle-nonograms.com/hall.php", 3, "20x20 nonograms")
    myscrape("https://www.puzzle-nonograms.com/hall.php", 4, "25x25 nonograms")
    print("\n")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 0, "5x5 easy shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 1, "5x5 normal shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 2, "7x7 easy shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 3, "7x7 normal shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 4, "7x7 hard shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 5, "10x10 easy shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 6, "10x10 normal shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 7, "10x10 hard shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 8, "15x15 easy shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 9, "15x15 normal shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 10, "15x15 hard shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 11, "20x20 easy shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 12, "20x20 normal shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 13, "20x20 hard shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 14, "25x25 easy shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 15, "25x25 normal shingoki")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 16, "25x25 hard shingoki")

    print("\n")
    myscrape("https://www.puzzle-shingoki.com/hall.php", 0, "5x5 easy shingoki")

multiscrape ("russellan")
