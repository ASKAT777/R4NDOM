import os,time,platform
os.system('clear')
print('\n\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m TOOL IS OFF..........\n')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print("\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOOL IS OFF \033[1;91m64\033[1;92m .....")
    time.sleep(2)
    import RM64
elif bit=='32bit':
    print("\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOOLS IS OFF \033[1;91m32\033[1;92m .....")
    time.sleep(2)
    import RM32
else:
    print('\033[1;31m[\033[1;92m×\033[1;91m] TOOLS IS OFF !!!!!')
 
