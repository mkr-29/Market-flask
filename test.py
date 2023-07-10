# import requests

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=FPYT7LRMOJA8N7IA'
# r = requests.get(url)
# data = r.json()

# print(data)


import requests

url = ('https://newsapi.org/v2/everything?'
       'q='
       'from=2023-07-06&'
       'sortBy=popularity&'
       'apiKey=a34c4bf76c2b453faec68e5280ed88db')

response = requests.get(url)

print (response.json())

# convert to list
data = response.json()
print(data['articles'][0]['title'])
print(data['articles'][0]['description'])
print(data['articles'][0]['url'])
print(data['articles'][0]['urlToImage'])
print(data['articles'][0]['publishedAt'])
print(data['articles'][0]['content'])

