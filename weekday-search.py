import datetime

print('start year')
y_i=input()
print('end year')
y_f=input()
print('day')
d=input()
print('weekday')
wd=input()

for y in range(int(y_i),int(y_f)):
    for m in range(1,13):
        D = datetime.date(y,m,int(d))
        
        if D.weekday() == int(wd)-1:
            print(D.strftime("%Y%m%d"))
            
