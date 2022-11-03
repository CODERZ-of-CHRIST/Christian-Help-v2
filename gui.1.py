from tkinter import messagebox
from win32com.client import Dispatch
import random
speak =  Dispatch("SAPI.SpVoice").Speak


         
def meditation():
        meditation = (
            "Sometimes the hardest part of the day is deciding to get out of bed. From the mundane, What am I going to have for breakfast? — to the major, Is this really where I want to be in my career? every day is filled with one stressful decision after another. Start the day by choosing to lean on God’s wisdom for all the difficult questions you will face.",
            "As you start your day, you may be wondering how you're going to get through it. The morning news show on TV lists yet another threat to your safety. And there’s a chance you might run into that one person you’ve been avoiding. Or maybe you just have an oppressive feeling of anxiety with no discernable cause but very noticeable effects. Taking some time to stop and consider what God has to say about anxiety can help bring you back to a place of peace.",
            "Just as you finally get moving to tackle the day, the slow-downs start. First, waiting in line at the café for a cup of coffee. Then traffic once again makes your commute an eternity. Instead of letting your impatience and anger take control, use the time to reflect and see if God is using the wait as an opportunity to speak to you and help remove your stress.",
            "Another day, another to-do list. Whether you're a top account executive or a stay-at-home parent, a best-selling artist or a mom-and-pop store owner, you have an important role to play in the world. It’s easy to lose sight of this unique purpose that you have been given in the thick of the emails and phone calls and meetings. This meditation will help you get back on track with your calling to keep you motivated as you work.",
            "Bill from the office next door lost the quarterly report. You get the fourth call this week from your child’s school asking you to meet your child at the principal’s office. Your spouse’s boss once again passes them over for a promotion. Some people seem to enjoy making our life challenging, yet as Christians, we are called to love them. Talk about needing some peace?! When you find yourself getting angry at them, take a moment to remember that God still loves them and you can too.",
            )
        choice = random.randint(0, 5)
        speak((meditation[choice]))
        import time
        time.sleep(3)
        output.insert(0.0, (meditation[choice]))


def saint():
        saint = (
                "St. Francis of Assisi",
                "St. Catherine of Siena",
                "St. Joseph",
                "St. Valentine",
                "St. Christopher",
                "St. Patrick",
                )
        choice = random.randint(0, 5)
        saint = (saint[choice])
        speak("The saint of the day is "+saint)
        messagebox.showinfo("CHRISTIAN HELP: BY IFEANYI", "The Saint of the day is "+saint)
        

def eucharist():
        webbrowser.open("http://www.miracolieucaristici.org/en/Liste/list.html")

def read():
        output.delete(0.0, END)
        message = "This function is coming soon"
        output.insert(0.0, message)

def carlo():
        output.delete(0.0, END)
        webbrowser.open("https://en.wikipedia.org/wiki/Carlo_Acutis")

def talk():
        speak(output)
from tkinter import *
from tkinter.tix import COLUMN
import webbrowser
from pygame import *
mixer.init()
def euch():
        webbrowser.open("http://www.miracolieucaristici.org/en/Liste/list.html")
#Load audio file
mixer.music.load('sounds\intro.mp3')


#Set preferred volume
mixer.music.set_volume(0.2)

#Play the music
mixer.music.play()

def github():
   import webbrowser
   webbrowser.open("www.github.com/coderifeanyi")

def message():
        output.delete(0.0, END)
        message = "Hello, I am Ifeanyi: I am trying my best to follow in the footsteps of St. Carlo Acutis: Please support the mission by donating to Churches: Thank you, God loves you"
        output.insert(0.0, message)
        
def close():
        exit()
import random
window = Tk()
photo = PhotoImage(file = "pics\logo.ico")
window.iconphoto(False, photo)

#click
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        response = dictionary[entered_text]
    except:
        response = "Sorry this function is not available\nTroubleShooting: Make sure to use the exact case used in the item your typing."
    output.insert(END, response)
    
            
window.title("CHRISTIAN HELP: BY IFEANYI ONUAMA")
window.geometry("650x600")
C = Canvas(window, bg="black", height=250, width=300)
filename = PhotoImage(file = "pics\dovy.gif")
background_label = Label(window, image=filename)
background_label.place(x=-20, y=100, relwidth=1,relheight=1)
  
window.configure(background="white")
#'label
Label (window, text="|About|   --  |Eucharist|   --   |Songs|   --   |Bible|   --    |Exit|", bg="white", fg="black", font="none 14 bold") .grid(row=1, column=0, sticky=W)
#textbox entry
textentry = Entry(window, width=82, bg="grey")
textentry.grid(row=2, column=0, sticky=W)

#submit
Button(window, text="ENTER", width=15, command=click) .grid(row=2, column=1, sticky=W)
#button2
Button(window, text="Author Message", width=15, command=message) .grid(row=10, column=0, sticky=W)
Button(window, text="Meditation", width=15, command=meditation) .grid(row=20, column=0, sticky=W)
Button(window, text="Close", width=15, command=close) .grid(row=10, column=1, sticky=W)
Button(window, text="Saint of the Day", width=15, command=saint) .grid(row=20, column=1, sticky=W)

#SUBSCRIPTIONS
Button(window, text="Follow me on Github", width=15, command=github) .grid(row=0, column=0, sticky=W)
#carlo
Button(window, text="About St. Carlo Acutis", width=20, command=carlo) .grid(row=0, column=1, sticky=W)



#label
Label (window, text="(Response will come here -->)", bg="white") .grid(row=4, column=0, sticky=W)
Label (window, text="© Copyright 2022 Ifeanyi Onuama. All rights reserved", bg="white") .grid(row=7, column=0, sticky=W)
#output
output = Text(window, width=75, height=6, wrap=WORD, background="grey")
output.grid(row=5, column=0, columnspan=2, sticky=W)



   
dictionary = {
        'Bible': 'The Bible uses meditation as deep contemplation, a turning over and around in the mind to gain greater understanding and be changed by God"s truth. True, meditation is a tool of learning that can be abused. Yet, instead of avoiding it, we should use it with care, biblical understanding, and respect.', 'Songs': 'Follow this link to here the full HillSong playlist\nhttps://www.youtube.com/watch?v=qCZAynQU_-8', 'About': 'This application was created by me, Ifeanyi Onuama, I got inspiration from St. Carlo Acutis, I love him and I aim to be like him by the Grace of God:\nHe got all the mysteries of the Eucharist and put the all together on one website, I hope to be like him.', 'Author Message': 'Hello, I am Ifeanyi: I am trying my best to follow in the footsteps of St. Carlo Acutis: Please support the mission by donating to Churches: Thank you, God loves you', 'Eucharist': 'The Eucharist is at the heart of Christian worship. It is celebrated by Christians around the world as a memorial of the death and resurrection of Jesus, in response to his words at the final meal he shared with his disciples, Do this in remembrance of me.', 'Exit': 'Click the close button below to Exit'
}



window.mainloop()
        
