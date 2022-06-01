#상하좌우 길찾기
#N x N 크기의 정사각형에서 가장 왼쪽위 좌표는 (1, 1), 가장 오른쪽 아래
#좌표는 (N, N)에 해당

n = 5 # int(input()) # 정사각형 크기
plans = ['R','R', 'R', 'U', 'D', 'D'] # input().split() # 여행계획

x, y = 1, 1 # 최초 시작점

# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_type = ['L', 'R', 'U', 'D']

for i in plans :
  for j in range(len(move_type)) :
    if i == move_type[j] :
      nx = x + dx[j]
      ny = y + dy[j]
  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue
  
  x, y = nx, ny
  
print(x, y)      

