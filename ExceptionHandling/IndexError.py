li = list(map(int, input().split()))

try :
    idx = int(input("Enter index :"))
    print(li[idx])
    
except IndexError:
    print("Please provide index with in the range of list")
    print(f"i.e 0~{len(li)} ")
    