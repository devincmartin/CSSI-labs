#main.py

import webapp2
import jinja2
import os
from models import MemeInfo
from google.appengine.api import urlfetch
import json

# This initializes the jinja2 environment
# THIS IS GOING TO BE THE SAME FOR EVERY APP YOU BUILD
# Jinja2.environment is a constructor

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# meme_templates = ["https://i.imgflip.com/2/1ur9b0.jpg", "https://i.imgflip.com/2/23ls.jpg", "https://i.imgflip.com/2/1ihzfe.jpg", "https://i.imgflip.com/2/1otk96.jpg", "https://i.imgflip.com/2/1h7in3.jpg", "https://i.imgflip.com/2/30b1gx.jpg", "https://i.imgflip.com/2/1bgw.jpg", "https://i.imgflip.com/2/265k.jpg"]

class Pokemon(object):
    def __init__(self, attack):
        self.attack = attack

#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        api_url = "https://api.imgflip.com/get_memes"
        imgflip_response = urlfetch.fetch(api_url).content
        imgflip_response_json = json.loads(imgflip_response)
        print(imgflip_response_json['data']['memes'])
        meme_templates = []
        for meme_template in imgflip_response_json['data']['memes'][0:10]:
            meme_templates.append(meme_template["url"])

        meme_dict = {
            "imgs": meme_templates
        }
        my_template_dict = {
        "isOn": False,
        # "myFavs": ["sushi", "spaghetti", "hot dogs"],
        # "myDict": {"name": "Ryan"},
        # "pokemon": Pokemon("FIRE")
        }
        # self.response.headers['Content-Type'] = 'text/html'
        # self.response.write("<h1>Ric Flair is the man<h1>")
        welcome_template = jinja_env.get_template('mainAE.html')
        # print(welcome_template.render())
        self.response.write(welcome_template.render(meme_dict))
        # my_template_dict

    def post(self):
        top_line = self.request.get("top-line")
        print(top_line)
        bottom_line = self.request.get("bottom_line")
        print(bottom_line)

class AboutPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/html'
        about_template = jinja_env.get_template("aboutPage.html")
        self.response.write(about_template.render())

class SupportPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<h3>Call Ric at 1-800-RIC.<h3>")

class InfoPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<h4>Ric is a 70 yr-old wrestler in the WWE<h4>")

class ResultPage(webapp2.RequestHandler):
    def post(self):
        top_line = self.request.get("top-line")
        bottom_line = self.request.get("bottom-line")
        meme_url = self.request.get("template")
        print(meme_url)
        data_dict = {
            "top": top_line,
            "bottom": bottom_line,
            "url": meme_url
        }

        meme = MemeInfo(meme_url = meme_url, top_line = top_line, bottom_line = bottom_line)
        meme.put()


        print(data_dict)
        result_template = jinja_env.get_template("result.html")
        self.response.write(result_template.render(data_dict))

class AllMemePage(webapp2.RequestHandler):
    def get(self):
        allMemes = MemeInfo.query().fetch()
        meme_dict = {
            "allUserMemes": allMemes
        }
        welcome_template = jinja_env.get_template('allMemePage.html')
        self.response.write(welcome_template.render(meme_dict))


# class saveAllMemes(ndb.Model):
#     def post(self):
#         top_line = ndb.StringProperty(required=True)
#         bottom_line = ndb.StringProperty(required=True)
#         meme_url = ndb.StringProperty(required=True)
#
#     def printsaveAllMemes(self):
#         print(self.top_line + " " + self.bottom_line + " " + self.meme_url)

# car1 = Car(carMake="ford", carModel="mustang")
# car2 = Car(carMake="toyota", carModel="prius")
# car1.printCarInfo()
# car2.printCarInfo()





'''
    See if you can get your link from the first page to hit this
    handler and load a completely different html page
'''



# the app configuration section
app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/about', AboutPage),
        ('/support', SupportPage),
        ('/info', InfoPage),
        ('/result', ResultPage),
        ('/allmemes', AllMemePage)
    ],
    debug = True
)
