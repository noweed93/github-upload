import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

class commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("you have not told me your name yet")
            else:
                self.respond("my name is python commander. how are you?")
        else:
            f = Fetcher("https://www.google.com/search?sxsrf=ALeKk00gCIH5APt1HILNIDUoIcCQ69yKng%3A1589124948400&ei=VB-4XrH6F8GZkwXy7KXwDQ&q=" + text)
            answer = f.lookup()
            self.respond(answer)

        '''if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            os.system(app)'''

    def respond(self, response):
        print(response)
        subprocess.call('PowerShell -Command "Add-Type –AssemblyName System.Speech; ' +
                        '(New-Object System.Speech.Synthesis.SpeechSynthesizer).' +
                        "Speak('" + response + "'" + ');"', shell=True)