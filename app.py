#!/usr/bin/env python

# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for


#this will do the search if it is fed already. to feed it use other script
from whoosh.qparser import MultifieldParser
from whoosh.index import open_dir


import json

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the default URL, which loads the form
@app.route('/searchbar/')
def searchbar():
    return render_template('form_submit.html')




@app.route('/viewer/')
def viewer():
    return render_template('viewer.html')

@app.route('/contactos/')
def contactos():
    return render_template('contactos.html')



@app.route('/pub1/')
def pub1():
    return render_template('pub1.html')

@app.route('/pub2/')
def pub2():
    return render_template('pub2.html')

@app.route('/pub3/')
def pub3():
    return render_template('pub3.html')

@app.route('/pub4/')
def pub4():
    return render_template('pub4.html')

@app.route('/pub5/')
def pub5():
    return render_template('pub5.html')

@app.route('/pub6/')
def pub6():
    return render_template('pub6.html')


@app.route('/pub07-08/')
def pub7():
    return render_template('pub07-08.html')

@app.route('/pub09-10/')
def pub9():
    return render_template('pub09-10.html')

@app.route('/pub11/')
def pub11():
    return render_template('pub11.html')

@app.route('/pub12/')
def pub12():
    return render_template('pub12.html')

@app.route('/pub13-14/')
def pub13():
    return render_template('pub13-14.html')

@app.route('/pub15-16/')
def pub15():
    return render_template('pub15-16.html')

@app.route('/pub17-18/')
def pub17():
    return render_template('pub17-18.html')

@app.route('/pub19-20/')
def pub19():
    return render_template('pub19-20.html')

@app.route('/pub21-22/')
def pub21():
    return render_template('pub21-22.html')



# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/searchterm/', methods=['POST'])


def searchterm():
    search_term=request.form['search_term']
    ix = open_dir("indexdir")
    with ix.searcher() as searcher:
        query = MultifieldParser(["title","author","secondauthor","publication"], ix.schema).parse(search_term)
        results = searcher.search(query, limit=20)
        result_dict = {}
        for result in results:
            headline_jpeg = "imgs/publications/pub" + result['publication'] + "/" + result['path'].split("/")[-1] + ".jpg"
            result_dict[result['path']] = [result['title'],result['author'],result['publication'], headline_jpeg]
            
        
    return render_template('form_action.html', search_terms=result_dict, orig_search = search_term)


# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000")
  )

