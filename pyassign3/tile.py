#!/usr/bin/env python3

"""tile.py: .

__author__ = "Huruihua"
__pkuid__  = "1800011843"
__email__  = "1800011843@pku.edu.cn"
"""

a = int(input("请输入墙的长度a:"))
# input the length of the wall

b = int(input("请输入墙的宽度b:"))
# input the width of the wall

c = int(input("请输入瓷砖的长度c:"))
# input the length of the tile

d = int(input("请输入瓷砖的宽度d:"))
# input the width of the tile
 

wall= [0]*(a*b)
#墙的二维坐标
answers = []
#铺法


def whether_paved(i,j,c,d):
#检查该位置起铺砖能不能成功，如果能铺，返回True
    for m in range(i,i+c):
        for n in range(j,j+d):
            if m >= a or n >= b:
            #检查是否越界，如果越界，则返回False
                return False
            number = m*b + n  
            #记录编号
            if wall[number] == 1:
            #1为已铺过，如果已铺过，则返回False
                return False
    return True       
  

def paving_tiles(nowans,i,j,c,d,value):
#当前位置铺砖/拆砖，value == 1 铺砖，value == 0 拆砖
    attempt = []
    
    for m in range(i,i+c):
        for n in range(j,j+d):
            number = m*b + n 
            wall[number] = value
            attempt.append(number)
            
    if value == 1:
        nowans.append(attempt)
    else:
        nowans.remove(attempt)
    

def paving_next_tile(nowans,i,j):
#从当前位置开始铺砖   
    if i == a-1 and j == b:
        #如果已经到结尾，则输出
        print(nowans)
        answers.append(nowans.copy())
        return
    
    elif j == b:
        #如果非最后一行结尾，则从下一行的开始铺
        paving_next_tile(nowans,i+1,0)
        return
    
    if wall[i*b + j] == 1:
        #如果该位置已经被铺了，则铺下一块
        paving_next_tile(nowans,i,j+1)
        return
    
    if whether_paved(i,j,c,d):
        #如果可以横着铺砖，则开始横铺
        paving_tiles(nowans,i,j,c,d,1)
        paving_next_tile(nowans,i,j+d)
        paving_tiles(nowans,i,j,c,d,0)
        
    if c != d and whether_paved(i,j,d,c):
        #如果砖不是正方形且可以竖铺，则开始竖铺
        paving_tiles(nowans,i,j,d,c,1)
        paving_next_tile(nowans,i,j+c)
        paving_tiles(nowans,i,j,d,c,0)
    
    return


def drawing(step):
    import turtle
    wn = turtle.Screen() 
    
    #定义画笔，选择其中一种方案
    t = turtle.Pen()
    t.penup()
    t.speed(0)
    step = 0
    
    n = int(turtle.numinput('选择一种要画的方案','最小值=0,最大值='+str(len(answers)-1),\
                            default=None,minval=0,maxval=len(answers)-1))
    
    #计算格子位置，画出方格并标号
    l1 = -(d+1)//2
    l2 = -d//2+20*d+1
    r1 = -(c+1)//2
    r2 = -c//2+20*c+1
    for y in range(l1,l2,20):
        for x in range(r1,r2,20):
            if step < 10:
                t.goto(x+8,y+2)
                t.write(step)
            else:
                t.goto(x+5,y+2)
                t.write(step)
            #在格子合适位置处标数字
            t.goto(x,y)
            t.pendown()
            t.forward(20)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.penup()
            step = step +1
                
    yourchioce = eval(answers[n]) 
    colors = ["bisque","goldenrod","lightseagreen","firebrick","peru","chocolate"]
    k = 0
    for i in yourchioce:
        #遍历所选方案中的砖块位置
        for j in i:
            #将同一块砖涂上同样的颜色
            if j == step:
                t.color(colors[k])
                t.begin_fill()
                drawing(j)
                t.end_fill()
            if k > 6:
                k = 0
            else:
                k = k+1
            
            #涂色失败,想不出能将涂色序号和砖块位置联系在一起的方法，只能单一画图或者画一个正方形涂一种色
            
                       
        
def main():
    paving_next_tile([],0,0)
    print(len(answers))   
    drawing(len(answers))       
    
if __name__ == '__main__':
    main()

