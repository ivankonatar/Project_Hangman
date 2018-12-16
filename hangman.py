# importing necessary modules
from tkinter import *
import csv
import random
import sys
import os

# self restart function
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# reading a ,csv file in Python
spamReader = csv.reader(open('BazaRijeci.csv', 'r', encoding="utf8"))
data = sum([i for i in spamReader],[])

# selecting a random word from a .csv file
rijec = random.choice(data)

# create the GUI window
top2 = Tk()
top2.geometry("500x500")
top2.title("HANGMAN")

# changing the background color of the window
top2.configure(background='white')

# self close function
def kill():
    top2.destroy()

# Creating a button to start the function "kill"
killbutton = Button(top2, text="ZATVORI  IGRU", command=kill, background='red')
killbutton.pack()
killbutton.place(x=380, y=440)


# empty string to add hit letters
guess_word = []

# converting upper case letters into lower in random word
secretWord = rijec.lower()

# length of secret word
length_word = len(secretWord)

# printing "-" in places where there is an unknown letter
for character in secretWord:
    guess_word.append("-")

# letters that can be in a secret word
abeceda = ("A a B b C c Č č Ć ć D d Dž dž Đ đ E e F f G g H h I i J j K k L l Lj lj M m N n Nj nj O o P p R r S s Š š T t U u V v Z z Ž ž")

# empty string for storing used letters
letter_storage = []

# initial appearance of the gallows
w2 = Label(top2, text="     _________________ ", background='white', fg="red")
w2.pack()
w2.place(x=80, y=100)
w3 = Label(top2, text="     |                           |", background='white', fg="red")
w3.pack()
w3.place(x=80, y=117)
w4 = Label(top2, text="     |                           |", background='white', fg="red")
w4.pack()
w4.place(x=80, y=134)
w5 = Label(top2, text="     |                          ", background='white', fg="red")
w5.pack()
w5.place(x=80, y=151)
w6 = Label(top2, text="     |                        ", background='white', fg="red")
w6.pack()
w6.place(x=80, y=168)
w7 = Label(top2, text="     |                          ", background='white', fg="red")
w7.pack()
w7.place(x=80, y=185)
w8 = Label(top2, text="     |                        ", background='white', fg="red")
w8.pack()
w8.place(x=80, y=202)
w9 = Label(top2, text="     |                            ", background='white', fg="red")
w9.pack()
w9.place(x=80, y=219)
w10 = Label(top2, text="     |                            ", background='white', fg="red")
w10.pack()
w10.place(x=80, y=236)
w11 = Label(top2, text=" ____|____                        ", background='white', fg="red")
w11.pack()
w11.place(x=72, y=253)

# creating text box in which the gamer writes a letter
T2 = Text(top2, height=1, width=4)
T2.pack()
T2.place(x=120, y=350)

# text in label in which the current state of the secret word is entered
teskt_iz_labele = StringVar()
teskt_iz_labele.set(guess_word)

# creating label in which printing current state of the secret word
W20 = Label(top2, textvariable=teskt_iz_labele, background='white', fg="blue", font=("Helvetica", 20))
W20.pack()
W20.place(x=72, y=300)

# mistake counter, at the beginning set on zero
guess_taken = 0

