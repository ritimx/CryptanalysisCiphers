from gui.main_window import MainWindow
import tkinter as tk

def main():
    
    root = tk.Tk()
    root.title("Cryptanalysis of Simple Ciphers")

    
    app = MainWindow(root)
    app.run()

if __name__ == "__main__":
    main()
