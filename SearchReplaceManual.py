import os
import sys
import glob
import pickle


folder = 'Folder'
find = 'S:/'
replace = 'D:/'



f = glob.glob(folder+"*.*")

for i in f:
    dataOpen = open(i,"rb")
    conteudo = "".join(dataOpen)
    dataOpen.close()
    

    conteudo = conteudo.replace(find, replace)
    #print (conteudo)
                
    dataWrite = open(i, "wt")
    dataWrite.write(conteudo)
    dataWrite.close()