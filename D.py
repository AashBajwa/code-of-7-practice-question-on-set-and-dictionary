#WAP TO create dictionary containing 5 students and thier marks ask the user for name and check whether their marks above 50 pass or fail
student={
    "Ayesha":90,
    "Samaviya":80,
    "Areeba":40,
    "Eshwa":30,
    "Sadia":75
}
name=input("Enter a student name:")
if name in student:
    marks=student[name]
    if marks>=50:
        print(name,"got",marks,"Marks Pass")
    else:
        print(name,"got",marks,"Marks Fail")    
    print(name,"is in this dictionary")
else:
    print(name,"is not in this dictionary")  

#WAP create two sets of students names ask user a name to check either student is present
set1={"Ayesha","Samaviya","Sadia",}  
set2={"Eshwa","Areeba"}
name=input("Enter a name:")
if name in set1:
    print(name,"Student is found in set1",set1)
elif name in set2:
    print(name,"Student is found in set2",set2)
else:
    print(name,"Student is not found in these sets")  

#WAP create a tuple of 5 numbers sum of these number and check sum is greater than 50 or not
tup=(10,20,5,7,15)  
total=sum(tup)
print(total)
aver=total/len(tup)
print(aver)
if aver>=50:
    print("aver is greater than 50")
else:
    print("aver is less than 50")

#WAP create a dictionary conatain student name, age, subjects(tuple), hobbies(set), marks(list) check age above then 18, passed, python present, average marks
dict={
    "name":"Ayesha",
    "age":20,
    "subjects":("urdu","english","biology"),
    "hobbies":{"python","Javascript","HTML"},
    "marks":[90,95,99]
}
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["subjects"])
print(dict["hobbies"])
print(dict["marks"])
if dict["age"]>18:  
    print("It'adult")
else:
    print("not adult")

#WAP UNION of 2 sets
set1={1,2,3}
set2={4,5,6}
set=set1.union(set2)
print(set)

#WAP TO intersect of 2 sets
set1={1,2,3,4}
set2={3,4,5,6}
set=set1.intersection(set2)
print(set)

#WAP to find difference pf 2 sets
set1={1,2,3,4}
set2={3,4,5}
set=set1.difference(set2)
print(set)