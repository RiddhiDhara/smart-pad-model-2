#>>>>>>>>>>>>>>>importing the package  
import language_tool_python 
import re
#>>>>>>>>>>>>>>>DPI SETTING
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#>>>>>>>>>>>>>>>DICTIONARY
from PyDictionary import PyDictionary
dict = PyDictionary()
#>>>>>>>>>>>>>>>GOOGLE TRANSLATOR
from googletrans import Translator
#>>>>>>>>>>>>>>>SPEECH RECOGNITION
import speech_recognition as s_r
import os
# >>>>>>>>>>>>>>Pyaudio
import pyaudio
import threading
#>>>>>>>>>>>>>>>TKINTER
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox
# ==========================global variables 
count_int = 0
index_num = None
# ======================================================-> defining function

# ------------------>create window 1
def create_text_window1(window, row, column):
    
    text_frame1 = tk.Frame(window, bg="light gray", bd=1)
    text_frame1.grid(row=row, column=column, sticky="nsew")
    
    text_widget1 = tk.Text(text_frame1, bg="dark gray", font=('Courier New', 11, 'bold'), wrap=tk.WORD, undo=True)
    text_widget1.pack(expand=True, fill="both")
    
    scrollbar = tk.Scrollbar(text_frame1, command=text_widget1.yview ,relief=tk.RAISED , bg="dark gray")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    text_widget1.config(yscrollcommand=scrollbar.set)
    
    return text_widget1
# ------------------>create window 2
def create_text_window2(window, row, column):

    text_frame2 = tk.Frame(window, bg="light gray", bd=1)
    text_frame2.grid(row=row, column=column, sticky="nsew")
    
    text_widget2 = tk.Text(text_frame2, bg="dark gray", font=('Courier New', 11, 'bold'), wrap=tk.WORD)
    text_widget2.pack(expand=True, fill="both")
    
    scrollbar = tk.Scrollbar(text_frame2, command=text_widget2.yview ,relief=tk.RAISED , bg="dark gray")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    text_widget2.config(yscrollcommand=scrollbar.set)
    
    return text_widget2

# ------------------->open file
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    txt1_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt1_edit.insert(tk.END, text)
    window.title(f"SMART-PAD [OPEN WINDOW] :-) - {filepath}")
# ------------------save file
def save_file():
    filepath = asksaveasfilename(
        defaultextension= "txt",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
            return
    with open(filepath, "w") as output_file:
        text1 = txt1_edit.get(1.0, tk.END)
        text2 = txt1_edit.get(1.0, tk.END)
        output_file.write(text1)
    window.title(f"SMART-PAD [SAVE WINDOW] :-) - {filepath}")
# ------------------my info
def info_About_me():
   tkinter.messagebox.showinfo("INTRODUCTION :-]", "NAME : RIDDHI DHARA \nCOLLEGE : JISCE \nPROJECT TOPIC : PYTHON PROGRAMMING \nPROJECT NAME : SMART-PAD \nUNIVERSITY ROLL : 123211003113 \nCOLLEGE-ID : JIS/2021/0929 \n")
# ------------------error info 
def error_info():
   tkinter.messagebox.ERROR("Enter Valid number!")
#-------------------translate information 
def info_translate():
   tkinter.messagebox.showinfo("LANGUAGE TRANSLATION :->", "OPTION AVAILABLE:========>>> \n1) ENGLISH :- translate to ENGLISH \n2) BENGALI :- translate to BENGALI \n3) HINDI :- translate to HINDI \n")
# ------------------undo
def undo():
    txt1_edit.edit_undo()
# ------------------redo
def redo():
    txt1_edit.edit_redo()
#-------------------clear screen 1
def clear_screen_1():
    txt1_edit.delete("1.0", "end")
#-------------------clear screen 2
def clear_screen_2():
    txt2_edit.delete("1.0", "end")
    
# ------------------popup
def create_popup():
    def get_user_input():
        nonlocal user_number
        try:
            user_number = int(entry.get())
            popup.destroy()  # Close the popup window
        except ValueError:
            print("Please enter a valid number.")

    def validate_input(new_value):
        if new_value == "" or new_value.isdigit() or (new_value.startswith('-') and new_value[1:].isdigit()):
            return True
        else:
            return False

    user_number = None  # Initialize user_number to None

    popup = tk.Toplevel(window)
    popup.title("Index-Popup")
    popup.geometry("300x80")

    validate_cmd = popup.register(validate_input)

    entry = tk.Entry(popup, validate="key", validatecommand=(validate_cmd, '%P'))
    entry.pack()

    submit_button = tk.Button(popup, text="Submit", command=get_user_input)
    submit_button.pack()

    popup.wait_window(popup)  # Wait for the popup window to close
    return user_number

# ------------------voice input // some changes required
def voice_input():
    def recognize_speech():
        r = s_r.Recognizer()
        bluetooth_device_index = create_popup()
        my_mic = s_r.Microphone(device_index=bluetooth_device_index)
        with my_mic as source:
            # amb
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source , timeout=3)
                print(audio)
            except:
                txt2_edit.delete("1.0", "end")
                txt2_edit.insert(tk.END, "Sorry! TIME OUT :-(")
                
        recorded_text = (r.recognize_google(audio), "\n")
        txt1_edit.insert(tk.END, recorded_text)
    threading.Thread(target=recognize_speech).start()    
        
