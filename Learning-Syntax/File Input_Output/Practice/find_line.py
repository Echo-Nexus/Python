def check():
    word = "learning"
    with open("Python/Learning-Syntax/File Input_Output/Practice/task1.txt", "r") as f:
        data = f.read()
        if word in data:
            print("Found")
        else:
            print("not found")

check()


def check_for_line():
    word = "programming"
    data = True
    line_no = 1

    with open("Python/Learning-Syntax/File Input_Output/Practice/task1.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return line_no
            line_no += 1

    return -1   # ✅ correctly aligned


check_for_line()
