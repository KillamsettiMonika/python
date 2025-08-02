import time

t=int(input("enter time in sexonds: "))
for x in range(t,0,-1):
    sec=x%60
    min=int(x/60)%60
    hour=int(x/3600)
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("time is up!")
