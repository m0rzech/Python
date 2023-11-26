from math import *

def main():
    w, h=80,40
    global list
    list=makeSurface(w, h)    
    
    fun(w,h)
    
def fun(w,h):        
    global list
    while True:        
        a=int(input("left limit: "))
        b=int(input("right limit: "))
        inp=input("type the function using x as unknown or type q to quit: ")
        
        if inp == 'q':
            break
            
        dict={}#x - key ; y - value
        min, max=0, 0 #min i max of the function will be used to scale y axis
        
        scale=(abs(a)+abs(b))
        dx=w/scale
        ox=(w/2)
        x=float(a)
        step=(abs(a)+abs(b))/float(w)
    
        try:
            while x<=b:# loop in which min, max and value of function for each step is calculated
                try:
                    y=eval(inp)
                except ZeroDivisionError as err:
                    x+=step    
                    continue
                    
                if y<min:
                    min=y
                if y>max:
                    max=y            
                dict[x]=y
                x+=step            
        except :
            print('Incorrect format of function')
            continue
        
        scale=abs(min)+abs(max)#the scope between the min and max VALUES of the function on the drawn interval
        oy=h/2#the middle of coordinate system
        if scale<h:#then scaling makes sense, otherwise scaling flattens the chart which might result in printing x**2 function as straight line
            dy=h/scale#scale factor   
        else:
            dy=1
            
        x=float(a)          
        while x<b:# actual drawing        
            x1=int(x*dx)+ox
            try:
                y=(-dict[x]*dy)+oy        
            except KeyError as err:
                x+=step
                continue
            if 0<=y<h and x1<w: #y<h and y>=0:#checking limits if there was no scaling
                                #checking x1 in case of limits value were a=0 b=...
                print (f'x: {x1} y: {y}')
                list[int(y)][round(x1)]="*"    
            x+=step    
        printL(list)
        del list[:]# clear up memory
        list=makeSurface(w, h)#drawing a coordinate system

            
            
def printL(n):
    print("")
    line=""
    for i in n:
        line=""
        for j in i:
            line+=str(j)
        print(line)
        
def makeSurface(w, h):    
    list=[[" "] * w for i in range(h)]    
    for i in range(h):
        list[i][round(w/2)]="|"
    for i in range(w):
        list[round(h/2)][i]="-"
    return list
    
if __name__ == "__main__":
    main()