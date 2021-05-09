import random
students=["saxona","bernette","emily","berkley"]
dict={stud:random.randint(1,100)  for stud in students}
print(dict)
d1={study : val  for (study,val) in dict.items() if val>25}
print(d1)
