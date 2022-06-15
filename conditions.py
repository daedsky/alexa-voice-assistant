from commands import *


def loop():
    while True:
        try:
            query = takecommand()
            print(f'you said: {query}')
            command = query

            if f'{name} open' in command and '.' in command:
                open_website(command)

            elif f'{name} play music' in command:
                play_random_music()

            elif f'{name} open' in command:
                open_app(command)

            elif f"{name} locate" in command:
                locate_a_place_on_gmaps(command)

            elif f'{name} play' in command:
                play_music(command)

            elif name in command and 'joke' in command:
                tell_a_joke()

            elif name in command and 'gender' in command:
                guess_gender()

            elif name in command and 'bored' in command:
                I_am_bored()

            elif name in command and 'wikipedia' in command:
                Search_on_wikipedia_()

            elif name in command and 'my' in command and 'ip' in command and 'info' in command:
                my_ip_info()

            elif name in command and 'my' in command and 'ip' in command:
                tell_my_ip()

            elif name in command and 'time' in command:
                Tell_the_time()

            elif name in command and 'type' in command:
                write(command)

            elif name in command and 'search' in command:
                search_something()

            elif name in command and 'download' in command:
                video_download()

            elif name in command and 'send' in command and 'email' in command:
                send_email()

            elif name in command and 'shut down' in command and 'computer' in command:
                shut_down_pc()

            elif name in command and 'restart' in command and 'computer' in command:
                restart_pc()

            elif name in command and any(["don't listen" in command, "stop listerning" in command]):
                dont_listen()


            elif any((f'{name} say' in command, f'{name} se' in command)):
                speak_what_I_say(command)

            elif name in command and any(('will you be my gf' in command,
                                          'will you be my girlfriend' in command,
                                          'will you be my girl friend' in command)):
                will_you_be_my_gf()

            elif name in command and "how are you" in command:
                talk("I'm fine, glad you me that")

            elif all((name in command, 'where' in command,
                      'am' in command, 'i' in command)):
                where_am_i()

            elif name in command and 'quote' in command:
                say_random_quotes()

            elif name in command and 'sleep' in command:
                print('ok! going to sleep.')
                talk('ok! going to sleep.')
                break

            elif name in command and 'tell' in command and 'me' in command:
                wolf_ram_commands(query=command)
        except:
            print("failed! to execute command.")
