# Python code to add current script to the registry 
  
# module to edit the windows registry  
import winreg as reg  
import os              
  
def AddToRegistry(): 
    #get homepath of current user
    pth = os.getenv("HOMEPATH")

    # name of the python file with extension 
    s_name="C:" + pth + "\\Desktop\\TEAMPROJRAT-master\\UDP_Connection\\pos.pyw"

    # key we want to change is HKEY_CURRENT_USER  
    # key value is Software\Microsoft\Windows\CurrentVersion\Run 
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
      
    # open the key to make changes to 
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
      
    # modifiy the opened key 
    reg.SetValueEx(open,"pos",0,reg.REG_SZ,s_name) 
      
    # now close the opened key 
    reg.CloseKey(open) 

# Driver Code 
if __name__=="__main__": 
    AddToRegistry() 