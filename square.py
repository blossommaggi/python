x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
s1=x2-x1
s2=y2-y3
s3=x3-x4
s4=y1-y4
if(s1==s2==s3==s4):
    print('yes')
else:
    print('no')
