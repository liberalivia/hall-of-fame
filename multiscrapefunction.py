import requests
from bs4 import BeautifulSoup
import csv
import time
import concurrent.futures
import sys

helptext = "This script finds puzzle highscores. Enter up to two usernames in the form 'multiscrapefunction.py username1 username2', or run multiscrapefunction.py without arguments and it will prompt you for two usernames. If you only want to find the scores for one username press return when asked for the second username."

#defining some things

#puzzles = ["shingoki", "masyu", "stitches", "aquarium", "tapa", "star-battle", "kakurasu", "skyscrapers", "futoshiki", "words", "shakashaka", "kakuro", "jigsaw-sudoku", "killer-sudoku", "binairo", "nonograms", "loop", "sudoku", "light-up", "bridges", "shikake", "nurikabe", "dominosa"]
# comment out the line above and use the one below if you're testing to see if new features work as expected
puzzles = ["masyu", "aquarium"]

# a very bad way of taking the usernames from the command line.
# I feel like I should be using argparse and including help messages and so on, but in some ways that makes things a lot more complicated?
# and if I ever do want to make this work for more than 2 usernames then I'll have to completely change the structure anyway
if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
    print(helptext)
    exit()
elif len(sys.argv) > 3:
    print("This script currently only supports up to two usernames.")
    print(helptext)
    exit()
elif len(sys.argv) == 3:
    usernameA = sys.argv[1]
    usernameB = sys.argv[2]
elif len(sys.argv) == 2:
    usernameA = sys.argv[1]
elif len(sys.argv) == 1:
    usernameA = input('Enter first username: ')
    usernameB = input('Enter second username, or press return to continue with a single username: ')
else:
    print(helptext)
    quit()


#ok, now we basically have two fairly similar functions for the case of 1 and 2 usernames. I could probably figure out how to do this without repeating everything.

