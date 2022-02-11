def function1():
    a=input("Enter the file name : ")
    wordC= 0
    openFile=open(a,'r')
    for i in openFile :
       splitArray1= i.split()
       wordC=wordC+len(splitArray1)
    print(wordC)

function1()

