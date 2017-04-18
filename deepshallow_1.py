import copy
dict1 ={"name":"eva","age":"7","grade":"1"}
dict2 = copy.deepcopy(dict1)
dict3 =dict1.copy()
dict1["grade"] = "23" 
dict2["name"] = "priya"
print dict1 
print dict2
print dict3 
 
 
