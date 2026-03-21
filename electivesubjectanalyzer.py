subjectsofDeptA=set(str(input("Enter subjects for Department A:")).split(","))
subjectsofDeptB=set(str(input("Enter subjects for Department B:")).split(","))

def find_all_subjects(subdeptA,subdeptB):
    return subdeptA.union(subdeptB)

def find_common_subjects(subdeptA,subdeptB):
    return subdeptA.intersection(subdeptB)

def find_unique_subjects(subdeptA,subdeptB):
    return subdeptA.difference(subdeptB)

def find_exclusive_subjects(subdeptA,subdeptB):
    return subdeptA.symmetric_difference(subdeptB)

def calculate_similarity(subdeptA,subdeptB):
    return (len(subdeptA.intersection(subdeptB))/len(subdeptA.union(subdeptB)))*100

print("All Subjects:",find_all_subjects(subjectsofDeptA,subjectsofDeptB))
print("Common Subjects:",find_common_subjects(subjectsofDeptA,subjectsofDeptB))
print("Only Dept A:",find_unique_subjects(subjectsofDeptA,subjectsofDeptB))
print("Only Dept B:",find_unique_subjects(subjectsofDeptB,subjectsofDeptA))
print("Exclusive Subjects:",find_exclusive_subjects(subjectsofDeptA,subjectsofDeptB))
print("Similarity Percentage:",round(calculate_similarity(subjectsofDeptA,subjectsofDeptB),2),"%")

