import matplotlib.pyplot as plt
import networkx as nx
import speech_recognition as sr
import pyttsx3


# graph object
g = nx.Graph()
r = sr.Recognizer()
r = sr.Recognizer()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# graph nodes
g.add_nodes_from(['MA101', 'MA102', 'MA103', 'MA104', 'MA105', 'MA106', 'MA107',
                 'MA108', 'MA109', 'MA110', 'MA111', 'MA112', 'MA113', 'MA114', 'MA115'])

# labels
g.add_edge('MA101', 'MA102', weight=3.04)
g.add_edge('MA102', 'MA103', weight=16.80)
g.add_edge('MA103', 'MA104', weight=6.72)
g.add_edge('MA104', 'MA105', weight=3.36)
g.add_edge('MA105', 'MA106', weight=15.58)
g.add_edge('MA106', 'MA107', weight=4.48)
g.add_edge('MA107', 'MA108', weight=0.65)
g.add_edge('MA108', 'MA109', weight=10.08)
g.add_edge('MA109', 'MA110', weight=3.36)
g.add_edge('MA110', 'MA111', weight=2.7)
g.add_edge('MA111', 'MA112', weight=6.16)
g.add_edge('MA112', 'MA113', weight=16.8)
g.add_edge('MA113', 'MA114', weight=4)
g.add_edge('MA114', 'MA115', weight=3.23)
g.add_edge('MA115', 'MA101', weight=60.55)
# g.add_edge('MA105','g', weight=12)
# g.add_edge('MA115','MA111', weight=2)
# g.add_edge('MA111','g', weight=3)


def speak(audiovoice):
    # engine.say('Hello Dear')
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()


def locate():
    source = ""
    destination = ""
    ans = "no"
    while (True):

        while(ans == "no"):
            speak('Say source location')
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.5)
                audio2 = r.listen(source2)
                source = r.recognize_google(audio2)
                source = "MA"+source

                print("Did you say "+source+" ?")
                audio2 = r.listen(source2)
                ans = r.recognize_google(audio2)
                ans = ans.lower()

        ans = "no"

        while(ans == "no"):
            speak("Say destination location")
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.5)
                audio2 = r.listen(source2)
                destination = r.recognize_google(audio2)
                destination = "MA"+destination
                print("Did you say "+destination+" ?")
                audio2 = r.listen(source2)
                ans = r.recognize_google(audio2)
                ans = ans.lower()

            # if(ch=='y'):
            # location = MyText

            # pos = nx.spring_layout(g)

        print(source, destination)
        shortest_path = nx.algorithms.single_source_dijkstra(
            g, source, destination)
        print(shortest_path)
        dist = round(shortest_path[0])
        

        paths = shortest_path[1]
        msg = "From "+paths[0]+" you need to go to "
        paths.pop(0)

        for p in paths:
            msg = msg + p + ","

        msg = msg[0:-1]

        msg = msg + " total distance will be {} meters.".format(dist)

        speak(msg)

        fixed_positions = {'MA101': (0, 8), 'MA102': (2, 8), 'MA103': (4, 8), 'MA104': (6, 8), 'MA105': (8, 8), 'MA106': (8, 6), 'MA107': (8, 5), 'MA108': (
            8, 4), 'MA109': (8, 3), 'MA110': (8, 2), 'MA111': (8, 0), 'MA112': (6, 0), 'MA113': (4, 0), 'MA114': (2, 0), 'MA115': (0, 0)}  # dict with two of the positions set

        edge_labs = dict([((u, v), d['weight'])
                          for u, v, d in g.edges(data=True)])

        nx.draw_networkx(g, fixed_positions)
        nx.draw_networkx_edge_labels(
            g, fixed_positions, edge_labels=edge_labs)
        nx.draw_networkx_nodes(
            g, fixed_positions, node_color='lightblue')
        plt.title("Graph")
        # nx.draw_networkx(g.add_edge)
        plt.show()
        break


locate()
