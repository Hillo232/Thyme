import time
import sys
import os
import os.path
import urllib.request as request
import platform
commands=["cd","burn","delete","append","clear","image","help","python","terminate","os"]
while True:
  my_system = platform.uname()
  thyme=input(f"{my_system.system}"+" Thyme ")
  thyme=thyme.split(" ")
  if thyme[0]=="cd":
    cd=thyme[1:len(thyme)]
    print("You have requested to go into: "+str(cd))
    for x in("Loading...\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)
    time.sleep(2)
    thyme=thyme[1:len(thyme)]
    cd=' '.join(thyme)

    if cd.endswith(('.png', '.jpg', '.jpeg',".pdf")):
      print("Cannot open file because the file is an image.")
    else:    
      f=open(cd,"r")
      content=f.readlines()
      content=' '.join(content)
      print(content)
      f.close()
    print("\n")
  if thyme[0]=="burn":
    burned_file_name=thyme[1]
    burned=thyme[2:len(thyme)]
    thyme=' '.join(thyme)
    print("You have burned: "+burned_file_name+" to you disk.")
    if os.path.isfile(burned_file_name):    
      burned_file_name.write(burned)
    else:
      f=open(burned_file_name,"w")
      burned=' '.join(burned)
      f.write(str(burned))
      f.close()
  if thyme[0]=="delete":
    delete=thyme[1]
    delete=''.join(delete)
    print("You have removed file:"+delete)
    os.remove(delete)
  if thyme[0]=="append":
    first=thyme[1]
    append=thyme[2:len(thyme)]
    append=' '.join(append)
    f=open(first,"a+")
    f=f.write(append)
    print("Appended: "+append+" to file:"+first)
  if thyme[0]=="strip":
    file=thyme[1]
    strip=thyme[2:len(thyme)]
    f=open(file,"w+")

    f.close()
  if thyme[0]=="clear":
    os.system("clear")
  if thyme[0]=="image":
    filename=input("Filename: ")
    imagetype=input("Image type: ")
    image_url=input("Image Url: ")
    file=filename+"."+imagetype
    open(file,"w")
    request.urlretrieve(image_url,file)
  if thyme[0]=="help":
    print("cd\n   Change Files\nburn\n   Create Files\ndelete\n   Delete Files\nappend\n   Add text to files.\nclear\n   Clears the whole screen.\nimage\n   Creates a file with the image.\nhelp\n   Brings up this text.\nreplace\n   Allows you to replace certain text in a file\npython\n   Allows you to run print commands ONLY.\nterminate\n   Does not take arguments, terminates the program.")
  if thyme[0]=="replace":
    file=thyme[1]
    replace=thyme[2]
    will_replace=thyme[3]
    f=open(file,"r")
    content=f.read()
    f.close()
    if replace in content:
      f = open(file,'w')
      content=content.replace(replace,will_replace)
      f.write(content)
      print(content)
      f.close()
    else:
     print("There is no such word or character in this file.")
  if thyme[0] not in commands:
    print("-Thyme:"+thyme[0],": Not found.",end='')
    sys.stdout.flush()
    time.sleep(3)
    
    print('\renter valid command' + ' ' * len(thyme[0]))
  if thyme[0]=="python":
    
    print("NO VARIABLES. SIMPLE PRINT COMMANDS ONLY.")
    while True:
      test=input(">>> ")
      if test=="exit":
        break
      if test=="" or test==" ":
        continue
      else:
        try:
          eval(test)
        except Exception as e:
          print(e)
          continue
  if thyme[0]=="terminate":
    while True:
      terminate=input("Type anything for yes or type NO in all caps with no space.")
      if terminate=="NO":
        break
      else:
        sys.exit()
