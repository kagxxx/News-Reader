import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("news for today.. lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=294e1180c6bc4a9aa16a2e0a940db4a9"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for index,article in enumerate(arts):
        print(article['title'])
        speak(article['title'])
        speak("moving on to the next news..")
    speak("THANKYOU...")