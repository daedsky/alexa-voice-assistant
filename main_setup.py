import pyttsx3
import speech_recognition as sr

# girls: alexa, clara, siri, jiya, sara
# boys: eric, jarvis
name = 'alexa'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 170)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    query = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold = 2
            audio = r.listen(source, timeout=2, phrase_time_limit=10)

            print('recognizing...')
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
    except:
        print('failed! to recognize.')

    return query


def wake_me_up():
    r = sr.Recognizer()
    query = ''
    try:
        with sr.Microphone() as source:
            print('sleeping...')
            r.pause_threshold = 2
            audio = r.listen(source, timeout=2, phrase_time_limit=10)

            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
    except:
        print('failed! to recognize')

    return query
