head='Python'
tail=' is fun!'
print(head+tail)
print((head+tail)*2+"\n")
# 연결 / 연속 / 연쇄 = Concatenation [kənˌkætəˈneɪʃn] 

print(head[0])
print(head[1])
print(head[-1])
print(head[-2]+"\n")
# [] = 대괄호 square bracket 
#    = Indexing = 데이터 위치 정보.
#    = 파이썬에서 데이터의 첫 번째 위치는 0이다. 즉, 0부터 세기 시작한다.  
#      반대로 끝에서 첫 번째 위치는 -1이다. 음수는 역방향으로 세기 시작한다.

print(head[0:6])
# [N1:N2] = N1이상부터 시작하거나:N2미만까지의 범위
#         = N1의 첫 번째 위치는 0 이지만,
#           N2가 마지막 위치를 포함시키는 위치의 수는 
#           정방향 마지막 위치+1 또는 문자열 총 갯수와 같다. 
print(head[4:])
print(head[-4:]+"\n")

print(head[:4])
print(head[:-4]+"\n")

print(head[::3])
print(head[::2]+"\n")
# N1:N2:N = Slicing(슬라이싱) = 조각, 부분 범위
#         = N1이상부터 시작하거나:N2미만까지의 범위에서:N칸번째씩