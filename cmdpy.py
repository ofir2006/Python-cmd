from os import chdir,popen,getcwd

while True:
    cmd = input(getcwd() + "> ")
    if cmd[0:2] == "cd":
        chdir(cmd[3:])
    output = popen(cmd).readlines()
    for line in output:
        print(line.strip())
        
    