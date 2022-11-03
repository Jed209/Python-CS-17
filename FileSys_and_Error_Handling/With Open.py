try:
    with open("text.txt", "r") as text:
        text.write("This is With Open")
except Exception:
    print("Unsupported Operation, cannot write in read mode")
    