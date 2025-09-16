#Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a
# regular expression and count the number of lines that matched the regular expression:
print("Where is the file that you are going to check?")
file_type = input("Type 'path' if it is in the local files and 'web' if it is in the web: ")
matches = list()
if file_type == "path":
    file_input = input("Enter the path of the file to open it: ")
    regex = input("Enter a regular expression: ")
    try:
        import re
        file = open(file_input)
        for line in file:
            line = line.strip()
            x = re.findall(regex, line)
            if len(x) < 1:
                continue
            matches.append(x)
        print(f"The file had {len(matches)} lines that matched {regex}")
    except:
        raise ValueError("The path is not correct or the file doesn't exist")
elif file_type == "web":
    file_url = input("Please type the url of the file: ")
    regex = input("Enter a regular expression: ")
    try:
        import urllib.request, re
        file_web = urllib.request.urlopen(file_url)
        for line in file_web:
            line = line.decode()
            line = line.strip()
            x = re.findall(regex, line)
            if len(x) < 1:
                continue
            matches.append(x)
        print(f"The file had {len(matches)} lines that matched {regex}")
    except:
        raise ValueError("The url is not correct or the it doesn't exist")
else:
    print("Please insert one of the options given.")

