from math import exp
import tkinter as tk
import pyautogui
from time import time, sleep
import data

class MyApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        # variables
        self.pad = 2
        
        # initialization
        self.title('Automatisch invullen van lichamelijk onderzoek in HIS')
        self.minsize(800,400)
                
        # adding items
        self.create_menu()
        self.create_main_frame()        
        
        
    def create_menu(self):
        menubar = tk.Menu(self)
        
        # Create File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # Attach the menubar to the root window
        self.config(menu=menubar)
        
    def create_main_frame(self):
        main_frame = tk.Frame(self, bg='yellow')
        main_frame.grid(row=0, column=0)
        
        # titel
        title_frame = tk.Frame(main_frame, bg="red", borderwidth=1, relief="solid").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(title_frame, textvariable=tk.StringVar(title_frame,"Meetgegevens")).grid(row=0, column=0, sticky='w')
        
        # input_frame of "Meetgegevens"
        input_frame = tk.Frame(main_frame, bg="yellow", borderwidth=1, relief="solid").grid(row=1, column=0, sticky="news")
        
        # item to input
        column_number = 0
        row_number = 1
        width_number = 5
        
        item_frame = tk.Frame(input_frame, bg="green", borderwidth=1, relief="solid").grid(row=row_number, column=column_number, sticky="news")
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Lengte"), bg="yellow", anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        lengte_entry = tk.Entry(item_frame, justify='left', width=width_number).grid(row=row_number+1, column=column_number, padx=5, sticky='ww')
        
        column_number += 1
        item_frame = tk.Frame(input_frame, bg="green", borderwidth=1, relief="solid").grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Gewicht"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        gewicht_entry = tk.Entry(item_frame, justify='left', width=width_number).grid(row=row_number+1, column=column_number, padx=5, sticky='w')
        
        # column_number += 1
        # item_frame = tk.Frame(input_frame).grid(row=row_number, column=column_number)
        # tk.Label(frame, textvariable=tk.StringVar(frame, "Systolische bloeddruk"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        # syst_entry = tk.Entry(frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='w')
        # column_number += 2
        
        # tk.Label(frame, textvariable=tk.StringVar(frame, "Diastolische bloeddruk"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        # diast_entry = tk.Entry(frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='w')
        # column_number += 2
        
        # tk.Label(frame, textvariable=tk.StringVar(frame, "Pols"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        # pols_entry = tk.Entry(frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='w')
        # column_number += 2
        
        # tk.Label(frame, textvariable=tk.StringVar(frame, "Saturatie %"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        # sat_entry = tk.Entry(frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='w')
        # column_number += 2

        
        # add a submit button
        button_frame = tk.Frame(main_frame).grid(row=100, column=0, pady=10)
        button = tk.Button(button_frame, text='Kopieer naar HIS', width=20, height=3, command=self.quit).grid(row=3, column=0, padx=5, pady=5)
    
            
    def button_click(self):
        with pyautogui.hold("alt"):
            pyautogui.press("tab")
        # pyautogui.getWindowsWithTitle("Medicom*")[0]
        sleep(2)
        pyautogui.hotkey("shift", "f12")
        sleep(2)
        pyautogui.typewrite("Voorbeeldtekst regel S", interval=0.01)
        for i in range (3):
            pyautogui.press("tab")
        pyautogui.typewrite("C")
        pyautogui.press("tab")
        pyautogui.typewrite("Voorbeeldtekst regel O", interval=0.01)
        for i in range (4):
            pyautogui.press("tab")
        pyautogui.typewrite("L01")
        pyautogui.press("enter")
        sleep(0.5)
        with pyautogui.hold("alt"):
            pyautogui.press("s")
        sleep(0.5)
        for i in range (4):
            pyautogui.press("tab")
        pyautogui.typewrite("Voorbeeldtekst regel P", interval=0.01)
        with pyautogui.hold("shift"):
            pyautogui.press("f6")
        sleep(2)
        for i in range (4):
            pyautogui.press("tab")
        pyautogui.typewrite("GEWICHT", interval=0.01)
        sleep(0.4)
        pyautogui.press("enter")
        sleep(0.1)
        pyautogui.press("enter")
        sleep(0.2)
        pyautogui.typewrite("76,5")
        sleep(0.5)
        pyautogui.press("enter")
        sleep(1.0)
        with pyautogui.hold("shift"):
            pyautogui.press("f6")
        sleep(2)
        for i in range (4):
            pyautogui.press("tab")
        pyautogui.typewrite("TEMPERATUU", interval=0.01)
        sleep(0.4)
        pyautogui.press("enter")
        sleep(0.1)
        pyautogui.press("enter")
        sleep(0.2)
        pyautogui.typewrite("38,1")
        sleep(0.5)
        pyautogui.press("enter")
        
        with pyautogui.hold("alt"):
            pyautogui.press("s")




if __name__ == '__main__':
    app = MyApp()
    app.mainloop()