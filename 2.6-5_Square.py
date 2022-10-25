'''Task 2.6-5 Output a table of size n*n, filled with numbers from 1 to n^2 in a spiral coming out of the upper left corner and twisting clockwise'''
n=int(input())
a=[[0]*n for i in range(n)]
y,x,z=0,0,1
a[0][0]=z
while z<n**2:
    while 0==0: #fill to the right
        if x+1<n and a[y][x+1]==0:
            x+=1
            z+=1
            a[y][x]=z
        else:
            break
    while 0==0: #fill to the down
        if y+1<n and a[y+1][x]==0
            y+=1
            z+=1
            a[y][x]=z
        else:
            break
    while 0==0: #fill to the left
        if x-1>=0 and a[y][x-1]==0:
            x-=1
            z+=1
            a[y][x]=z
        else:
            break
    while 0==0: #fill to the up
        if y-1>=0 and a[y-1][x]==0:
            y-=1
            z+=1
            a[y][x]=z
        else:
            break
for i in range(n):
    print(*a[i])

