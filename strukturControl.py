# contoh pernyataan if
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# Measure some strings:
words = ['cat','window','defenestrate']

for w in words:
    print(w,len(w))

# fungsi range
for i in range(5):
    print(i)

range(5,10)
range(0,10,3)
range(-10,-100,-30)

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])
# sum
sum(range(4))
# list
list(range(4))
