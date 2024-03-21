try:
    with open(r"C:\Users\kmeet\OneDrive\Desktop\PythonProject\demo.txt",'r') as file:
        content=file.read()
        print("Here are the details Of the file")
        for text in content:
            print(text,end="")
except FileNotFoundError:
    print("File does not exists")
except Exception as e:
    print(f'An error occurred: {e}')