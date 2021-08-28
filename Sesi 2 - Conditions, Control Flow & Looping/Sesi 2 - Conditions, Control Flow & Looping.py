#Conditional


##Introduction to the if Statement
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')


##Grouping Statements: Indentation and Blocks
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')


# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


##The else and elif Clauses
###1
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


###2
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


###3
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")


###4
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")


###5
name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")


##6 (akan error)
# if 'a' in 'bar':
#     print('foo')
# elif 1/0:
#     print("This won't happen")
# elif var:
#     print("This won't either")


##One-Line if Statements
###1
if 'f' in 'foo': print('1'); print('2'); print('3')


###2
if 'z' in 'foo': print('1'); print('2'); print('3')

###3
x = 2

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


###4
x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


###5
x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')


##Conditional Expressions (Python’s Ternary Operator)
###1
raining = False
print("Let's go to the", 'beach' if not raining else 'library')


###2
raining = True
print("Let's go to the", 'beach' if not raining else 'library')


###3
age = 12
s = 'teen' if age < 21 else 'adult'
s


###4
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'


##The Python pass Statement
###akan error
# if True:

# print('foo')


##tidak error
if True:
    pass

print('foo')


#Python "while" Loops


###1
n = 5
while n > 0:
    n -= 1
    print(n)


###2
i = 1
while i < 6:
  print(i)
  i += 1


##The Python break and continue Statements
###1
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')


###2
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')


##The else Clause
###1
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')


###2
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')


##Infinite Loops
# while True:
#     print('foo')


##Nested while Loops
###1
# if age < 18:
#     if gender == 'M':
#         print('son')
#     else:
#         print('daughter')
# elif age >= 18 and age < 65:
#     if gender == 'M':
#         print('father')
#     else:
#         print('mother')
# else:
#     if gender == 'M':
#         print('grandfather')
#     else:
#         print('grandmother')


###2
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))


##One-Line while Loops
n = 5
while n > 0: n -= 1; print(n)


#The Python for Loop
###1
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)


###2
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)


###3
for k in d:
    print(d[k])


###4
for k in d.values():
    print(k)


###5
for k, v in d.items(): 
    print(k, ":", v) 


##The range() Function
for n in (0, 1, 2, 3, 4):
    print(n)

##The break and continue Statements
###1
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)


###2
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)


##The else Clause
###1
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute


###2
for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute


###Contoh Penggunaan 1
temp = input("Ketikan temperatur yang ingin dikonversi, eg. 45F, 120C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == "F":
    result = int(round((degree - 32) * 5 / 9))
else:
    print("Masukan input yang benar")

print("Temperaturnya adalah", result, "derajat")


###Contoh Penggunaan 2
while True:
    msg = input("Ketikan karakter: ").lower()
    print(msg)
    if msg == "stop":
        break
