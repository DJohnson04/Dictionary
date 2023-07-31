from tkinter import BooleanVar, ttk
import tkinter as tk
from dictionary import DictionaryAPI
import webbrowser

api = DictionaryAPI()
#api information
def search_word():
    word = entry.get()
    api = DictionaryAPI()
    response = api.get_response(word)
    #checks to make sure the word is valid
    if response:
        definition = api.get_definition(response)
        synonyms = api.get_synonyms(response)
        more_info = api.get_more_info(response)
        #configures the labels
        word_label.config(text ='Word: '+ word)
        definition_label.config(text="Definition: " + definition)
        synonyms_label.config(text="Synonyms: " + ", ".join(synonyms) if synonyms else "No synonyms found.")
        #adding clickable link
        def open_link(event,more_info):
            webbrowser.open_new_tab(more_info)
        if more_info:
            more_info_link = ", ".join(more_info)
            more_info_label = ttk.Label(master=window, text="More Info: " + more_info_link, font=deffont, wraplength=400, foreground="blue", cursor="hand2")
            more_info_label.grid(row=4, column=0, sticky="w")
            more_info_label.bind("<Button-1>", lambda event, urls=more_info: [open_link(event, url) for url in urls])

        #more_info_label.config(text="More Info: " + ", ".join(more_info)+ ' '.join(callback(more_info)) if more_info else "No additional info available.")
        #callback(more_info)
    else:
        definition_label.config(text="Word not found.")
        synonyms_label.config(text="")
        more_info_label.config(text="")

#starting gui application
font = 'Calibri 24'
deffont = 'Calibri 14'
#window
window = tk.Tk() 
window.title('Dictionary')
window.geometry('1000x500')

#title
title_label = ttk.Label(master=window, text='Dictionary', font=font)
title_label.grid(row=0, column=0, columnspan=3)

# input field
input_frame = ttk.Frame(master=window)

entry = ttk.Entry(master=input_frame) #search box
button = ttk.Button(master=input_frame, text='Search', command=search_word) #search button
entry.grid(row=0, column=0, padx=10)
button.grid(row=0, column=1)
input_frame.grid(row=1, column=0, columnspan=3, pady=20)

# Labels to display word info
word_label = ttk.Label(master=window, text='Word: ', font=deffont)
word_label.grid(row=1, column=0, sticky="w")  

definition_label = ttk.Label(master=window, text="Definition: ", font=deffont)
definition_label.grid(row=2, column=0, sticky="w")  

synonyms_label = ttk.Label(master=window, text="Synonyms: ", font=deffont)
synonyms_label.grid(row=3, column=0, sticky="w")  

more_info_label = ttk.Label(master=window, text="More Info: ", font=deffont)
more_info_label.grid(row=4, column=0, sticky="w")  

wraplength = 400
definition_label.config(wraplength=wraplength)
synonyms_label.config(wraplength=wraplength)
more_info_label.config(wraplength=wraplength)

#grid layout
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)

window.rowconfigure(0, weight=3)
window.rowconfigure(1, weight=3)
window.rowconfigure(2, weight=3)
window.rowconfigure(3, weight=3)
window.rowconfigure(4, weight=3)
window.rowconfigure(5, weight=3)

#run
window.mainloop()