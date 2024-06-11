from math import exp
import tkinter as tk
import pyautogui as pg
import pygetwindow as gw
from time import time, sleep
import data

class MyApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        # variables
        self.pad = 2
        
        # initialization
        self.title('Automatisch invullen van lichamelijk onderzoek in HIS')
        self.minsize(700,600)
                
        # adding items
        self.create_menu()
        self.create_main_frame()        
        
        
    def create_menu(self):
        menubar = tk.Menu(self)
        
        # Create File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # Attach the menubar to the root window_HIS
        self.config(menu=menubar)
        
    def create_main_frame(self):
        # radio options
        self.selected_option = tk.IntVar()
        options = {
            "self.zuigeling_radio": "zuigeling_radio",
            "self.locomotorius_radio": "locomotorius_radio",
        }
        
        # Start frames
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0)
        
        # add a submit button
        new_frame = tk.Frame(main_frame, bg="blue", borderwidth=1, relief="solid").grid(row=0, column=0, padx= 5, pady=5)
        new_button = tk.Button(new_frame, text='Quit', width=15, height=2, command=self.quit)
        new_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        
        
        # input_frame
        input_frame = tk.Frame(main_frame, bg="yellow", borderwidth=1, relief="solid").grid(row=1, column=0, pady=5)
        tk.Label(input_frame, textvariable=tk.StringVar(input_frame,"Meetgegevens")).grid(row=1, column=0, columnspan=2, sticky='w')
        
        # item to input
        column_number = 1
        row_number = 2
        width_number = 5
        item_width = 50
        
        item_frame = tk.Frame(input_frame, width=item_width).grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Systolische bloeddruk"), anchor='nw').grid(row=row_number, column=column_number, sticky='w', padx=50)
        self.syst_entry = tk.Entry(item_frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='ew')
        column_number += 1
        
        item_frame = tk.Frame(input_frame, width=item_width).grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Diastolische bloeddruk"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        self.diast_entry = tk.Entry(item_frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='ew')
        column_number += 1
        
        item_frame = tk.Frame(input_frame, width=item_width).grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Lengte"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        self.lengte_entry = tk.Entry(item_frame, justify='left', width=width_number).grid(row=row_number+1, column=column_number, padx=5, sticky='ew')
        column_number += 1
        
        item_frame = tk.Frame(input_frame, width=item_width).grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Gewicht"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        self.gewicht_entry = tk.Entry(item_frame, justify='left', width=width_number).grid(row=row_number+1, column=column_number, padx=5, sticky='ew')
        column_number += 1
        
        item_frame = tk.Frame(input_frame, width=item_width).grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Pols"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        self.pols_entry = tk.Entry(item_frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='ew')
        column_number += 1
        
        item_frame = tk.Frame(input_frame, width=item_width).grid(row=row_number, column=column_number)
        tk.Label(item_frame, textvariable=tk.StringVar(item_frame, "Saturatie %"), anchor='nw').grid(row=row_number, column=column_number, sticky='w')
        self.sat_entry = tk.Entry(item_frame, justify='left', width=4).grid(row=row_number+1, column=column_number, padx=self.pad, sticky='ew')
        column_number += 1

        for category in data.physical.keys():
            print(category)
        # kinder
        self.zuigeling_radio = tk.Radiobutton(input_frame, text="Zuigeling onderzoek", variable=self.selected_option, value=1)
        self.zuigeling_radio.grid(row=5, column=0, columnspan=2, sticky='w')
        self.zuigeling_entry = tk.Text(input_frame, width=80, height=8)
        self.zuigeling_entry.grid(row=6, column=1, columnspan=6, padx=self.pad, sticky='ew')
        self.zuigeling_entry.insert("1.0", data.physical['Zuigeling'])
        
        # loco motorius
        self.locomotorius_radio = tk.Radiobutton(input_frame, text="Locomotorius onderzoek", variable=self.selected_option, value=2)
        self.locomotorius_radio.grid(row=7, column=0, columnspan=2, sticky='w')
        self.locomotorius_entry = tk.Text(input_frame, width=80, height=8)
        self.locomotorius_entry.grid(row=8, column=1, columnspan=6, padx=self.pad, sticky='ew')
        self.locomotorius_entry.insert("1.0", data.physical['Locomotorius'])
            
        # add a submit button
        button_frame = tk.Frame(main_frame, bg="blue", borderwidth=1, relief="solid").grid(row=100, column=0, padx= 5, pady=5)
        button = tk.Button(button_frame, text='Kopieer naar HIS', width=15, height=2, command=self.button_click)
        button.grid(row=100, column=0, columnspan=2, padx=5, pady=5, sticky='w')
        
    def button_click(self):
        text = ""
        if self.selected_option.get() == 1:
            text = self.zuigeling_entry.get("1.0", tk.END)
        elif self.selected_option.get() == 2:
            text = self.locomotorius_entry.get("1.0", tk.END)
        window_HIS = gw.getWindowsWithTitle('Medico')[0]
        window_HIS.activate()
        # pg.hotkey('alt', 'n')
        # sleep(2)
        # pg.press("C")
        # sleep(1)
        # pg.press('tab')
        # sleep(1)
        # pg.hotkey('alt', 'tab')
        # sleep(1)
        # pg.press('O')
        # sleep(1)
        # pg.press('tab')
        pg.typewrite(text, interval=0.01)
        # for i in range (4):
        #     pyautogui.press("tab")
        # pyautogui.typewrite("L01")
        # pyautogui.press("enter")
        # sleep(0.5)
        # with pyautogui.hold("alt"):
        #     pyautogui.press("s")
        # sleep(0.5)
        # for i in range (4):
        #     pyautogui.press("tab")
        # pyautogui.typewrite("Voorbeeldtekst regel P", interval=0.01)
        # with pyautogui.hold("shift"):
        #     pyautogui.press("f6")
        # sleep(2)
        # for i in range (4):
        #     pyautogui.press("tab")
        # pyautogui.typewrite("GEWICHT", interval=0.01)
        # sleep(0.4)
        # pyautogui.press("enter")
        # sleep(0.1)
        # pyautogui.press("enter")
        # sleep(0.2)
        # pyautogui.typewrite("76,5")
        # sleep(0.5)
        # pyautogui.press("enter")
        # sleep(1.0)
        # with pyautogui.hold("shift"):
        #     pyautogui.press("f6")
        # sleep(2)
        # for i in range (4):
        #     pyautogui.press("tab")
        # pyautogui.typewrite("TEMPERATUU", interval=0.01)
        # sleep(0.4)
        # pyautogui.press("enter")
        # sleep(0.1)
        # pyautogui.press("enter")
        # sleep(0.2)
        # pyautogui.typewrite("38,1")
        # sleep(0.5)
        # pyautogui.press("enter")
        
        # with pyautogui.hold("alt"):
        #     pyautogui.press("s")




if __name__ == '__main__':
    app = MyApp()
    app.mainloop()