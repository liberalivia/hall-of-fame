import requests
from bs4 import BeautifulSoup
import csv

def multiscrape(username):

    #this first nested function figures out how many versions there are of each puzzle
    def numberscrape(site):

        #get the page
        url = "https://www.puzzle-"+site+".com/hall.php"
        page0 = requests.get(url)
        doc0 = BeautifulSoup(page0.text, 'html.parser')

        #find what I want
        form0 = doc0.find("form")
        option0 = form0.find_all("option")

        #count how many options. note to self that this starts from 1 not 0
        number0 = len(option0)

        def myscrape(size):

            # here is the form data
            data = {
                'nick' : username,
                'hallsize' : size
            }

            # I've already got the url, but have to request it again with .post
            # send the data
            response = requests.post(url, data=data)
            doc = BeautifulSoup(response.text, 'html.parser')

            # hah, apparently I didn't need to go down one level at a time, which makes sense
            # it is in a table, which I am sure there are easy ways to parse, but I do know that it is always inside the first <th> tag
            userdata = doc.find_all("th")
            alltime = userdata[0]
            alltime1 = alltime.string

            # it lists your position and your time in the same string, so we need to split those up
            # but if you have no highscore it returns "n/a", so first we need to check for that
            if " " in alltime1:
                position, time = alltime1.split(" ", 1)
                #time has unhelpful brackets around it
                timenb = time[1:-1]
            else:
                position = ""
                timenb = ""

            # scrape the name of the puzzle
            puzzle = doc.find(class_="on")

            #and output! This time to a csv. "a" parameter lets me add to the file even though we're doing this over and over again
            with open("highscores.csv", "a") as highscores:
                highscores_writer = csv.writer(highscores, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

                highscores_writer.writerow([puzzle.string, position, timenb])

        #run the scrape as many times as there are puzzles on that site
        for i in range(number0):
            myscrape(i)

    # ok, so now it might still be prettier to have these in some kind of list, but this works
    numberscrape("shingoki")
    numberscrape("masyu")
    numberscrape("stitches")
    #annoyingly the site does not name the Aquarium puzzles
    numberscrape("aquarium")
    numberscrape("tapa")
    numberscrape("star-battle")
    numberscrape("kakurasu")
    numberscrape("skyscrapers")
    numberscrape("futoshiki")
    numberscrape("words")
    numberscrape("shakashaka")
    numberscrape("kakuro")
    numberscrape("jigsaw-sudoku")
    numberscrape("killer-sudoku")
    numberscrape("binairo")
    numberscrape("nonograms")
    numberscrape("loop")
    numberscrape("sudoku")
    numberscrape("light-up")
    numberscrape("bridges")
    numberscrape("shikaku")
    numberscrape("nurikabe")
    numberscrape("dominosa")

multiscrape ("russellan")
