<#
Author: Mitch Hydrick
Date: 30 Jan 2020
Synopsis:
    - Checks the operating system for 32 bit or 64 bit
    - Looks for python installed somewhere on the system
      and if not found, downloads the correct python installer based on 
      system architecture, and installs it silently without user interaction
    - It adds the python and pip path to the PATH environment variable
      for ease of calling python and pip in other scripts
#>

# initialize flags indicating 32 or 64 bit to 0
$thirty_two_bit = 0
$sixty_four_bit = 0

# initialize python_local_path, python_download_link, python_exe, pip_path, and python_download_local_path
$python_local_path = "C:\Python38\python.exe"
$pip_path = ($python_local_path.Substring(0,11) + "\Scripts")
$python_user_path = $env:USERPROFILE + "\AppData\Local\Programs\Python\Python38"
$python_download_link = ""
$python_exe = ""
$python_download_local_path = ""

# Function that finds out if the machine is 32 bit or 64 bit, then sets the appropriate flag
Function Set-OS_Architecture_Flag{ 
    $os_architecture = (wmic os get osarchitecture)[2]

    Write-Host "The OS architecture is: $($os_architecture)"

    if ($os_architecture -eq "64-bit"){
        $sixty_four_bit = 1
    } else {
        $thirty_two_bit = 1
    }
}

# 
Function Download-Python{
    
    if ($thirty_two_bit){
        # 32-bit version download link
        $python_download_link = "https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe"
    } else {
        # 64-bit version download link
        $python_download_link = "https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe"
    }

    # python executable name
    $python_exe = "$(($python_download_link).split('/')[-1])"

    # local python download path
    $python_download_local_path = "$($Env:TEMP)\$($python_exe)"

    # download appropriate version for the os architecture
    Invoke-WebRequest $python_download_link -OutFile $python_download_local_path 

    return $python_download_local_path
}

# Function that installs python quietly without user input necessary
Function Install-Python($py_path, $target_dir){
    & $py_path /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=$($target_dir) 
}

### Start of Script Execution ###

Set-OS_Architecture_Flag

# find location of python
Write-Host "Starting search for python."
$python_locations = C:\windows\system32\where.exe /r C:\ Python38

# if python is not installed, download and install it
if ($python_locations.count -eq 0){
    
    Write-Host "Python not found, downloading now..."
    
    # download python
    $download_path = Download-Python
    
    Write-Host "Finished downloading; installing now..."
    
    # install python
    Install-Python -py_path $download_path -target_dir $python_local_path
    
    Write-Host "Finished installing python."

} else {

    Write-Host "Found Python"

}