#------------------ translate text
def translate_to(text):
        lang_input = text
        lang_translate(lang_input)
#----------------- language select
def lang_translate(take_language):
        txt2_edit.delete("1.0", "end")
        sentence = txt1_edit.get(1.0, tk.END)
        translator = Translator()
        translation = translator.translate(sentence, dest=take_language)
        if translation.src == translation.dest:
            txt2_edit.insert(tk.END, "SOURCE language & TRANSLATED language is SAME!!!  :-|")
            txt2_edit.insert(tk.END, "\n")
        else:
            txt2_edit.insert(tk.END, translation)
            txt2_edit.insert(tk.END, "\n")
#------------------ meaning of the word
def find_meaning():
        txt2_edit.delete("1.0", "end")
        selection = txt1_edit.get(tk.SEL_FIRST, tk.SEL_LAST)
        meaning = dict.meaning(selection)
        txt2_edit.insert(tk.END, selection + ":-------------------------------" + "\n")
        try:
            txt2_edit.insert(tk.END, meaning)
            txt2_edit.insert(tk.END, "\n")
        except:
            txt2_edit.insert(tk.END, "Sorry! DEFINITION not found :-(")
# -----------------correction grammer 
def correction():
        my_tool = language_tool_python.LanguageTool('en-US')  
        my_text = txt1_edit.get(1.0, tk.END) # given text    
        my_matches = my_tool.check(my_text)  # getting the matches
        myMistakes = []  # defining some variables 
        myCorrections = []  
        startPositions = []  
        endPositions = []  
        for rules in my_matches :                                          # using the for-loop  
            if len(rules.replacements) > 0 :
                startPositions.append(rules.offset)  
                endPositions.append(rules.errorLength + rules.offset)  
                myMistakes.append(my_text[rules.offset : rules.errorLength + rules.offset])  
                myCorrections.append(rules.replacements[0])  
        my_NewText = list(my_text)   # creating new object  
        for n in range(len(startPositions)):  # rewriting the correct passage  
            for i in range(len(my_text)):  
                my_NewText[startPositions[n]] = myCorrections[n]  
                if (i > startPositions[n] and i < endPositions[n]):  
                    my_NewText[i] = ""  
        my_NewText = "".join(my_NewText)
        try:   
            txt1_edit.delete("1.0", "end")
            txt1_edit.insert(tk.END, my_NewText)
            txt2_edit.delete("1.0", "end")
            txt2_edit.insert(tk.END, "Disclaimer: [Correction] may not give the Appropriate result" + "\n-----------------------------------------------------------------\n")
            txt2_edit.insert(tk.END, "CORRECTION:-" + "\n")
            txt2_edit.insert(tk.END, list(zip(myMistakes, myCorrections)))
        except:
            txt2_edit.insert(tk.END, "NO Correction needed!!!")
