from math import exp
import tkinter as tk
import pyautogui
from time import time, sleep
import data

class MyApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        # variables
        self.pad = 5
        
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
        frame = tk.Frame(self, bg='blue')
        frame.pack(fill='both', expand=True, padx=self.pad, pady=self.pad)
        
        for keyword in data.physical.keys():
            # New paragraph
            sub_frame = tk.Frame(frame, bg="lightblue")
            sub_frame.pack(fill='both', expand=True, padx=self.pad, pady=self.pad)
            
            # Title of paragraph in its own frame
            label_frame = tk.Frame(sub_frame, height=1)
            label_frame.pack()
            name = tk.Label(sub_frame, textvariable=tk.StringVar(sub_frame,keyword), anchor='nw')
            name.pack(fill='x')
            
            # input of the paragraph
            input_frame = tk.Frame(sub_frame)
            input_frame.pack(side='top', fill='both', expand=True)
            for each_item in data.physical[keyword]:
                item_label = tk.Label(input_frame, textvariable=tk.StringVar(input_frame, each_item), anchor='nw')
                item_label.pack(fill='both')
        
        # add a submit button
        button_frame = tk.Frame(frame, bg='lightblue')
        button_frame.pack(fill='both')
        button = tk.Button(button_frame, text='Kopieer naar HIS', width=20, height=3, command=self.quit)
        button.pack(padx=self.pad, pady=self.pad, anchor='se')
    
            
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