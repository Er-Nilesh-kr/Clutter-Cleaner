import os


def CreateDir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folder_name, files):
    for file in files:
        os.replace(file, f"{folder_name}/{file}")


files = os.listdir()
files.remove('main.py')
image_ext = ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.psd', '.bmp']
doc_ext = ['.pdf', '.doc', '.docx', '.ppt', '.pptx']
media_ext = ['.mp4', '.mp3', '.mkv', '.flv', '.mov', '.wmv', '.m4a']
compressed_ext = ['.zip', '.rar', '.7z', '.pkg', '.tar']
others = []
CreateDir('Images')
CreateDir('Documents')
CreateDir('Media')
CreateDir('Compressed Files')
CreateDir('Others')

images = [file for file in files if os.path.splitext(file)[
    1].lower() in image_ext]
docs = [file for file in files if os.path.splitext(file)[1].lower() in doc_ext]
media = [file for file in files if os.path.splitext(
    file)[1].lower() in media_ext]
compressed = [file for file in files if os.path.splitext(
    file)[1].lower() in compressed_ext]

for file in files:
    oext = os.path.splitext(file)[1].lower()
    if (oext not in image_ext) and (oext not in doc_ext) and (oext not in media_ext) and (oext not in compressed_ext) and os.path.isfile(file):
        others.append(file)

move("Images", images)
move("Documents", docs)
move("Media", media)
move("Compressed Files", compressed)
move("Others", others)
