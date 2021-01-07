data = int(input("enter a number "))

def fizzbuzz(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else: print(i)    

fizzbuzz(data)

"""
function oddRange(end) {
  const arr = [];

  for (let i = 1; i <= end; i += 2) {
      arr.push(i);
  }

  return arr;
}
"""
def oddRange(n):
    list = [] 
    for i in range(1, len(n), 2):
       list.append(i)
    return list


print(oddRange([1,2,3,4,5,6,7,8]))

"""
function catBuilder(name, color, toys) {
  const cat = {
    name: name,
    color: color,
    toys: toys
  };

  return cat;
}
"""

def cat_builder(name, color, toys):
    cat = {
        "name": name,
        "color": color ,
        "toys": toys
    }
    return cat

print(cat_builder('tom', 'grey', 'jerry'))    
