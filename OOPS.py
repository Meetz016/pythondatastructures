class Student:
    print("Enter marks of 3 subjects(Space Seprated):")
    l=list(map(int,input().split()))
    print("average marks of the student is:",int(sum(l)/len(l)))

Student()