try:
    f=open("studentregistration","r")
except  FileNotFoundError:
    print("file not found")
finally:
    print("The code isi cleaned and can not be found")
