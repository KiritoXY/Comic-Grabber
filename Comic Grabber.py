from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as url
file=open("comic.txt","r")
name=input("Enter Name of Comic")
var = bs(file, "html.parser")
print("URL parsered to BS4")
list=var.findAll("img",{"rel":"noreferrer"})
index=1
for images in list:
    file_loc=str(images["src"])
    temp=url(file_loc)
    output=open((+"Comics\ file"+str(index)+".jpg"),"wb")
    output.write(temp.read())
    output.close()
    print("Downloaded file "+str(index)+" of "+ str(len(list)))
    index=index+1
    break
print("Download Complete")