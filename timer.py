import time        
def addzero(Number:int):
    if len(str(Number))==1:
        return f'0{Number}'
    else:
        return str(Number)


def string_to_time(my_time:str):
    my_list=[]
    s=''
    for i in range(0,len(my_time)):
        if my_time[i]==':':
            my_list.append(int(s))
            s=''
        elif i==len(my_time)-1:
            s+=my_time[i]
            my_list.append(int(s))
        if my_time[i]!=':':
            s+=my_time[i]
    return my_list

my_time=input('Insert time to countdown (h:m:s) without spaces ')
my_time_list=string_to_time(my_time)
hour=my_time_list[0]
minute=my_time_list[1]
second=my_time_list[2]
Seconds_all=second+(minute*60)+(hour*360)
for i in range(Seconds_all):
    print(f'{addzero(hour)} : {addzero(minute)} : {addzero(second)}')
    time.sleep(1)
    if second==0:
        second=60
        if minute>=1:
            minute-=1
    if minute==0:
        if hour>=1:
            hour-=1
            minute=59
    second-=1
