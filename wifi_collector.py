import platform
import subprocess
import locale
import glob


def windows_wifi():
    if locale.setlocale(locale.LC_ALL, "").split('_')[0] in 'French':
        var1='Profil Tous les utilisateurs'
        var2='Contenu de la cl'
    else:
        var1='All User Profile'
        var2='Key Content'
    print("\n ***** WIFI Passoword check ongoing ... \n")
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp1252').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "Profil Tous les utilisateurs" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp1252').split('\n')
        #print(results)
        results = [b.split(":")[1][1:-1] for b in results if "Contenu de la cl" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))


def linux_wifi():
    print("\n ***** WIFI Passoword check ongoing ... \n")
    path='/etc/NetworkManager/system-connections/'
    if os.path.exists(path):
        for file_path in glob.glob(path):
            with open(file_path, 'r') as file:
                for line in file:
                    if line.startswith('ssid') or line.startswith('key-mgmt') or line.startswith('psk'):
                        print(line.strip())
    else:
        print('Probably this PC does not have a wireless interface')

def main():
    
    if platform.system()=='Windows':
        print("======> Operating System Detected : WINDOWS \n")
        windows_wifi()
    elif platform.system()=='Linux':
        print("======> Operating System Detected : LINUX \n")
        linux_wifi()
    else:
        print("======> Operating System Detected : N/A " )


if __name__ == "__main__":
    main()



