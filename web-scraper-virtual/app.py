#app.py
### 
''' This the main app file ,it covers following services:
        *Given a Public URL it returns the following statistics:
        -extract data from web page
        -Each word's frequency
        -Longest word
        -Most common letter
        --as a bonus point it also draws a graph with data 
'''


# Importing built-in and external libraries 
from flask import Flask, jsonify, url_for,request, render_template,redirect 
from bs4 import BeautifulSoup
import requests
from collections import Counter 
import string 



# Define app class 
app = Flask(__name__)



# Standard HTTP GET should guarantee index.html page rendering 
@app.route("/", methods=["GET","POST"])
def scraper():
    return render_template("index.html")


# HTTP POST method to utilize input from the user on front end
@app.route("/scraped/", methods=["POST"])
def scraped():
    info = request.form["info"]
    #if info == "":
     #   return render_template("error.html")
    try:
        requests.get(info)
    except:
        return render_template("error.html")

    page = requests.get(info)
    soup = BeautifulSoup(page.text, "html.parser")

    # Removing uncessary tags and their contents from our text 
    for script in soup.find_all(["script", "footer", "style", "head", "meta", "noscript", ""]):
        script.decompose()
    
  
    data = soup.find('body').get_text()
    
    
    # Most common Letter
    a = Counter([x.lower() for y in data for x in y.split()])
    b = a.most_common()
    mixed_bags = [x[0] for x in b]
    
    # Finding out if our letters are alphabets or not 
    letters_only = []
    for y in mixed_bags:
        if y.isalpha() == True:
            letters_only.append(y)
      
    
    # Each word's frequency 
    soupa = BeautifulSoup(page.content)
    texts = soupa.findAll(text=True)
   
        
    bb = Counter([x.lower() for y in texts for x in y.split()])
    cc = bb.most_common()
   
    # Find out if our words are correct or not 
    words_only = []
    for x in cc:
        if x[0].isalnum() == True:
            words_only.append(x)
        
    # Longest word 
    all_words = [x[0] for x in words_only]
    words = []
    for y in all_words:
        if y.isalnum() == True:
            words.append(y)
    longest_word = max(words, key=len)
    return render_template("scraped.html", letters_only=letters_only, words_only=words_only, longest_word=longest_word)


# Custom Error handler
@app.errorhandler(404)
def erroring(e):
    return render_template("error.html", e )



# host can be changed to '0.0.0.0' if there is a need for other device access to server
if __name__=="__main__":
    app.run(host='127.0.0.1', debug=True, port='8000')

