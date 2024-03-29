from flask import Flask
from waitress import serve
from template import display
#reference:https://www.youtube.com/watch?v=kng-mJJby8g
#Activate website or localhost
app = Flask(__name__)
app.register_blueprint(display, url_prefix="/Home.html/")

if __name__ == '__main__':
    #this will be changed due to server change
    serve(app, host="0.0.0.0", port=8080)
    #default host is 8080
    #localhost name is>> http://localhost:8080/DSVSpotQuotationMain/

