h="hello world"
#h='hello world'
#h="""hello world"""
#h='''hello world'''
print(h)
print(type(h))
#문자열 자료형=str=string
#여러 줄로 이루어진 문자열 = multiline

food='Python\'s favorite food is perl'
print(food)
say='"Python is very easy." he says.'
print(say)
#   >>> food="Python's favorite food is perl"
#   >>>     ='Python\'s favorite food is perl'
#if '백슬레쉬'' 또는 "백슬레쉬""를 쓰면 
#   백슬레시 바로 뒤에 오는 '"를 문자 그대로 독립적으로 표현시킴.
#   문자 백슬레쉬를 글자 그대로 표현하고 싶다면 \\
#   즉, 선행하는 백슬레쉬가 기능적 코드로 작용함
#   >>>say="\"Python is very easy.\"he says."
#   >>>   ='"Python is very easy." he says.'


n='Life is too short, \nYou need python.'
# \n = 문자열의 줄을 바꾼다는 의미 = enter 역할
# \f 도 \n과 동일한 역할을 수행함
# """"""이나 ''''''로 문자열 작성 시 내부에서 enter를 쳐도 성립.
# n='''Life is too short,
#    You need python'''
print(n)

t='Life is too short,\tYou need python.'
# \t = 문자열 사이에 탭 정도의 간격을 준다는 의미 = tab 역할
print(t)

b='Life \bi\bs\b t\bo\bo\b\b s\bh\bo\br\bt\b, You \bneed \bpython.'
# print(b) = print('Life, Youneedpython.')
# \b = 백스페이스 역할 = 출력
#  시 문자열 한 칸씩 지운다는 의미

a='\aLife is too short, You need python.'
# \a = alarm = 문자열 안에 속해있어야 하며, 
# print로 출력될 때 "띠링!"같은 기본 알림음이 같이 스피커로 출력된다. 
# print(a) = Life is too short, You need python.(띠링!)

null='null\000'
null2='\000null\000'
# Null[널]은 표현의 끝을 매듭지어 코드 상의 충돌을 방지 = 마침표 역할
# \000 = 숫자 0(ASCII값 0)을 의미. 출력되지 않지만 문자열 길이 1개가 추가됨. 
#      = C/C++에서의 \0
#      ≠ 문자 0 (ASCII값 48) 
#      ≠ 공백(스페이스 바)는 ASCII값 32
print(null)

print(null2)