#make sure ur in cmd not powershell
#cd C:\Users\aleks\dev\python_projects\SKORPZ\skorpzbot
#-m venv SkorpzEnv
#SkorpzEnv\Scripts\Activate

from flask import Flask, request, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form action="/scrape" method="post">
        <label for="url">Enter URL:</label>
        <input type="text" id="url" name="url" required>
        <button type="submit">Scrape</button>
    </form>
    '''

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return render_template_string('''
    <h1>Scraped Content</h1>
    <pre>{{ content }}</pre>
    <a href="/">Go Back</a>
    ''', content=soup.prettify())

if __name__ == "__main__":
    app.run(debug=True)

