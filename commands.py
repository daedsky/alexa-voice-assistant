import pyautogui
import requests
import pywhatkit
import json
import time as Time
import datetime
import wikipedia
from pytube import YouTube
import smtplib
import wolframalpha
import os
import random
import webbrowser
from main_setup import *


def wish():
    print(f"Hi I am {name}. How may I help you?")
    talk(f"Hi I am {name}. How may I help you?")


def say_random_quotes():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        'x-rapidapi-key': "02118c70d0mshf019f7d35ffbca1p124ad0jsnfca7236a85d6",
        'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    response = json.loads(response.text)
    quoter = response.get('originator')
    quoter = quoter.get('name')
    print('########################## QUOTE OF THE DAY ####################################')
    print(f"{response['content']}, {quoter}")
    print('################################################################################')
    talk(f"{response['content']}, {quoter}")


def will_you_be_my_gf():
    replies = ["I'm not sure about, may be you should give me some time",
               "Sorry! I have a boyfriend",
               "Maa chuda behen k lund"]
    reply = random.choice(replies)
    print(reply)
    talk(reply)


def play_random_music():
    path = 'C:\\dedsky\\mp3'
    songs = os.listdir(path)
    song = random.randint(0, len(songs))
    os.startfile(os.path.join(path, songs[song]))


def dont_listen():
    talk("for how much time you want to stop me from listening commands")
    a = int(takecommand())
    print('not listening...')
    Time.sleep(a)
    print('I am back to work')


def wolf_ram_commands(query):
    '''
    print('tell me what to do')
    talk('tell me what to do')
    command = takecommand()
    '''
    client = wolframalpha.Client("3Q3GG2-3WP234LVPG")
    query = query.replace(name, '')
    query = query.replace('tell', '')
    query = query.replace('me', '')
    query = query.strip()
    print(query)
    res = client.query(query)

    try:
        print(next(res.results).text)
        talk(next(res.results).text)
    except StopIteration:
        print("No results found")
        talk("No results found")


def shut_down_pc():
    print("Hold On a Sec ! Your system is on its way to shut down")
    talk("Hold On a Sec ! Your system is on its way to shut down")
    os.system("shutdown /s /t 1")


def restart_pc():
    print("Hold On a Sec ! Your system is on its way to restart")
    talk("Hold On a Sec ! Your system is on its way to restart")
    os.system("shutdown /r /t /1")


def locate_a_place_on_gmaps(command):
    command = command.replace("where is", "")
    command = command.replace(name, "")
    command = command.replace('locate', '')
    command = command.strip()
    print('locating... please wait!')
    talk('locating... please wait!')
    location = command
    print(f"locating {command} on google maps.")
    talk(f"locating {command} on google maps.")
    webbrowser.open(f"https://www.google.nl/maps/place/{location}")


def send_email():
    try:
        # only works if (less secure apps) option is enabled on g-mail id
        print('please enable less secure apps on your gmail-id then continue')
        talk('please enable less secure apps on your gmail-id then continue')
        talk('please enter your email address')
        user_id = pyautogui.prompt(title='e-mail sender',
                                   text='Enter your e-mail address')

        talk('please enter your password')
        password = pyautogui.password(title='e-mail sender',
                                      text='Enter your password')

        talk("please enter the reciever's e-mail address")
        to = pyautogui.prompt(title='e-mail sender',
                              text='Enter the recievers e-mail address')

        print('what should I say')
        talk('what should I say')
        content = takecommand()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user_id, password)
        server.sendmail(from_addr=user_id, to_addrs=to, msg=content)
        server.close()

        print('e-mail has been sent')
        talk('e-mail has beeen sent')

    except Exception as e:
        print(e)
    # print('failed to send e-mail')
    # talk('failed to send e-mail')


def play_music(command):
    command = command.replace(name, '')
    command = command.strip()

    song = command.replace('play', '').strip()
    print(f"playing {song}")
    talk(f"playing {song}")
    pywhatkit.playonyt(song)
    print('please wait this can take a while')
    talk('please wait this can take a while')


def Search_on_wikipedia_():
    print('What topic do you want to search on wikipedia?')
    talk('What topic do you want to search on wikipedia?')
    topic = takecommand()
    print(f'gathering info... {topic}')
    info = wikipedia.summary(topic, 2)
    print(f'according to wikipedia... {info}')
    talk(f'according to wikipedia... {info}')


def write(command):
    command = command.replace(name, '')
    command = command.replace('type', '')
    command = command.strip()

    print('Tell me the text to type')
    talk('Tell me the text to type')
    Speech = takecommand()
    while name and 'stop' not in Speech:
        print('typing...')
        if name and 'stop' in Speech:
            Speech = f'{name} stop'
            talk('Typing stopped')

        else:
            if 'press enter' in Speech:
                pyautogui.press('enter')
                Speech = Speech.replace('press enter', '')
                pyautogui.typewrite(Speech)
                Speech = takecommand()
            elif 'press space' in Speech:
                pyautogui.typewrite(' ')
                Speech = Speech.replace('press space', '')
                pyautogui.typewrite(Speech)
                Speech = takecommand()


