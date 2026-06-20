def count(fname):
    f = None
    try:
        f = open(fname, 'r')
        data = f.readlines()
        return len(data)
    except FileNotFoundError:
        print("File is not found in the disk!")
    finally:
        print("Program completed")
        if f is not None:
            f.close()
f = input()
res = count(f)
print("No of lines :", res)
