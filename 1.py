# 파이썬 과제 1주차
#과제 1
korean = 80
english = 75
math = 55

print((korean + english + math)/3)

#과제 2

pin = "881120-1068234"
# code here

print(pin[0:6])
print(pin[7:14])
#과제 3
ls=[1 ,3 ,5 ,4 ,2]
# code here
ls.sort()
ls.reverse()
print (ls)

#과제 4
ls2 = ['life', 'is', 'too', 'short']
a = " ".join(ls2)
print (a)

#과제 5
a = b = [1, 2, 3]
a[1]=4
print(b)

# 첫번째 줄에서 a와b를 같다고 지정(a와 b에 따로따로 리스트를 지정하지 않음)
# 따라서 a를 변경하면 b도 같은 값이기 때문에 같이 변경됨  
