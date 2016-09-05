from sense_hat import SenseHat
from time import sleep
sense=SenseHat()


celsiusH = sense.get_temperature_from_humidity()
celsiusP = sense.get_temperature_from_pressure()
tempH = 9.0/5.0 * celsiusH + 32
tempP = 9.0/5.0 * celsiusP + 32
tempH = int(tempH)
tempP = int(tempP)
tempCombined = (tempP + tempH)/2


p = (102, 0, 204)
e = (0, 0, 0)
b = (0, 0, 255)
g = (0, 255, 0)
r = (255, 0, 0)
o = (255, 128, 0)
w = (255, 255, 255)
f = (255, 0, 255)
c = (0, 255, 255)
y = (255, 255, 0)



smallNum =

[b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,b,e,e,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,e,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,b,e,e,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,b,e,e,e,e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

[b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e],

frame10 = [e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame11 = [e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame12 = [e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,b,e,e,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame13 = [e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame14 = [e,e,e,e,b,e,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame15 = [e,e,e,e,b,b,b,e,e,e,e,e,b,e,e,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame16 = [e,e,e,e,b,b,b,e,e,e,e,e,b,e,e,e,e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame17 = [e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame18 = [e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

frame19 = [e,e,e,e,b,b,b,e,e,e,e,e,b,e,b,e,e,e,e,e,b,b,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,b,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

sense.clear()
A = map(int,str(tempCombined))
print A
B = A[:len(A)/2]
print B
C = A[len(A)/2:]
print C
running = True
while running:
    for x in range(0,9):
     if B==[x]:
         leftNum=frame + x

    for x in range(0,9):
     if C==[x]:
         for y in range(0,64):
          if leftNum[x]==b or RightNum[x]==b:
          DisplayNum.append(b)
         else:
          DisplayNum.append(e)
          RightNum=frame1 + x
    sense.clear
    running= False
    

print len(frame0)
DisplayNum=[]
for x in range(0,64):
     if leftNum[x]==b or RightNum[x]==b:
         DisplayNum.append(b)
     else:
         DisplayNum.append(e)
print DisplayNum
print len(DisplayNum)
sense.set_pixels(DisplayNum)

    
         

