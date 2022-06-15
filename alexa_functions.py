import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import json
import requests
import os
import random
from playsound import playsound
import pyautogui
import time
from bs4 import BeautifulSoup
from threading import Thread
from pywikihow import search_wikihow
import wikipedia
import webbrowser
import sys


class AlexaCommands:
    def __init__(self, name: str = 'alexa'):
        self.say_random_quotes()
        self.name = name
        print(f'Hi! I am {self.name}! How may I help you?')
        self.talk(f'Hi! I am {self.name}! How may I help you?')

    def Listen(self):
        r = sr.Recognizer()
        query = ''
        try:
            with sr.Microphone() as source:
                r.pause_threshold = 2
                print('listening...')

                audio = r.listen(source, timeout=5, phrase_time_limit=8)
                print('recognizing...')
                query = r.recognize_google(audio, language='en-in')

        except sr.RequestError:
            print("[!] No internet connection.\n[!] Please connect to a network and try again")

        except sr.UnknownValueError:
            print('failed to recognisze')
        finally:
            return query.lower()

    def talk(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[1].id)
        engine.say(text)
        engine.runAndWait()

    def play_yt_video(self, topic):
        topic = topic.replace(self.name, '')
        topic = topic.replace('play', '').strip()
        print(f'playing... {topic}')
        self.talk(f'playing... {topic}')
        t = Thread(target=pywhatkit.playonyt, args=(topic,))
        t.start()

    def tell_current_time(self):
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(f'current time is {time}')
        self.talk(f"current time is {time}")

    def say_random_quotes(self):
        url = "http://py-quoters.herokuapp.com/"

        response = requests.request("GET", url)

        response = json.loads(response.text)

        print(f"{response['quote']}")
        self.talk(f"{response['quote']}")

    def play_random_local_music(self):
        path = f"C:\\Users\\{os.getlogin()}\\Music\\"
        songs = os.listdir(path)
        song = random.randint(0, len(songs))
        song = os.path.join(path, songs[song])
        if song.endswith('.mp3'):
            play_song = Thread(target=playsound, args=(song,))
            play_song.start()
        else:
            os.startfile(song)

    def shut_down_pc(self):
        print('are you sure you want to shutdown this computer')
        self.talk('are you sure you want to shutdown this computer')
        confirm = self.Listen()
        if 'yes' in confirm:
            print('shutting down the computer in 1 minute.')
            self.talk('shutting down the computer in 1 minute.')
            os.system('shutdown /s')
        else:
            print('shutdown aborted!')
            self.talk('shutdown aborted!')

    def restart_pc(self):
        print('are you sure you want to restart this computer')
        self.talk('are you sure you want to restart this computer')
        confirm = self.Listen()
        if 'yes' in confirm:
            print('restarting the computer in 1 minute.')
            self.talk('restarting the computer in 1 minute.')
            os.system('shutdown /r')
        else:
            print('restart aborted!')
            self.talk('restart aborted!')

    def locate_a_place_on_gmaps(self, location):
        location = location.replace("where is", "")
        location = location.replace(self.name, "")
        location = location.replace('locate', '').strip()

        print(f"locating {location} on google maps.")
        self.talk(f"locating {location} on google maps.")
        locating = Thread(target=webbrowser.open, args=(f"https://www.google.nl/maps/place/{location}",))
        locating.start()

    def acitvate_typing_mode(self):
        print('Typing mode! activated.')
        self.talk('Typing mode, activated')

        while True:
            query = self.Listen()
            if self.name in query and any(('stop' in query, 'deactivate' in query)):
                print('typing mode deactivated')
                self.talk('typing mode deactivated')
                break

            elif query != '':
                if 'press enter' in query:
                    pyautogui.press('enter')
                elif 'press space' in query:
                    pyautogui.typewrite(' ')
                elif 'full stop' in query:
                    pyautogui.typewrite('.')
                elif 'comma' in query:
                    pyautogui.typewrite(',')
                else:
                    pyautogui.typewrite(query)

    def open_site(self, website):
        website = website.replace(self.name, '')
        website = website.replace('open', '').strip()

        print(f'opening... {website}')
        self.talk(f'opening {website}')
        site = Thread(target=webbrowser.open, args=(f"http://{website}",))
        site.start()

    def google_search(self, query):
        query = query.replace(self.name, '')
        query = query.replace('search', '').strip()

        print(f'searching... {query}')
        self.talk(f'searching {query} on google')
        search = Thread(target=webbrowser.open, args=(f"https://google.com/search?q={query}",))
        search.start()

    def repeat_me(self, query):
        query = query.replace(self.name, '')
        query = query.replace('say', '')
        query = query.replace('se', '').strip()

        self.talk(query)

    def open_app(self, app_name):
        app_name = app_name.replace(self.name, '')
        app_name = app_name.replace('open', '').strip()

        print(f'opening... {app_name}')
        self.talk(f'opening... {app_name}')

        def app_open():
            search_location = pyautogui.locateOnScreen('TypeToSearch.png')
            pyautogui.click(search_location)
            pyautogui.sleep(2)
            pyautogui.typewrite(app_name)

            pyautogui.sleep(2)
            open_location = pyautogui.locateOnScreen('openButton.png')
            pyautogui.leftClick(open_location)

        app = Thread(target=app_open)
        app.start()

    def tell_my_ip(self):
        print('getting your ip. just a sec...')
        self.talk('getting your ip. just a second')
        ip = requests.get("https://api64.ipify.org/")
        ip = ip.text
        print(f"Your public ip address is {ip}")
        self.talk(f"Your public ip address is {ip}")

    def tell_my_ip_info(self):
        print('collecting data...')
        ip = requests.get("https://api64.ipify.org/")
        ip = ip.text

        ip_info = requests.get(f"https://ipinfo.io/{ip}/geo")

        ip_Info = json.loads(ip_info.text)

        ip = ip_Info['ip']
        city = ip_Info['city']
        region = ip_Info['region']
        country = ip_Info['country']
        timezone = ip_Info['timezone']

        print(f'''
        Your public ip address is {ip},
        city is {city},
        region is {region},
        country is {country},
        and timezone is {timezone}''')

        self.talk(
            f'Your public ip address is {ip}, city is {city}, region is {region}, country is {country}, and timezone is {timezone}')

    def i_am_bored(self):
        print('wait a sec...')
        activity = requests.get("https://www.boredapi.com/api/activity")
        activity = activity.text
        activity = json.loads(activity)
        print(activity['activity'])
        self.talk(activity['activity'])

    def guess_gender(self):
        print('tell me the name of the person')
        self.talk('tell me the name of the person')

        person_name = self.Listen()
        gender = requests.get(f"https://api.genderize.io/?name={person_name}")
        gender = gender.text

        gender = json.loads(gender)
        person_gender = gender['gender']
        person_name = gender['name']
        probability = gender['probability']

        print(f"The gender of {person_name} is {person_gender} with {probability * 100} % probability")
        self.talk(f"The gender of {person_name} is {person_gender} with {probability * 100} % probability")

    def tell_a_joke(self):
        print('fetching jokes...')
        joke = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = joke.text

        joke = json.loads(joke)
        setup = joke['setup']
        punchline = joke['punchline']

        print(setup)
        self.talk(setup)

        time.sleep(1.1)
        print(punchline)
        self.talk(punchline)

    def where_am_i(self):
        print('getting your location...')
        ip = requests.get("https://api64.ipify.org/")
        ip = ip.text

        ip_info = requests.get(f"https://ipinfo.io/{ip}/geo")

        ip_Info = json.loads(ip_info.text)

        city = ip_Info['city']
        region = ip_Info['region']
        country = ip_Info['country']

        print(f'You are at {city} city of {country}, region: {region}')

        self.talk(f'You are at {city} city of {country}, region: {region}')

    def scrape_wikipedia_using_google(self, query):
        query = query.replace(' ', '+')
        query = query.replace(self.name, '').strip()

        url = f"https://google.com/search?q={query}"
        self.google_searh_url = url

        html = requests.get(url).text

        soup = BeautifulSoup(html, 'lxml')

        result = soup.find_all('a')

        try:
            all_link = []

            for links in result:
                link = links['href']

                if 'https://en.wikipedia.org/wiki/' in link:
                    link = link.replace('/url?q=', '')

                    all_link.append(link)

            strLink = str(all_link[0])
            idx = strLink.index('&')
            strLink = strLink[:idx]

            wiki_topic = strLink[30:idx]

            info = wikipedia.summary(wiki_topic, 2)

            print(info)
            self.talk(info)

            print("Do you want to read more about this topic?")
            self.talk("Do you want to read more about this topic?")

            read_more = self.Listen()
            if 'yes' in read_more:
                print("ok! just wait a sec.")
                self.talk("ok! just wait a second.")
                t = Thread(target=os.system, args=(f"explorer {strLink}",))
                t.start()
            else:
                print("ok!")
                self.talk("o... ok! not a problem.")
        except wikipedia.exceptions.DisambiguationError:
            print(f"failed to get info!")
            self.talk("failed to get info!")

        except wikipedia.exceptions.PageError:
            print("due to some issues you have to find it yourself")
            self.talk("due to some issues you have to find yourself")
            t = Thread(target=webbrowser.open, args=(self.google_searh_url,))
            t.start()

        except IndexError:
            print("due to some issues you have to find it yourself")
            self.talk("due to some issues you have to find yourself")
            t = Thread(target=webbrowser.open, args=(self.google_searh_url,))
            t.start()

    def how_to(self, question):
        question = question.replace(self.name, '').strip()
        ans = search_wikihow(question, max_results=1)
        ans = ans[0].print()
        print(ans)

        self.talk("result is displayed on your screen.")

    def deactivate_ownself(self):
        print("deactivating... ownself")
        self.talk("deactivating... ownself")
        sys.exit()

    def go_to_sleep(self):
        def listen():
            r = sr.Recognizer()
            query = ""
            try:
                with sr.Microphone() as source:
                    r.pause_threshold = 2
                    print('sleeping...')
                    audio = r.listen(source, timeout=2, phrase_time_limit=7)
                    query = r.recognize_google(audio, language='en-in')
            except sr.RequestError:
                print("[!] No internet connection.\n[!] Please try again later.")
            except sr.UnknownValueError:
                print("[!] failed to recognize")
            finally:
                return query.lower()

        while True:
            watcher = listen()
            print(f'say "hey {self.name}" to wake me up')
            print(watcher)
            if self.name in watcher and 'hey' in watcher:
                break
