dict1 = {"name":{"eva":"arya"},"mom":{"priya":"arya"}}
def flatten_dict(dict1):
  def expand(key,value):
   if isinstance(value,dict):
      return [(key + '.' + k, v) for k,v in flatten_dict(value).items()] 
   else:
     return[(key,value)] 
  items = [item for k,v in dict1.items() for item in expand(k,v)]

  return dict(items)  
print flatten_dict(dict1) 
