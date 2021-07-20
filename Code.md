# Code



```python
n = int(input())
while n > 0:
    print(n % 10)
    n = n // 10
    
185
5
8
1    
```



```python
n = 0
total = 0
user_input = int(input('1부터 어디까지 더할까요? '))

while n < user_input:
    n += 1
    total += n
print(total)


1부터 어디까지 더할까요? 10
55
```



```python
user_input = ''
while user_input != '안녕':
    print('안녕?')
    user_input = input('말해봐 : ')
```



```python
for i in [1, 2, 3]:
    pass
else:
    pass

구조 기억
```



```python
numbers = range(1, 51)
numbers_list = list(numbers)
print(numbers_list[::2])
```



```python
n = 5
m = 9
for i in range(m):
    for j in range(n):
        print('*', end = '')
    print()
```



```python
N = int(input())

for i in range(1, 501):
    if N % i == 0:
        print(i)
```



```python
number = int(input())

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end = '')
    print()
```

