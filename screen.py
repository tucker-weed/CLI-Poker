from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk

img = [] # Stores references to images to bypass garbage collection (Property of tkinter gui lib)


class Atrr:
    """A class that acts as the gui object."""
    
    def __init__(self,plr,river,pot):
        self.plr = plr
        self.river = river
        self.pot = pot

    def test(self):
        """This method initializes the root, and sets up player stats plus card images as information."""
        
        global img
        root = Tk()
        root.title("Controller")
        w = 650
        h = 650
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        Label(root, font=('Helvetica', 17), text=self.plr.alias_.upper()).pack(side="top", anchor=W, padx=0, pady=0)
        Label(root, font=('Helvetica', 17), text="NOTE: EXIT THIS WINDOW BEFORE TYPING").pack(side="top", anchor=W, padx=0, pady=0)
        
        for card in self.plr.hand:
            first = card.name
            last = card.suit
            if card.name == "ace":
                first = "A"
            elif card.name == "jack":
                first = "J"
            elif card.name == "queen":
                first = "Q"
            elif card.name == "king":
                first = "K"
                
            if card.suit == "clubs":
                last = "C"
            elif card.suit == "spades":
                last = "S"
            elif card.suit == "hearts":
                last = "H"
            elif card.suit == "diamonds":
                last = "D"
            stri = first+last
            image = (Image.open("/Users/tucker_weed/Desktop/PyPrograms/Poker/images/"+stri+".jpg"))
            imG = ImageTk.PhotoImage(image)
            img.append(imG)
            Label(root,image=imG).pack(side="top", anchor=W, padx=10, pady=0)

        Label(root, font=('Helvetica', 17), fg="green",text="CASH: "+str(self.plr.cash)).pack(side="top",anchor=W, padx=0, pady=0)
        Label(root, font=('Helvetica', 17), fg="green",text="POT: "+str(self.pot)).pack(side="top",anchor=W, padx=0, pady=0)
        Label(root, font=('Helvetica', 17), text="RIVER:").pack(side="top",anchor=W, padx=0, pady=0)
        
        for card in self.river:
            first = card.name
            last = card.suit
            if card.name == "ace":
                first = "A"
            elif card.name == "jack":
                first = "J"
            elif card.name == "queen":
                first = "Q"
            elif card.name == "king":
                first = "K"
                
            if card.suit == "clubs":
                last = "C"
            elif card.suit == "spades":
                last = "S"
            elif card.suit == "hearts":
                last = "H"
            elif card.suit == "diamonds":
                last = "D"
            stri = first+last
            image = (Image.open("/Users/tucker_weed/Desktop/PyPrograms/Poker/images/"+stri+".jpg"))
            imG = ImageTk.PhotoImage(image)
            img.append(imG)
            Label(root,image=imG).pack(side="left", anchor=W, padx=10, pady=0)
        
        return root