# ----------------- mic index in pc
def MIC_INDEX_Window():
    newWindow = Toplevel(window)
    newWindow.title("DEVICE-INDEX :-] ")
    newWindow.rowconfigure(0, minsize=1000, weight=1)
    newWindow.columnconfigure(1, minsize=1000, weight=1)
    v=Scrollbar(newWindow, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    txt=Text(newWindow, font=("Georgia, 10"), yscrollcommand=v.set)
    # ...............................................
    r = s_r.Microphone.list_microphone_names()
    j = 0
    for i in r:
        a = r[j]
        txt.insert(END, str(j) + "." + " " + a + "\n")
        j = j+1
    # ...............................................
    v.config(command=txt.yview)
    txt.pack()

# ======================================================-> window structure
window = tk.Tk()
window.title("<<SMART-PAD>>:-) ")
window.configure(bg="lightgray",relief='sunken')
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
# ======================================================-> sidebar
sidebar = tk.Frame(window, bg="lightgray", width=100)
sidebar.grid(row=0, column=0, sticky="ns")
# ======================================================-> textbox structure
txt1_edit = create_text_window1(window, 0, 1)
txt2_edit = create_text_window1(window, 0, 2)
# --------------------------------
btn_AboutMe = tk.Button(sidebar, text="About Creator", bg='dark gray', command=info_About_me)

btn_open = tk.Button(sidebar, text="Open", bg='light gray', command=open_file)
btn_save = tk.Button(sidebar, text="Save_As", bg='light gray', command=save_file)
btn_mic = tk.Button(sidebar, text="Mic-Index", bg='light gray', command=MIC_INDEX_Window)
btn_voice_input = tk.Button(sidebar, text="Voice Text", bg='light gray', command=voice_input)
btn_definition = tk.Button(sidebar, text="Definition", bg='light gray', command=find_meaning)
btn_correction = tk.Button(sidebar, text="Correction", bg='light gray', command=correction)

btn_clear_1 = tk.Button(sidebar, text="Clear-1", bg='sky blue', command=clear_screen_1)

btn_translate = tk.Button(sidebar, text="Translate", bg='dark gray', command=info_translate)
btn_ENGLISH = tk.Button(sidebar, text="ENGLISH", bg='light gray', command=lambda:translate_to("en"))
btn_BENGALI = tk.Button(sidebar, text="BENGALI", bg='light gray', command=lambda:translate_to("bn"))
btn_HINDI = tk.Button(sidebar, text="HINDI", bg='light gray', command=lambda:translate_to("hi"))

btn_clear_2 = tk.Button(sidebar, text="Clear-2", bg='sky blue', command=clear_screen_2)

btn_undo = tk.Button(sidebar,bg='blueviolet', text="<<Undo", command=undo)
btn_redo = tk.Button(sidebar,bg='blueviolet', text="Redo>>", command=redo)
# ======================================================-> button grid
btn_AboutMe.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_mic.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_voice_input.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_definition.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_correction.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_clear_1.grid(row=7, column=0, sticky='ew', padx=5, pady=5)
btn_translate.grid(row=8, column=0, sticky="ew", padx=5, pady=5)
btn_ENGLISH.grid(row=9, column=0, sticky="ew", padx=5, pady=5)
btn_BENGALI.grid(row=10, column=0, sticky="ew", padx=5, pady=5)
btn_HINDI.grid(row=11, column=0, sticky="ew", padx=5, pady=5)
btn_clear_2.grid(row=12, column=0, sticky='ew', padx=5, pady=5)
btn_undo.grid(row=13, column=0, sticky='ew', padx=5, pady=5)
btn_redo.grid(row=14, column=0, sticky='ew', padx=5, pady=5)
# ===============->binding window
window.bind("<Control-z>", lambda event: undo())
window.bind("<Shift-Control-Z>", lambda event: redo())
# ===============-> window grid
window.grid_columnconfigure(0, minsize=20)
window.grid_rowconfigure(0, minsize=20)
# ===============>window end
window.mainloop()
#-------------------------------END--------------------------------------------