# printing funcion
def stampanje(event=None):

    # taking letters from the text box
    provjera=T2.get("1.0", END)
    global guess_taken

    # delete letters in the text box after pressing the button
    T2.delete('1.0', END)

    # checking if the letter is in the offered alphabet
    # if not, printing message
    if not provjera.strip().lower()  in abeceda:
        W21 = Label(top2, text='                                                            ', background='white', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
        W21 = Label(top2, text='Niste unijeli slovo iz abecede A-Ž', background='white', fg="red")
        W21.pack()
        W21.place(x=72, y=400)

    # checking if the letter has already been entered
    # if yes, printing message
    elif provjera.strip().lower() in letter_storage:
        W21 = Label(top2, text='                                                          ', background='white', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
        W21 = Label(top2, text='Vec ste unijeli to slovo', background='white', fg="red")
        W21.pack()
        W21.place(x=72, y=400)

    # else cases
    else:
        W21 = Label(top2, text='                                                         ', background='white', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
        letter_storage.append(provjera.strip().lower())

        # checking if the letter is in the secret word
        # if yes, doing next check
        if provjera.strip().lower() in secretWord:

            for x in range(0, length_word):

                # add a letter in the label
                if secretWord[x] == provjera.strip().lower():
                    guess_word[x] = provjera.strip().upper()
                    stara_vrijednost = teskt_iz_labele.get()
                    teskt_iz_labele.set(guess_word)

                # if there is no '-' in the label, the game is over
                if not '-' in guess_word:

                    # the first window closes
                    top2.destroy()

                    #  a new window opens with a message and secret word, button for close the game, and button for restart the game
                    top3 = Tk()
                    top3.geometry("330x300")
                    top3.title("ZAVRSENA IGRA")
                    w2 = Label(top3, text="ČESTITAMO ! POBIJEDILI STE \n \n Tajna riječ je bila: " +secretWord.upper())
                    w2.pack()
                    w2.place(x=80, y=100)

                    def kill():
                        top3.destroy()

                    killbutton = Button(top3, text="ZATVORI IGRU", command=kill)
                    killbutton.pack()
                    killbutton.place(x=120, y=200)

                    killbutton3 = Button(top3, text="PONOVO POKRENI", command=restart_program)
                    killbutton3.pack()
                    killbutton3.place(x=107, y=250)


        # checking if the letter is in the secret word
        # if not, doing next steps
        else:

            # printing message in label
            W21 = Label(top2, text='                                                    ', background='white', fg="red")
            W21.pack()
            W21.place(x=72, y=400)
            W21 = Label(top2, text='Slovo se ne nalazi u tajnoj rijeci', background='white', fg="red")
            W21.pack()
            W21.place(x=72, y=400)

            # add 1 in mistake counter
            guess_taken +=1

            # cases for plotting a human body depending on the number of mistakes
            if guess_taken == 1:
                n = 'O     '
            elif guess_taken == 2:
                n = 'O/     '
            elif guess_taken == 3:
                n = 'O/\    '
            elif guess_taken == 4:
                n = 'O/\|   '
            elif guess_taken == 5:
                n = 'O/\|/  '
            elif guess_taken == 6:
                n = 'O/\|/\ '

            w2 = Label(top2, text="     _________________ ", background='white', fg="red")
            w2.pack()
            w2.place(x=80, y=100)
            w3 = Label(top2, text="     |                           |", background='white', fg="red")
            w3.pack()
            w3.place(x=80, y=117)
            w4 = Label(top2, text="     |                           |", background='white', fg="red")
            w4.pack()
            w4.place(x=80, y=134)
            w5 = Label(top2, text="     |                          {0}".format(n[0]), background='white', fg="red")
            w5.pack()
            w5.place(x=80, y=151)
            w6 = Label(top2, text="     |                        {0}    {1}".format(n[1], n[2]), background='white', fg="red")
            w6.pack()
            w6.place(x=80, y=168)
            w7 = Label(top2, text="     |                           {0}".format(n[3]), background='white', fg="red")
            w7.pack()
            w7.place(x=80, y=185)
            w8 = Label(top2, text="     |                        {0}    {1}".format(n[4], n[5]), background='white', fg="red")
            w8.pack()
            w8.place(x=80, y=202)
            w9 = Label(top2, text="     |                            ", background='white', fg="red")
            w9.pack()
            w9.place(x=80, y=219)
            w10 = Label(top2, text="     |                            ", background='white', fg="red")
            w10.pack()
            w10.place(x=80, y=236)
            w11 = Label(top2, text=" ____|____                        ", background='white', fg="red")
            w11.pack()
            w11.place(x=72, y=253)

        # if a player makes six mistakes
        if guess_taken == 6:

            # the first window closes
            top2.destroy()

            #  a new window opens with a message and secret word, button for close the game, and button for restart the game
            top3 = Tk()
            top3.geometry("330x300")
            top3.title("ZAVRSENA IGRA")
            w2 = Label(top3, text="Žao nam je, izgubili ste! \n \n Tajna riječ je bila: " + secretWord.upper())
            w2.pack()
            w2.place(x=85, y=100)

            def kill():
                top3.destroy()

            killbutton = Button(top3, text="ZATVORI IGRU", command=kill)
            killbutton.pack()
            killbutton.place(x=120, y=200)

            killbutton3 = Button(top3, text="PONOVO POKRENI", command=restart_program)
            killbutton3.pack()
            killbutton3.place(x=105, y=250)


# binding the enter key to a function 'stampanje'
top2.bind('<Return>', stampanje)

# creating a button for confirming the entered letters
B2 = Button(top2, text="Potvrdi slovo", command = stampanje )
B2.place(x=200, y=345)


top2.mainloop()

