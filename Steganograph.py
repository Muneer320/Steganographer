def hideImage():
    import PIL.Image as I
    import io

    loc = input('Location of picture to be hidden >>> ')
    d_loc = input('Location of picture to hide in >>> ')
    img = I.open(loc)
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')

    with open(d_loc, 'ab') as f:
        f.write(byte_arr.getvalue())

    print("Done!")

def hideMessage():
    file = input("File to hide message in >>> ")
    with open(file, 'ab') as f:
        message = bytes(input("Message to hide >>> "), 'utf-8')
        f.write(message)

    print("Done!")

def hideExecutable():
    imgLoc = input("Image location >>> ")
    exeLoc = input("EXE location >>> ")
    with open(imgLoc, 'ab') as f, open(exeLoc, "rb") as e:
        f.write(e.read())
    print("Done!")

def hideVideo():
    imgLoc = input("Image location >>> ")
    vidLoc = input("Video location >>> ")
    with open(imgLoc, 'ab') as f, open(vidLoc, "rb") as e:
        f.write(e.read())
    print("Done!")

def hideFolder():
    import zipfile
    import os

    folder = input("Folder to hide >>> ")
    d_loc = input('Location of picture to hide in >>> ')
    n_zip = folder + ".zip"
    
    with zipfile.ZipFile(n_zip, 'w') as z:
        for root, _, files in os.walk(folder):
            for file in files:
                z.write(os.path.join(root, file))

    with open(d_loc, 'ab') as f:
        with open(n_zip, 'rb') as z:
            f.write(z.read())

    os.remove(n_zip)

    print("Done!")


def getHiddenImage():
    import PIL.Image as I
    import io

    file = input("File to get hidden image from >>> ")
    n_file = input("Name of new image >>> ")
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)

        newImg = I.open(io.BytesIO(f.read()))
        newImg.save(n_file)
    print(f"Secret image saved as {n_file}.jpg")

def getHiddenMessage():
    file = input("File to get hidden message from >>> ")
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)
        print(f.read().decode('utf-8'))

        save = input("\nSave to file? (y/n) >>> ")
        if save == 'y':
            with open('secret.txt', 'w') as s:
                s.write(f.read().decode('utf-8'))
            print("Saved to secret.txt")

def getHiddenExecutable():
    file = input("File to get hidden executable from >>> ")
    n_file = input("Name of new executable (with extension; ex: file.exe)>>> ")
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)

        with open(n_file, 'wb') as e:
            e.write(f.read())

    print("Done!")

def getHiddenVideo():
    file = input("File to get hidden video from >>> ")
    n_file = input("Name of new video (with extension; ex: file.mp4)>>> ")
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)

        with open(n_file, 'wb') as e:
            e.write(f.read())

    print("Done!")

def getHiddenFolder():
    import zipfile
    import os

    file = input("File to get hidden folder from >>> ")
    n_folder = input("Name of new folder >>> ")
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)

        with open("temp.zip", 'wb') as z:
            z.write(f.read())

    with zipfile.ZipFile("temp.zip", 'r') as z:
        z.extractall(n_folder)

    os.remove("temp.zip")
    print(f"Folder extracted as {n_folder}")


def removeHiddenData():
    file = input("File to remove hidden data from >>> ")
    with open(file, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)
        with open('clean_' + file, 'wb') as c:
            c.write(content[:offset + 2])
    print(f"Clean file saved as clean_{file}")



def main():
    print("Welcome to Steganography!")
    print("1. Hide image")
    print("2. Hide message")
    print("3. Hide executable")
    print("4. Hide video")
    print("5. Hide Folder")
    print("6. Get hidden image")
    print("7. Get hidden message")
    print("8. Get hidden executable")
    print("9. Get hidden video")
    print("10. Get hidden folder")
    print("11. Remove hidden data")

    funcs = {
        '1': hideImage,
        '2': hideMessage,
        '3': hideExecutable,
        '4': hideVideo,
        '5': hideFolder,
        '6': getHiddenImage,
        '7': getHiddenMessage,
        '8': getHiddenExecutable,
        '9': getHiddenVideo,
        '10': getHiddenFolder,
        '11': removeHiddenData
    }

    choice = input(">>> ")
    if choice in funcs:
        funcs[choice]()
    else:
        print("Invalid choice. Exiting...")
        r = input("Press r to restart >>> ")
        if r == 'r':
            main()

'''
    match input(">>> "):
        case '1':
            hideImage()
        case '2':
            hideMessage()
        case '3':
            hideExecutable()
        case '4':
            hideVideo()
        case '5':
            hideFolder()
        case '6':
            getHiddenImage()
        case '7':
            getHiddenMessage()
        case '8':
            getHiddenExecutable()
        case '9':
            getHiddenVideo()
        case '10':
            getHiddenFolder()
        case '11':
            removeHiddenData()
        case _:
            print("Invalid choice. Exiting...")
            r = input("Press r to restart >>> ")
            if r == 'r':
                main()
'''


if __name__ == '__main__':
    main()
