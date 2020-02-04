#Modules for client.py to run successfully
#netconnect and client_gui are in-house built modules for this program to run
from netconnect import *
from client_gui import *

#Begin the program
if __name__ == '__main__':
    root = tk.Tk()
    my_gui = GUI(root)
    root.mainloop()
