import requests
from flask import Flask, render_template
app=Flask(__name__)

def fetchNewsData():
    url = ('https://newsapi.org/v2/everything?'
           'q=stock%20market&'  # Example query parameter: 'stock market'
           'from=2023-07-06&'
           'sortBy=popularity&'
           'apiKey=a34c4bf76c2b453faec68e5280ed88db')

    response = requests.get(url)
    data = response.json()
    
    # Extract the articles from the response data
    articles = data.get('articles', [])

    # Create a list to store the processed news items
    news_data = []
    
    for article in articles:
        # Extract the necessary fields from each article
        title = article.get('title', '')
        description = article.get('description', '')
        url=article.get('url','')
        
        # Create a dictionary representing the news item
        news_item = {
            'title': title,
            'details': description.split('\n') if description else [],
            'url': article.get('url', ''),
        }
        
        # Append the news item to the news data list
        news_data.append(news_item)
    
    return news_data


@app.route('/')
@app.route('/home')
def index():
    news_data = fetchNewsData()
    return render_template('home.html', news_data=news_data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')



# from alpha_vantage.timeseries import TimeSeries

# Initialize Alpha Vantage client with your API key
# api_key = 'YOUR_API_KEY'
# ts = TimeSeries(key=api_key)


if __name__=='__main__':
    app.run(host='0.0.0.0' ,debug=True)