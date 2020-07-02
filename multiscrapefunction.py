import requests
from bs4 import BeautifulSoup

def multiscrape(username):

    def myscrape(site, size):

        # here is the form data
        data = {
            'nick' : username,
            'hallsize' : size
        }

        # Get the page
        # use .post
        # send the data
        url = "https://www.puzzle-"+site+".com/hall.php"
        response = requests.post(url, data=data)
        doc = BeautifulSoup(response.text, 'html.parser')

        # look for what I want
        container = doc.find(id="MainContainer")
        content = container.find(id="pageContent")

        # it is in a table, which I am sure there are easy ways to parse, but I do know that it is always inside the first <th> tag
        userdata = content.find_all("th")
        alltime = userdata[0]

        # scrape the name of the puzzle
        puzzle = content.find(class_="on")

        #and output!
        print(puzzle.string, alltime.string)

    # yes, I could probably still find a way to use a function to generate all these too
    myscrape("nonograms", 0)
    myscrape("nonograms", 1)
    myscrape("nonograms", 2)
    myscrape("nonograms", 3)
    myscrape("nonograms", 4)
    print("\n")
    myscrape("shingoki", 0)
    myscrape("shingoki", 1)
    myscrape("shingoki", 2)
    myscrape("shingoki", 3)
    myscrape("shingoki", 4)

multiscrape ("russellan")
