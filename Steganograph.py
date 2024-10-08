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
    print("5. Get hidden image")
    print("6. Get hidden message")
    print("7. Get hidden executable")
    print("8. Get hidden video")
    print("9. Remove hidden data")

    
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
            getHiddenImage()
        case '6':
            getHiddenMessage()
        case '7':
            getHiddenExecutable()
        case '8':
            getHiddenVideo()
        case '9':
            removeHiddenData()
        case _:
            print("Invalid choice. Exiting...")
            r = input("Press r to restart >>> ")
            if r == 'r':
                main()


if __name__ == '__main__':
    main()