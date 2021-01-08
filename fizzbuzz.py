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

'''
function valuePair(obj1, obj2, key) {
    let val1 = obj1[key];
    let val2 = obj2[key];
    const arr = [val1, val2];
  
    return arr;
}
'''
def valuePair(obj1, obj2, key):
    val1 = obj1[key]
    val2 = obj2[key]
    list =[val1, val2]
    return list

obj1 = {"name":"lev", "last_name":"choubine"}
obj2 = {"name":"rome", "last_name":"bell"}
name ="name"
print(valuePair(obj1, obj2, name))

'''
function doesKeyExist(obj, key) {
  return obj[key] !== undefined;
}
'''

def does_key_exist(obj, key):
    if key in obj:
        print('found')
    else: print('not found')    
  

does_key_exist(obj1,"name")
does_key_exist(obj1,"job")

'''
function adults(people) {
  const names = [];

  for (let i = 0; i < people.length; i += 1) {
    let person = people[i];
    if (person.age >= 18) {
      names.push(person.name);
    }
  }

  return names;
}
'''
people = [{"name":"Lev", "age":"5"},{"name":"Lenin", "age":"150"},{"name":"picachu", "age": "78"}]
def adults(people):
    names=[]
    for i in range(len(people)):
        person = people[i]
        if(int(person["age"]) >= 18):
            names.append(person[name])
    return names

print(adults(people))

"""
function isPrime(number) {
    if (number < 2) {
      return false;
    }
  
    for (let i = 2; i < number; i += 1) {
      if (number % i === 0) {
        return false;
      }
    }
  
    return true;
}

"""
def is_prime(number):
    if int(number) < 2:
        return False 
    if (number == 2): return True    
    for i in range(2, number):
        if number % i == 0:
            return False
        else: 
            return True

print(is_prime(4))    

"""

function firstNPrimes(n) {
    const primes = [];
    let num = 2;
  
    while(primes.length < n) {
      if (isPrime(num)) {
        primes.push(num);
      }
  
      num += 1;
    }
  
    return primes;
}


"""

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
         
        if is_prime(num) is True:
            primes.append(num)
        num+=1    
    return primes

print(first_n_primes(4))

'''
function sumOfNPrimes(n) {
  let sum = 0;
  let primes = firstNPrimes(n);

  for (let i = 0;  i < primes.length; i += 1) {
      sum += primes[i];
  }

  return sum;
}
'''

def sum_of_n_primes(n):
    sum = 0
    primes = first_n_primes(n)
    for i in range(len(primes)):
        sum += primes[i]
    return sum

print(sum_of_n_primes(4))

'''
function countScores(people) {
  const scoresObj = {};

  for (let i = 0; i < people.length; i += 1) {
    let personObj = people[i];
    let name = personObj.name;
    let score = personObj.score;

    if (scoresObj[name]) {
      scoresObj[name] += score;
    } else {
      scoresObj[name] = score;
    }
  }

  return scoresObj;
}
'''
peeps = [
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Dexter", "score": 2},
  {"name": "Mike", "score": 2},
  {"name": "Pete", "score": 2},
  {"name": "Dexter", "score": 2}
];

def count_scores(people):
    scores_obj = {}
    for i in range(len(people)):
        person_obj = people[i]
        name = person_obj["name"]
        score = person_obj["score"]
        if name in scores_obj: 
            scores_obj[name] += score
        else: 
            scores_obj[name] = score
    return scores_obj

print(count_scores(peeps))        