import time
import sys
import os
import os.path
import urllib.request as request

while True:
  thyme=input("Thyme ")
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
    print("cd\n   Change Files\nburn\n   Create Files\ndelete\n   Delete Files\nappend\n   Add text to files.\nclear\n   Clears the whole screen.\nimage\n   Creates a file with the image.\nhelp\n   Brings up this text.")
