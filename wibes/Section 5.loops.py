mark = int(input("Enter your mark"))
highest= 0
lowest = 0
count = 0
total = 0
while mark != -1:
    if mark > 100 and mark < 0:
        mark = int(input("Enter your mark"))
    else:
        total = total + mark
        count = count + 1    
        
        
     
    