import requests
page = requests.get('https://www.met.ie/forecasts/dublin')


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


forecast = soup.find("div", "forecast")
count = 0

for child in forecast.children:
  count = count + 1
  if(count == 4 or count == 6 or count == 8 or count == 10):
    result = child.get_text()


from win10toast import ToastNotifier

popup = ToastNotifier()

popup.show_toast("Weather Update", result, duration = 8)

