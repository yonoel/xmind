py_set = {2,3,4,5,7,6}
print(py_set)
py_set_mix = set([11, 1.1, "11", (1, 2)])
print(py_set_mix)
py_list = [11, 1.1, "11", (1, 2)]
#py_set = {py_list} error
py_set = {x for x in py_list}
print(py_set)
py_set_mix = set(py_list)
print(py_set_mix)
print('---------------')
print("The type of py_set",type(py_set))
print("The type of py_set_mix",type(py_set_mix))
# Let's try to create an empty Python set
py_set_num = {}
print("The value of py_set_num:", py_set_num)
print("The type of py_set_num:", type(py_set_num))

py_set_num = set()
print("The value of py_set_num:", py_set_num)
print("The type of py_set_num:", type(py_set_num))
# We'll use the setA and setB for our illustration
setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}

print("Initial setA:", setA, "size:", len(setA))
print("Initial setB:", setB, "size:", len(setB))

print("(setA | setB):", setA | setB, "size:", len(setA | setB))
print("setA.union(setB):", setA.union(setB), "size:", len(setA.union(setB)))
print("setB.union(setA):", setB.union(setA), "size:", len(setB.union(setA)))
print("(setA & setB):", setA & setB, "size:", len(setA & setB))
diffAB = setA - setB
print("diffAB:", diffAB, "size:", len(diffAB))
diffBA = setB - setA
print("diffBA:", diffBA, "size:", len(diffBA))
# Python set example using the caret ^ operator
symdiffAB = setA^setB
print("symdiffAB:", symdiffAB, "size:", len(symdiffAB))
symdiffBA = setB^setA
print("symdiffBA:", symdiffBA, "size:", len(symdiffBA))
symdiffAB = setA.symmetric_difference(setB)
print("symdiffAB:", symdiffAB, "size:", len(symdiffAB))
symdiffBA = setB.symmetric_difference(setA)
print("symdiffBA:", symdiffBA, "size:", len(symdiffBA))
