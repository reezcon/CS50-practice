file_name = input("File name: ").lower().lstrip().rstrip()
dot = file_name.rfind(".")
extension_name = file_name[dot:]

if extension_name == ".gif":
    print("image/gif")
elif extension_name == ".jpg" or extension_name == ".jpeg":
    print("image/jpeg")
elif extension_name == ".png":
    print("image/png")
elif extension_name == ".pdf":
    print("application/pdf")
elif extension_name == ".txt":
    print("text/plain")
elif extension_name == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
