import tkinter as tk

class WhiteBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteBoard(root)
    root.geometry("1050x570")
    root.config(bg="#f2f3f5")
    root.resizable(False,False)
    
    root.mainloop()