def multiscrapesingle():
    # start a new csv and put in headers
    with open("highscores.csv", "w") as highscores:
        highscores_writer = csv.writer(highscores, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        highscores_writer.writerow(["puzzle", usernameA + ": position", usernameA + ": time"])


    #figure out how many versions there are of each puzzle
    def numberscrapesingle(site):

        #get the page
        url = "https://www.puzzle-"+site+".com/hall.php"
        page0 = requests.get(url)
        doc0 = BeautifulSoup(page0.text, 'html.parser')

        #find what I want
        form0 = doc0.find("form")
        option0 = form0.find_all("option")

        #count how many options. note to self that this starts from 1 not 0
        number0 = len(option0)

        def myscrapesingle(size):

            # here is the form data
            dataA = {
                'nick' : usernameA,
                'hallsize' : size
            }

            # I've already got the url, but have to request it again with .post
            # send the data
            responseA = requests.post(url, data=dataA)
            docA = BeautifulSoup(responseA.text, 'html.parser')

            # hah, apparently I didn't need to go down one level at a time, which makes sense
            # it is in a table, which I am sure there are easy ways to parse, but I do know that it is always inside the first <th> tag
            userdataA = docA.find_all("th")
            alltimeA = userdataA[0]
            alltime1A = alltimeA.string

            # it lists your position and your time in the same string, so we need to split those up
            # but if you have no highscore it returns "n/a", so first we need to check for that
            # also I had an object called time which was going to cause problems later
            if " " in alltime1A:
                positionA, ttimeA = alltime1A.split(" ", 1)
                # for the comparison later, we need to make sure that python recognises your position as a number
                intpositionA = int(positionA)
                # your time has unhelpful brackets around it
                timenbA = ttimeA[1:-1]
            else:
                positionA = ""
                timenbA = ""

            # scrape the name of the puzzle
            puzzle = docA.find(class_="on")

            #and output! This time to a csv. "a" parameter lets me add to the file even though we're doing this over and over again
            with open("highscores.csv", "a") as highscores:
                highscores_writer = csv.writer(highscores, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

                #just fixing the fact that the naming is inconsistent on aquarium
                if site == "aquarium":
                    aqpuzzle = "Aquarium " + puzzle.string
                    highscores_writer.writerow([aqpuzzle, positionA, timenbA])
                else:
                    highscores_writer.writerow([puzzle.string, positionA, timenbA])

            # I have learned that this is good practice
            time.sleep(0.25)

        #run the scrape as many times as there are puzzles on that site, now with threading
        threads = number0
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(myscrapesingle, range(number0))

    threads = len(puzzles)
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(numberscrapesingle, puzzles)

# and the function for 2 usernames:
def multiscrapedouble():
    # start a new csv and put in headers
    with open("highscores.csv", "w") as highscores:
        highscores_writer = csv.writer(highscores, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        highscores_writer.writerow(["puzzle", usernameA + ": position", usernameA + ": time", usernameB + ": position", usernameB +":time", "result"])


    #figure out how many versions there are of each puzzle
    def numberscrapedouble(site):

        #get the page
        url = "https://www.puzzle-"+site+".com/hall.php"
        page0 = requests.get(url)
        doc0 = BeautifulSoup(page0.text, 'html.parser')

        #find what I want
        form0 = doc0.find("form")
        option0 = form0.find_all("option")

        #count how many options. note to self that this starts from 1 not 0
        number0 = len(option0)

        def myscrapedouble(size):

            # here is the form data
            dataA = {
                'nick' : usernameA,
                'hallsize' : size
            }

            # I've already got the url, but have to request it again with .post
            # send the data
            responseA = requests.post(url, data=dataA)
            docA = BeautifulSoup(responseA.text, 'html.parser')

            # hah, apparently I didn't need to go down one level at a time, which makes sense
            # it is in a table, which I am sure there are easy ways to parse, but I do know that it is always inside the first <th> tag
            userdataA = docA.find_all("th")
            alltimeA = userdataA[0]
            alltime1A = alltimeA.string

            # it lists your position and your time in the same string, so we need to split those up
            # but if you have no highscore it returns "n/a", so first we need to check for that
            # also I had an object called time which was going to cause problems later
            if " " in alltime1A:
                positionA, ttimeA = alltime1A.split(" ", 1)
                # for the comparison later, we need to make sure that python recognises your position as a number
                intpositionA = int(positionA)
                # your time has unhelpful brackets around it
                timenbA = ttimeA[1:-1]
            else:
                positionA = ""
                timenbA = ""

            # now we do it all again for usernameB

            dataB = {
                'nick' : usernameB,
                'hallsize' : size
            }

            responseB = requests.post(url, data=dataB)
            docB = BeautifulSoup(responseB.text, 'html.parser')

            userdataB = docB.find_all("th")
            alltimeB = userdataB[0]
            alltime1B = alltimeB.string

            if " " in alltime1B:
                positionB, ttimeB = alltime1B.split(" ", 1)
                intpositionB = int(positionB)
                # your time has unhelpful brackets around it
                timenbB = ttimeB[1:-1]
            else:
                positionB = ""
                timenbB = ""

            # scrape the name of the puzzle
            puzzle = docA.find(class_="on")

            # now the all-important comparison
            if " " in alltime1A and " " in alltime1B:
                if intpositionA < intpositionB:
                    result = usernameA
                else:
                    result = usernameB
            elif " " in alltime1A:
                result = usernameA
            elif " " in alltime1B:
                result = usernameB
            else:
                result = ""


            #and output! This time to a csv. "a" parameter lets me add to the file even though we're doing this over and over again
            with open("highscores.csv", "a") as highscores:
                highscores_writer = csv.writer(highscores, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)

                #just fixing the fact that the naming is inconsistent on aquarium
                if site == "aquarium":
                    aqpuzzle = "Aquarium " + puzzle.string
                    highscores_writer.writerow([aqpuzzle, positionA, timenbA, positionB, timenbB, result])
                else:
                    highscores_writer.writerow([puzzle.string, positionA, timenbA, positionB, timenbB, result])

            # I have learned that this is good practice
            time.sleep(0.25)

        #run the scrape as many times as there are puzzles on that site, now with threading
        threads = number0
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(myscrapedouble, range(number0))

    # now I use threading here too. It doesn't seem to speed things up quite so much, not sure why.
    threads = len(puzzles)
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(numberscrapedouble, puzzles)

# deciding whether to use the one player or two player version

if len(sys.argv) == 1 and usernameB == "":
    multiscrapesingle()
elif len(sys.argv) in [1, 3]:
    multiscrapedouble()
elif len(sys.argv) == 2:
    multiscrapesingle()
else:
    print(helptext)
