# apparently I need to do this every time?

import requests
import BeautifulSoup

# I imagine I could automate more of this but I am going to do it manually because I don't know how. So we're doing one page at at time

# 5x5 nonograms
# here is the form data
data = {
    'nick' : 'russellan',
    'hallsize' : 0
}

# Get the page
# use .post
# send the data
n5url = "https://www.puzzle-nonograms.com/hall.php"
n5response = requests.post(n5url, data=data)
n5doc = BeautifulSoup(n5response.text, 'html.parser')

# look for what I want
n5container = n5doc.find(id="MainContainer")
n5content = n5container.find(id="pageContent")

# it is in a table, which I am sure there are easy ways to parse, but I do know that it is always inside the first <th> tag
n5userdata = n5content.find_all("th")
n5alltime = n5userdata[0]

# now I am going to turn it into a string, so that I can cut off the <th> tags!
n5answer = str(n5alltime)
print("5x5 nonograms    ",n5answer[4:-5])

# 10x10 nonograms

data = {
    'nick' : 'russellan',
    'hallsize' : 1
}

n10url = "https://www.puzzle-nonograms.com/hall.php"
n10response = requests.post(n10url, data=data)
n10doc = BeautifulSoup(n10response.text, 'html.parser')
n10container = n10doc.find(id="MainContainer")
n10content = n10container.find(id="pageContent")
n10userdata = n10content.find_all("th")
n10alltime = n10userdata[0]
n10answer = str(n10alltime)
print("10x10 nonograms  ",n10answer[4:-5])

# 15x15 nonograms

data = {
    'nick' : 'russellan',
    'hallsize' : 2
}

n15url = "https://www.puzzle-nonograms.com/hall.php"
n15response = requests.post(n15url, data=data)
n15doc = BeautifulSoup(n15response.text, 'html.parser')
n15container = n15doc.find(id="MainContainer")
n15content = n15container.find(id="pageContent")
n15userdata = n15content.find_all("th")
n15alltime = n15userdata[0]
n15answer = str(n15alltime)
print("15x15 nonograms  ",n15answer[4:-5])


# 20x20 nonograms

data = {
    'nick' : 'russellan',
    'hallsize' : 3
}

n20url = "https://www.puzzle-nonograms.com/hall.php"
n20response = requests.post(n20url, data=data)
n20doc = BeautifulSoup(n20response.text, 'html.parser')
n20container = n20doc.find(id="MainContainer")
n20content = n20container.find(id="pageContent")
n20userdata = n20content.find_all("th")
n20alltime = n20userdata[0]
n20answer = str(n20alltime)
print("20x20 nonograms  ",n20answer[4:-5])

# 25x25 nonograms

data = {
    'nick' : 'russellan',
    'hallsize' : 4
}

n25url = "https://www.puzzle-nonograms.com/hall.php"
n25response = requests.post(n25url, data=data)
n25doc = BeautifulSoup(n25response.text, 'html.parser')
n25container = n25doc.find(id="MainContainer")
n25content = n25container.find(id="pageContent")
n25userdata = n25content.find_all("th")
n25alltime = n25userdata[0]
n25answer = str(n25alltime)
print("25x25 nonograms  ",n25answer[4:-5])

# 5x5 easy shingoki

data = {
    'nick' : 'russellan',
    'hallsize' : 0
}

sh5eurl = "https://www.puzzle-shingoki.com/hall.php"
sh5eresponse = requests.post(sh5eurl, data=data)
sh5edoc = BeautifulSoup(sh5eresponse.text, 'html.parser')
sh5econtainer = sh5edoc.find(id="MainContainer")
sh5econtent = sh5econtainer.find(id="pageContent")
sh5euserdata = sh5econtent.find_all("th")
sh5ealltime = sh5euserdata[0]
sh5eanswer = str(sh5ealltime)
print("\n5x5 easy shingoki  ",sh5eanswer[4:-5])

# 5x5 normal shingoki

data = {
    'nick' : 'russellan',
    'hallsize' : 1
}

sh5nurl = "https://www.puzzle-shingoki.com/hall.php"
sh5nresponse = requests.post(sh5nurl, data=data)
sh5ndoc = BeautifulSoup(sh5nresponse.text, 'html.parser')
sh5ncontainer = sh5ndoc.find(id="MainContainer")
sh5ncontent = sh5ncontainer.find(id="pageContent")
sh5nuserdata = sh5ncontent.find_all("th")
sh5nalltime = sh5nuserdata[0]
sh5nanswer = str(sh5nalltime)
print("5x5 normal shingoki  ",sh5nanswer[4:-5])
