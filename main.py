import tkinter as tk
import pyautogui
from time import time, sleep
import data

class MainWindow:
    
    def __init__(self, window):
        self.window = window
        self.menubar = tk.Menu(self.window)
                
    def menu_bar(self):
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.window.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.window.config(menu=self.menubar)
    
    def window_frame(self):
        self.frame = tk.Frame(self.window, background='red')
        self.frame.pack()

        
         
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

    def test(self):
        print('okay')

def main(): 
    root = tk.Tk()
    root.title('Automatisch invullen van lichamelijk onderzoek in HIS')
    root.geometry('500x300')
    MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()