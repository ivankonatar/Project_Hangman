
from tkinter import *
import csv
import random

spamReader = csv.reader(open('BazaRijeci.csv', 'r', encoding="utf8"))

data = sum([i for i in spamReader],[])
rijeci = random.choice(data)

top2 = Tk()
top2.geometry("500x500")
top2.title("HANGMAN")
top2.configure(background='yellow')

def kill():
    top2.destroy()

killbutton = Button(top2, text="ZATVORI  IGRU", command=kill, background='red')
killbutton.pack()
killbutton.place(x=380, y=440)

n = '       '


wordList=rijeci.lower().split(' ')
guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)

for character in secretWord:
    guess_word.append("-")

abeceda = ("A a B b C c Č č Ć ć D d Dž dž Đ đ E e F f G g H h I i J j K k L l Lj lj M m N n Nj nj O o P p R r S s Š š T t U u V v Z z Ž ž")
letter_storage = []


w2 = Label(top2, text="     _________________ ", background='yellow', fg="red")
w2.pack()
w2.place(x=80, y=100)
w3 = Label(top2, text="     |                           |", background='yellow', fg="red")
w3.pack()
w3.place(x=80, y=117)
w4 = Label(top2, text="     |                           |", background='yellow', fg="red")
w4.pack()
w4.place(x=80, y=134)
w5 = Label(top2, text="     |                          {0}".format(n[0]), background='yellow', fg="red")
w5.pack()
w5.place(x=80, y=151)
w6 = Label(top2, text="     |                        {0}    {1}".format(n[1], n[2]), background='yellow', fg="red")
w6.pack()
w6.place(x=80, y=168)
w7 = Label(top2, text="     |                           {0}".format(n[3]), background='yellow', fg="red")
w7.pack()
w7.place(x=80, y=185)
w8 = Label(top2, text="     |                        {0}    {1}".format(n[4], n[5]), background='yellow', fg="red")
w8.pack()
w8.place(x=80, y=202)
w9 = Label(top2, text="     |                            ", background='yellow', fg="red")
w9.pack()
w9.place(x=80, y=219)
w10 = Label(top2, text="     |                            ", background='yellow', fg="red")
w10.pack()
w10.place(x=80, y=236)
w11 = Label(top2, text=" ____|____                        ", background='yellow', fg="red")
w11.pack()
w11.place(x=72, y=253)


T2 = Text(top2, height=1, width=4)
T2.pack()
T2.place(x=120, y=350)

teskt_iz_labele = StringVar()
teskt_iz_labele.set(guess_word)

W20 = Label(top2, textvariable=teskt_iz_labele, background='yellow', fg="blue", font=("Helvetica", 20))
W20.pack()
W20.place(x=72, y=300)

guess_taken = 0
def stampanje():

    provjera=T2.get("1.0", END)
    global guess_taken

    T2.delete('1.0', END)

    if not provjera.strip().lower()  in abeceda:
        W21 = Label(top2, text='                                                            ', background='yellow', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
        W21 = Label(top2, text='Niste unijeli slovo iz abecede A-Z', background='yellow', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
    elif provjera.strip().lower() in letter_storage:
        W21 = Label(top2, text='                                                          ', background='yellow', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
        W21 = Label(top2, text='Vec ste unijeli to slovo', background='yellow', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
    else:
        W21 = Label(top2, text='                                                         ', background='yellow', fg="red")
        W21.pack()
        W21.place(x=72, y=400)
        letter_storage.append(provjera.strip().lower())
        if provjera.strip().lower() in secretWord:

            for x in range(0, length_word):
                if secretWord[x] == provjera.strip().lower():
                    guess_word[x] = provjera.strip().upper()
                    stara_vrijednost = teskt_iz_labele.get()
                    teskt_iz_labele.set(guess_word)

                if not '-' in guess_word:
                    top2.destroy()
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



        else:
            W21 = Label(top2, text='                                                    ', background='yellow', fg="red")
            W21.pack()
            W21.place(x=72, y=400)
            W21 = Label(top2, text='Slovo se ne nalazi u tajnoj rijeci', background='yellow', fg="red")
            W21.pack()
            W21.place(x=72, y=400)

            guess_taken +=1

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

            w2 = Label(top2, text="     _________________ ", background='yellow', fg="red")
            w2.pack()
            w2.place(x=80, y=100)
            w3 = Label(top2, text="     |                           |", background='yellow', fg="red")
            w3.pack()
            w3.place(x=80, y=117)
            w4 = Label(top2, text="     |                           |", background='yellow', fg="red")
            w4.pack()
            w4.place(x=80, y=134)
            w5 = Label(top2, text="     |                          {0}".format(n[0]), background='yellow', fg="red")
            w5.pack()
            w5.place(x=80, y=151)
            w6 = Label(top2, text="     |                        {0}    {1}".format(n[1], n[2]), background='yellow', fg="red")
            w6.pack()
            w6.place(x=80, y=168)
            w7 = Label(top2, text="     |                           {0}".format(n[3]), background='yellow', fg="red")
            w7.pack()
            w7.place(x=80, y=185)
            w8 = Label(top2, text="     |                        {0}    {1}".format(n[4], n[5]), background='yellow', fg="red")
            w8.pack()
            w8.place(x=80, y=202)
            w9 = Label(top2, text="     |                            ", background='yellow', fg="red")
            w9.pack()
            w9.place(x=80, y=219)
            w10 = Label(top2, text="     |                            ", background='yellow', fg="red")
            w10.pack()
            w10.place(x=80, y=236)
            w11 = Label(top2, text=" ____|____                        ", background='yellow', fg="red")
            w11.pack()
            w11.place(x=72, y=253)

        if guess_taken == 6:
            top2.destroy()
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



B2 = Button(top2, text="Potvrdi slovo", command = stampanje )
B2.place(x=200, y=345)


top2.mainloop()