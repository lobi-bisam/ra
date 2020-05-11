
import os, shutil

def organize_files(location):
    
    os.chdir(location)
    cwd = os.getcwd()
    print(cwd)
    
    files = os.listdir(cwd)
    print(files)
    
    
 #tworzymy liste wypisujaca rozszerzenia plikow
   
    all_ext = set(os.path.splitext(file)[-1] for file in os.listdir(cwd))
     
    for ext in all_ext:
        if ext == '':
            all_ext.remove('')
            break
        
    print(all_ext)
    
 #dla wypisanych rozszerzen tworzymy foldert   
    for ext in all_ext:
        try:
            folderName = cwd + "\\" + ext.replace('.', '')
            os.mkdir(folderName)
        except:
            print(str(ext) + " już istnieje")
          
 #do każdego stworzonego folderu wrzucamy pliki z danych rozszerzeniem           
    for file in files:
        for ext in all_ext:
            if file.endswith(ext):
                oldLocation = cwd + "\\" + file
                newLocation = cwd + "\\" + ext.replace('.', '') + "\\" + file
                shutil.move(oldLocation, newLocation)
                break
        

organize_files(r"C:\Users\Iza\Documents\UKSW\Pedagogika Specjalna\Praktyki")