def Tell_the_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(f'current time is {time}')
    engine.say(f'current time is {time}')
    engine.runAndWait()


def open_website(command):
    command = command.replace(name, '')
    command = command.replace('open', '')
    command = command.strip()
    print(f"opening... {command}")
    talk(f"opening... {command}")
    webbrowser.open(f"https://{command}")
    print('please wait few seconds to open')
    talk('please wait few seconds to open')


def search_something():
    print('What do you want to search?')
    talk('What do you want to search?')
    search_query = takecommand()
    print(f"searching... {search_query}")
    talk(f"searching {search_query}")

    pywhatkit.search(search_query)


def speak_what_I_say(command):
    command = command.replace(name, '')
    command = command.replace('say', '')
    command = command.replace('se', '')
    command = command.strip()
    print(command)
    talk(command)


def open_app(command):
    command = command.replace(name, '')
    command = command.strip()
    command = command.replace('open', '')
    command = command.strip()

    print(f'opening... {command}')
    talk(f'opening... {command}')

    search_location = pyautogui.locateOnScreen('resources/TypeToSearch.png')
    pyautogui.click(search_location)
    pyautogui.sleep(2)
    pyautogui.typewrite(command)

    pyautogui.sleep(2)
    open_location = pyautogui.locateOnScreen('resources/OpenButton.png')
    pyautogui.doubleClick(open_location)


def tell_my_ip():
    print('getting your ip. just a sec...')
    ip = requests.get("https://api64.ipify.org/")
    ip = ip.text
    print(f"Your public ip address is {ip}")
    talk(f"Your public ip address is {ip}")


def my_ip_info():
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

    talk(
        f'Your public ip address is {ip}, city is {city}, region is {region}, country is {country}, and timezone is {timezone}')


def I_am_bored():
    print('wait a sec...')
    activity = requests.get("https://www.boredapi.com/api/activity")
    activity = activity.text
    activity = json.loads(activity)
    print(activity['activity'])
    talk(activity['activity'])


def exit_the_program():
    print('ok! logging... out')
    talk('ok! logging out')
    talk('have a great time ahead')
    print('have a great time ahead')


def guess_gender():
    print('tell me the name of the person')
    talk('tell me the name of the person')

    person_name = takecommand()
    gender = requests.get(f"https://api.genderize.io/?name={person_name}")
    gender = gender.text

    gender = json.loads(gender)
    person_gender = gender['gender']
    person_name = gender['name']
    probability = gender['probability']

    print(f"The gender of {person_name} is {person_gender} with {probability * 100} % probability")
    talk(f"The gender of {person_name} is {person_gender} with {probability * 100} % probability")


def tell_a_joke():
    print('fetching jokes...')
    joke = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = joke.text

    joke = json.loads(joke)
    setup = joke['setup']
    punchline = joke['punchline']

    print(setup)
    talk(setup)

    Time.sleep(1.1)
    print(punchline)
    talk(punchline)


def video_download():
    print('what do want to download video or a audio?')
    talk('what do want to download video or a audio?')
    video_or_audio = takecommand()

    if video_or_audio.lower() == 'video':
        talk('please enter the video url')
        link = pyautogui.prompt(
            title='video url',
            text='enter the video url')

        talk('enter the path where to save the file or keep it default and just press ok')
        path = pyautogui.prompt(title='audio downloader',
                                text='''Enter the path of folder where to save file
                                        or keep this default and just press ok!''',
                                default='C:\\alexa downloads\\videos')

        streams = YouTube(url=link).streams.get_highest_resolution()

        if streams == None:
            print('Sorry! the video is not downloadable')
            talk('Sorry! the video is not downloadable')
        else:
            print('downloading...')
            talk('downloading...')
            YouTube(url=link).streams.get_highest_resolution().download(path)
            print('downloader completed!')
            talk('download completed')
            print(f"it is stored at {path}")
            talk(f"it is stored at {path}")

    elif video_or_audio.lower() == 'audio':
        talk('please enter the video url')
        link = pyautogui.prompt(
            title='video url',
            text='enter the video url')

        talk('enter the path where to save the file or keep it default and just press ok')
        path = pyautogui.prompt(title='audio downloader',
                                text='''Enter the path of folder where to save file
                                        or keep this default and just press ok!''',
                                default='C:\\alexa downloads\\audios')

        streams = YouTube(url=link).streams.get_audio_only()

        if streams == None:
            print('Sorry! the video is not downloadable')
            talk('Sorry! the video is not downloadable')
        else:
            print('downloading...')
            talk('downloading...')
            YouTube(url=link).streams.get_audio_only().download(path)
            print('downloader completed!')
            talk('download completed')
            print(f"it is stored at {path}")
            talk(f"it is stored at {path}")


def where_am_i():
    print('getting your location...')
    ip = requests.get("https://api64.ipify.org/")
    ip = ip.text

    ip_info = requests.get(f"https://ipinfo.io/{ip}/geo")

    ip_Info = json.loads(ip_info.text)

    city = ip_Info['city']
    region = ip_Info['region']
    country = ip_Info['country']
    timezone = ip_Info['timezone']

    print(f'You are at {city} city of {country}, region: {region}')

    talk(f'You are at {city} city of {country}, region: {region}')
