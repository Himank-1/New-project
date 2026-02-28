import os, shutil
path = r'/home/him/Documents/'
print(os.path.exists(path)) 

os.listdir(path)

folder=['documents','misc','images', 'music', 'files','videos','folders']

for i in range (len(folder)):
    folder_path = os.path.join(path, folder[i])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Folder "{folder[i]}" created successfully.')

file_name = os.listdir(path)
print(file_name)
for file in file_name:
    print(file)
    if os.path.isdir(path+file):
        if file in folder:  
            print("CONTINUE")
            continue
        else: shutil.move(path+file, path+'folders/'+file)
        print(f'File "{file}" moved successfully.')
    elif file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.txt') or file.endswith('.xlsx') or file.endswith('.pptx') or file.endswith('.odt') or file.endswith('.rtf'):
        shutil.move(path+file, path+'documents/'+file)
    elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif') or file.endswith('.bmp') or file.endswith('.svg') or file.endswith('.jpeg'):
        shutil.move(path+file, path+'images/'+file)
    elif file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.flac') or file.endswith('.aac') or file.endswith('.ogg'):
        shutil.move(path+file, path+'music/'+file)
    elif file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv') or file.endswith('.mov') or file.endswith('.flv') or file.endswith('.m4a'):
        shutil.move(path+file, path+'videos/'+file)
    elif file.endswith('.zip') or file.endswith('.rar') or file.endswith('.7z') or file.endswith('.tar') or file.endswith('.gz') or file.endswith('.exe') or file.endswith('.ttf'):
        shutil.move(path+file, path+'files/'+file)
    else:
        shutil.move(path+file, path+'misc/'+file)
print("Item Sorted completely")
