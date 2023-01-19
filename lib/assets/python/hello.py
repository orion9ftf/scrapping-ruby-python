import sys, requests, webbrowser, bs4

input = sys.argv[1]
print(input + " mmhhh")

# res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# linkElements = soup.select('.r a')
# linkToOpen = min(2, len(linkElements))
# for i in range(linkToOpen):
#   webbrowser.open('https://google.com'+linkElements[i].get('href'))
