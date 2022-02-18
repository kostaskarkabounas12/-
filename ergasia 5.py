from collections  import Counter
file = open("two_cities_ascii.txt", "r")
data = file.read()
A=data.lower()
words = A.split()
print('Number of words in text file :', len(words))
lista= A.split()
Counter = Counter(lista)
leksis= Counter.most_common(10)  
print(leksis)
prw2=[]
for i in range(len(words)):
    prwtoi2=words[i][0:2]
    prw2.append(prwtoi2)
from collections  import Counter
Counter = Counter(prw2)
prwt2= Counter.most_common(3)
print(prwt2)
prw3=[]
for i in range(len(words)):
    prwtoi3=words[i][0:23]
    prw3.append(prwtoi3)
from collections  import Counter
Counter = Counter(prw3)
prwt3= Counter.most_common(3)
print(prwt3)
