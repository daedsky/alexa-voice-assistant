import alexa_functions

name = "alexa"
edith = alexa_functions.AlexaCommands(name=name)

while True:
    query = edith.Listen()
    print(query)
    if all((name in query, 'open' in query, '.' in query)):
        edith.open_site(query)

    elif name in query and 'play' in query and 'music' in query:
        edith.play_random_local_music()

    elif name in query and 'play' in query:
        edith.play_yt_video(query)

    elif name in query and 'time' in query:
        edith.tell_current_time()

    elif name in query and 'shut down' in query and any(('pc' in query, 'computer' in query)):
        edith.shut_down_pc()

    elif name in query and any(('restart' in query, 'reboot' in query)) and any(('pc' in query, 'computer' in query)):
        edith.restart_pc()

    elif all((name in query, 'locate' in query)):
        edith.locate_a_place_on_gmaps(query)

    elif all((name in query, 'activate' in query, 'typing' in query, 'mod' in query)):
        edith.acitvate_typing_mode()

    elif all((name in query, 'search' in query)):
        edith.google_search(query)

    elif all((name in query, 'open' in query)):
        edith.open_app(query)

    elif all((name in query, 'my' in query, 'ip' in query, 'info' in query)):
        edith.tell_my_ip_info()

    elif all((name in query, 'my' in query, 'ip' in query)):
        edith.tell_my_ip()

    elif all((name in query, 'bore' in query)):
        edith.i_am_bored()

    elif all((name in query, 'gender' in query)) and any(('guess' in query, 'tell' in query)):
        edith.guess_gender()

    elif all((name in query, 'joke' in query)):
        edith.tell_a_joke()

    elif name in query and any(('where am i' in query, 'my location' in query, 'locate me' in query)):
        edith.where_am_i()

    elif name in query and any(('say' in query, 'se' in query)):
        edith.repeat_me(query)

    elif name in query and any(('deactivate' in query, 'log out' in query, 'terminate' in query,
                                'quit' in query, 'exit' in query)):
        edith.deactivate_ownself()

    elif name in query and 'sleep' in query:
        edith.go_to_sleep()

    elif name in query and 'how to' in query:
        edith.how_to(query)

    elif name in query and (len(query) >= 15):
        edith.scrape_wikipedia_using_google(query)
