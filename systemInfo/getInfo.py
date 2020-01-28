import subprocess
import pprint


def main():
    result = subprocess.check_output(['sysinfo.exe'])
    result2 = subprocess.check_output(["ipInfoWindows.exe"])
    pprint.pprint(result.decode("utf-8"))
    pprint.pprint(result2.decode("utf-8"))

main()
