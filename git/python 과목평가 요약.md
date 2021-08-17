# python 과목평가 요약







## 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 `**`                                 `-3 ** 6 == ?`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`







- 문자열을 변환할 때, 문자열은 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안 됩니다.
  '1 + 2j'를 복소수로 변환해보고 오류를 확인해봅시다.

- 하나의 요소(값)로 구성된 tuple은 값 뒤에 쉼표를 붙여서 만듭니다.
- 빈 세트를 만들려면 `set()`을 사용해야 합니다. (`{}`로 사용 불가능) 
- 활용 가능한 연산자는 차집합(`-`), 합집합(`|`), 교집합(`&`)입니다.
- 앞으로 우리는 [PEP 8](https://www.python.org/dev/peps/pep-0008/#indentation)에서 권장하는 **4spaces**를 사용합니다.



## 변수(Variable)와 자료형(Data Type)[¶]

![variable](https://user-images.githubusercontent.com/9452521/87640197-55a7f280-c781-11ea-9cff-19c022ce704a.png)



![typecasting](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)

![container](https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png)



### 기본 인자 값 (Default Argument Values)

**함수를 정의할 때,** 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않도록하여, 정의된 것 보다 더 적은 개수의 인자들로 호출 될 수 있습니다.

- *주의\* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없습니다.

  ```python
  # 다음 코드를 실행해서 오류를 확인해봅시다.
  def greeting(name='john', age):
      return f'{name}은 {age}살입니다.'
  
  # 오류가 발생하지 않도록 아래에 직접 수정하고 실행해봅시다.
  def greeting(age, name = 'john'):
      return f'{name}은 {age}살입니다.'
  print(greeting(1))
  print(greeting(2, 'json'))
  ```

  

  

### 키워드 인자 (Keyword Arguments)

  **함수를 호출할 때** 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달할 수 있습니다.

- 단 아래와 같이 `키워드 인자`를 활용한 다음에 `위치 인자`를 활용할 수는 없습니다.

  ```python
  # 다음 코드를 실행해서 greeting 함수를 선언합니다.
  def greeting(age, name):
      return f'{name}은 {age}살입니다.'
  # 아래와 같이 키워드 인자를 사용해서 함수를 호출할 수 있습니다.
  greeting(name='철수', age=24)
  # 위치 인자와 함께 사용할 수 있습니다.
  greeting(24, name='철수')
  # 다음 코드를 실행해서 오류를 확인해봅시다.
  greeting(age=24, '철수')
  ```
  

### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 **함수를 정의할 때** 가변 인자 리스트`*args`를 활용합니다.

가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다.





### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

정해지지 않은 키워드 인자들은 **함수를 정의할 때** 가변 키워드 인자 `**kwargs`를 활용합니다.

가변 키워드 인자는 **`dict`** 형태로 처리가 되며, 매개변수에 `**`로 표현합니다.

```python
# 주의사항
# 식별자는 숫자만으로는 이루어질 수가 없습니다.(키워드인자로 넘기면 함수 안에서 식별자로 쓰이기 때문)
# 코드를 실행해서 오류를 확인해봅시다.
dict(1=1, 2=2) # X

# Key가 숫자인 딕셔너리를 만들고 싶다면, 아래와 같이 사용해야합니다.
dict([(1, 1), (2, 2)])
dict(((1,1), (2,2)))

# 아래의 코드를 실행시켜 kwargs가 딕셔너리로 처리되는 것을 확인해봅시다.
def my_dict(**kwargs):
    return kwargs

print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
```



## Object 중심의 장점

**<wikipedia - 객체지향 프로그래밍>**

> 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됩니다.
>
> 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
>
> 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있습니다.

- 코드의 **직관성**
- 활용의 **용이성**
- 변경의 **유연성**