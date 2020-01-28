import subprocess ## import subprocess

def main(): ## define mine
    ## set the variables to be the right subprocess thing
    sysinfo = subprocess.check_output(['sysinfo.exe']).decode('ascii')
    ipInfo = subprocess.check_output(["ipInfoWindows.exe"]).decode('ascii')
    userInfo = subprocess.check_output(["sysUser.exe"]).decode('ascii')
    ## print the data
    print(sysinfo)
    print(ipInfo)
    print(userInfo)

main()
