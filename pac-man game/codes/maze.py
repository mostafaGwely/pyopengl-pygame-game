from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time  import sleep
import  random  
import sys
from sound import *
from funcs import *
from tex import *
import pygame


score=0
dx =.1       #change in x of monsters
dy= .1       #change in y f monsters
x =.5     #x of red monster
y = -.35  #y of red monster
top = right = left = bottom =textureLeft=textureRight=textureTop=textureBottom = 0 #flags 
xpacman  = -1.05
ypacman=.35  
x2 =-.2   #x of blue monster
y2 = .15  #y of blue monster
binkMonsterX =.0 
binkMonsterY = .18 
yallowMonsterX =.0
yallowMonsterY = 0
cheeseList = [(-1.2, 0.35), (-1.0999999999999999, 0.35), (-0.9999999999999998, 0.35), (-0.8999999999999997, 0.35), (-0.7999999999999996, 0.35), (-0.6999999999999995, 0.35), (-0.5999999999999994, 0.35), (-0.49999999999999933, 0.35), (-0.39999999999999925, 0.35), (-0.29999999999999916, 0.35), (-0.19999999999999907, 0.35), (-0.09999999999999898, 0.35), (1.1102230246251565e-15, 0.35), (0.1000000000000012, 0.35), (0.2000000000000013, 0.35), (0.3000000000000014, 0.35), (0.40000000000000147, 0.35), (0.5000000000000016, 0.35), (0.6000000000000016, 0.35), (0.7000000000000017, 0.35), (0.8000000000000018, 0.35), (0.9000000000000019, 0.35), (1.000000000000002, 0.35), (1.100000000000002, 0.35), (1.2000000000000022, 0.35), (-1.2, 0.15), (-1.0999999999999999, 0.15), (-0.7999999999999996, 0.15), (-0.6999999999999995, 0.15), (-0.5999999999999994, 0.15), (-0.49999999999999933, 0.15), (-0.39999999999999925, 0.15), (-0.29999999999999916, 0.15), (-0.19999999999999907, 0.15), (-0.09999999999999898, 0.15), (1.1102230246251565e-15, 0.15), (0.1000000000000012, 0.15), (0.2000000000000013, 0.15), (0.3000000000000014, 0.15), (0.40000000000000147, 0.15), (0.5000000000000016, 0.15), (0.8000000000000018, 0.15), (0.9000000000000019, 0.15), (1.000000000000002, 0.15), (1.100000000000002, 0.15), (1.2000000000000022, 0.15), (-0.8399999999999996, 0.02), (-0.7799999999999996, 0.02), (0.1000000000000012, -0.05), (0.2000000000000013, -0.05), (0.3000000000000014, -0.05), (0.40000000000000147, -0.05), (0.5000000000000016, -0.05), (-1.2, -0.15), (-1.0999999999999999, -0.15), (-0.9999999999999998, -0.15), (-0.8999999999999997, -0.15), (-0.7999999999999996, -0.15), (-0.6999999999999995, -0.15), (-0.5999999999999994, -0.15), (-0.49999999999999933, -0.15), (-0.39999999999999925, -0.15), (-0.29999999999999916, -0.15), (-0.19999999999999907, -0.15), (-0.09999999999999898, -0.15), (1.1102230246251565e-15, -0.15), (0.6000000000000016, -0.15), (0.7000000000000017, -0.15), (0.8000000000000018, -0.15), (0.9000000000000019, -0.15), (1.000000000000002, -0.15), (1.100000000000002, -0.15), (1.2000000000000022, -0.15), (-1.2, -0.25), (0.1000000000000012, -0.25), (0.2000000000000013, -0.25), (0.40000000000000147, -0.25), (0.5000000000000016, -0.25), (1.2000000000000022, -0.25), (-1.2, -0.35), (-1.0999999999999999, -0.35), (-0.9999999999999998, -0.35), (-0.8999999999999997, -0.35), (-0.7999999999999996, -0.35), (-0.6999999999999995, -0.35), (-0.5999999999999994, -0.35), (-0.49999999999999933, -0.35), (-0.39999999999999925, -0.35), (-0.29999999999999916, -0.35), (0.1000000000000012, -0.35), (0.2000000000000013, -0.35), (0.3000000000000014, -0.35), (0.40000000000000147, -0.35), (0.5000000000000016, -0.35), (0.6000000000000016, -0.35), (0.7000000000000017, -0.35), (0.8000000000000018, -0.35), (0.9000000000000019, -0.35), (1.000000000000002, -0.35), (1.100000000000002, -0.35), (1.2000000000000022, -0.35), (-0.85, 0.09)]

redMonsterRandDir = redMonsterRandFunc()
blueMonsterRandDir= blueMonsterRandFunc()
binkMonsterRandDir= binkMonsterRandFunc()
yallowMosterRandDir = yallowMonsterRandFunc()
tex_id=[]
def init(): 
    ###############################
    global tex_id
    tex_id=glGenTextures(5)
    pacman_t=tex(tex_id[0]) #pacman
    pacman_t.load( "Pacman_HD.png")

    pink_monster=tex(tex_id[1])  #pink monster
    pink_monster.load("Pinky.png")

    red_monster=tex(tex_id[2])  #red monster
    red_monster.load("red.png")

    blue_monster=tex(tex_id[3])  #blue
    blue_monster.load("blue.png")

    yellow_monster=tex(tex_id[4])  #yellow monster
    yellow_monster.load("yellow.png")
    ####################################################
    glClearColor(1.0, 1.0, 1.0, 0) 
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    glOrtho(-1.3, 1.3, -.5 , .5 , 0 , 1) # l,r,b,t,n,f
    glMatrixMode (GL_MODELVIEW)
    
    glEnable(GL_TEXTURE_2D)    #enable textures
 



def keyboard(key, x, y):
    global  top , right ,left,bottom
    global xpacman ,ypacman,textureLeft,textureRight,textureTop,textureBottom
    if key == GLUT_KEY_UP:
        top = 1
        right = 0
        left = 0
        bottom = 0
        textureTop = 1 
        textureLeft = 0 
        textureRight = 0 
        textureBottom = 0 

    if key == GLUT_KEY_DOWN:
        top = 0
        right = 0
        left = 0
        bottom = 1
        textureTop = 0 
        textureLeft = 0 
        textureRight = 0 
        textureBottom = 1 
        
        # Rotate the cube
    if key == GLUT_KEY_LEFT:
        top = 0
        right = 0
        left = 1
        bottom = 0
        textureTop = 0
        textureLeft = 1 
        textureRight = 0 
        textureBottom = 0 
        
    if key == GLUT_KEY_RIGHT:
        top = 0
        right = 1
        left = 0
        bottom = 0
        textureTop = 0
        textureLeft = 0 
        textureRight = 1 
        textureBottom = 0 
        
        # Toggle the surface
    #glutPostRedisplay()
#############################################
def drawText(string, x, y):
        glLineWidth(3)
        glColor(0,0,0)  
        glLoadIdentity()
        glTranslate(x,y,0)
        glScale(.0005,.0005,0)
        string = string.encode() 
        for c in string:
                glutStrokeCharacter(GLUT_STROKE_ROMAN , c )

def display():
   global tex_id
   global score
   global x,y,dx,dy,xpacman ,ypacman,redMonsterRandDir,right,left,top,bottom,x2,y2,blueMonsterRandDir,result3,binkMonsterRandDir,yallowMosterRandDir
   global yallowMonsterX,yallowMonsterY,binkMonsterX,binkMonsterY,textureLeft,textureRight,textureTop,textureBottom
  
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity()
   glMatrixMode(GL_MODELVIEW)    
   glLoadIdentity()
   glColor(1,0,0)    #blue for frames and maze
   glLineWidth(3)
   frame(1)      #upper frame
   frame(-1)     #lower frame
   G()           #G letter
   O(0,0,0)        #outer left o
   O(.05,.05,0)        #insid left o
   glTranslate(-.3,0,0)
   O(0,0,0)        #outer left o
   O(.05,.05,0)        #insid left o
   
   
   glLoadIdentity()
   l()
   glTranslate(0,0,0)
   E()
   thin_rect()
   glLoadIdentity()
   small_rect(1,1)    #top left
   small_rect(-1,1)   #bottom left
   
   glTranslate(.9,-.5,0) #under l&e
   glScale(.6,1,1)
   thin_rect(.41)

   
   glLoadIdentity()    #set the matrix of model view (don't effect on glColor)
   T()
   glScale(2,1,1)
   glTranslate(.05,0,0)
   AA(.1)
   glLoadIdentity()
   glScale(2,1,1)
   glTranslate(-.1,0,0)
   AA(.1)
   
   glLoadIdentity()     #above E
   glTranslate(1.15,0,0) 
   glScale(.7,1,1)
   thin_rect(0)

   glLoadIdentity()        #wwwwww
   glTranslate(.6,-.2,0)
   thin_rect(-.1)

   glLoadIdentity()        #  above wwwwww
   glTranslate(.6,0,0)
   thin_rect(-.1)

   glLoadIdentity()       
   glTranslate(-.65,-.5,0)
   glScale(.7,1,1)
   thin_rect(.07) # the left boootom
################################################################################################################
   string="score : "+str(score)    
   drawText(string,-1.25,.45)     #draw string of score
   ###################################################33
   
   ##############draw cheese##############
   #glBindTexture(GL_TEXTURE_2D,0)    #solve the problem of changing color during use textures but it write before every polygon
   glLoadIdentity()
   drawCheese(cheeseList)       
   ################################################start of drawing monsters#######################################
   glLoadIdentity()
   glColor(1,1,1)
   glTranslate(.05+x,0+y,0)
   glTranslate(-.045, -.045, 0)
   glScale(.09, .09, 0)
   rect(tex_id[2], 0, 0, 1, 1)    #red monster


##################################################
  # glColor(1,1,1)
   glLoadIdentity()
   glTranslate(.05+x2,0+y2,0)
   glTranslate(-.045, -.045, 0)
   glScale(.09, .09, 0)
   rect(tex_id[3], 0, 0, 1, 1)    #blue monster          
  ##########################
   glColor(1,1,1)
   glLoadIdentity()
   glTranslate(.05+binkMonsterX,0+binkMonsterY,0)  
   glTranslate(-.045, -.045, 0)
   glScale(.09, .09, 0)
   rect(tex_id[1], 0, 0, 1, 1) #pink monster
  ####################
   glColor(1,1,1)
   glLoadIdentity()
   glTranslate(.05+yallowMonsterX,0+yallowMonsterY,0)   #coordinates make it move(translate)
   glTranslate(-.045, -.045, 0)
   glScale(.09, .09, 0)
   rect(tex_id[4], 0, 0, 1, 1)    #yellow monster
#####################################################################end of drawing monsters############################
#######################start drawing and motion of picman################################3   
   glLoadIdentity()
   glTranslate(xpacman ,ypacman,0)  #make pacman move (translate) by using its pacman
   glTranslate(-.045,-.045,0)
   glScale(.09,.09,0)
#################start of >>change the mouse of the pacman according to the pressed arraw####### 
   if textureRight ==1:
   		rect(tex_id[0], 0, 0, 1, 1)   #mouth toward right
   elif textureLeft == 1 :
   		rectl(tex_id[0], 0, 0, 1, 1)  #mouth toward left
   elif textureBottom == 1 :
   		rectb(tex_id[0], 0, 0, 1, 1)  #mouth toward bottom
   elif textureTop == 1 :           #mouth toward right
   		rectt(tex_id[0], 0, 0, 1, 1)
   else:
   		rect(tex_id[0], 0, 0, 1, 1)  #mouth toward left(defult)
#end of >> change the mouse of the pacman according to the pressed arraw 
   
  ##################start of checking on motion of pacman##################################3 	   	
   if right==1:   #right motion
	    if rightCheck(leftLista,xpacman -0.05,ypacman) == True:
    		xpacman  = xpacman  + .05
    		right = 0       #to move by only step 
   if left==1:
   		if leftCheck(rightlista,xpacman -0.05,ypacman) == True:
   			xpacman  = xpacman  - .05
   			left = 0        #to move by only step
   if top ==1:
   		if topCheck(bottomlista,xpacman -0.05,ypacman) == True:
   			ypacman  = ypacman + 0.05
   			top = 0      #to move by only step
   if bottom ==1:
   		if bottomCheck(toplista,xpacman -0.05,ypacman) == True:
   			ypacman  = ypacman - .05
   			bottom = 0   #to move by only step
#######################################################################

#############conditions of random motion of pacman######################
   if redMonsterRandDir==1:
   	if rightCheck(leftLista,x-.05,y) == True:
   		x = x + dx/100.0
   	else:
   		redMonsterRandDir = redMonsterRandFunc()
   if redMonsterRandDir==2:
   	if leftCheck(rightlista,x,y) == True:
   		x = x - dx/100.0
   	else:
   		redMonsterRandDir = redMonsterRandFunc()
   if redMonsterRandDir ==3:
   	if topCheck(bottomlista,x,y-0.01) == True:
   		y  = y + dy/100.0
   	else:
   		redMonsterRandDir = redMonsterRandFunc()
   if redMonsterRandDir ==4:
   	if bottomCheck(toplista,x,y+0.01) == True:
   		y  = y - dy/100.0
   	else:
   		redMonsterRandDir = redMonsterRandFunc()

###########red
   if blueMonsterRandDir==1 :
   	if rightCheck(leftLista,x2-.05,y2) == True:
   		x2 = x2 + dx/100.0
   	else:
   		blueMonsterRandDir = blueMonsterRandFunc()
   if blueMonsterRandDir==2:
   	if rightCheck(rightlista,x2,y2) == True:
   		x2 = x2 - dx/100.0
   	else:
   		blueMonsterRandDir = blueMonsterRandFunc()
   if blueMonsterRandDir ==3:
   	if topCheck(bottomlista,x2,y2-0.01) == True:
   		y2  = y2 + dy/100.0
   	else:
   		blueMonsterRandDir = blueMonsterRandFunc()
   if blueMonsterRandDir ==4:
   	if bottomCheck(toplista,x2,y2+0.01) == True:
   		y2  = y2 - dy/100.0
   	else:
   		blueMonsterRandDir = blueMonsterRandFunc()

#################################################################################################
#the start of the bink monster movement conditions
   if binkMonsterRandDir==1:
   	if rightCheck(leftLista,binkMonsterX-.05,binkMonsterY) == True:
   		binkMonsterX = binkMonsterX + dx/100.0
   	else:
   		binkMonsterRandDir = binkMonsterRandFunc()
   if binkMonsterRandDir==2:
   	if leftCheck(rightlista,binkMonsterX,binkMonsterY) == True:
   		binkMonsterX = binkMonsterX - dx/100.0
   	else:
   		binkMonsterRandDir = binkMonsterRandFunc()
   if  binkMonsterRandDir==3:
   	if topCheck(bottomlista,binkMonsterX,binkMonsterY-0.01) == True:
   		binkMonsterY  = binkMonsterY + dy/100.0
   	else:
   		binkMonsterRandDir = binkMonsterRandFunc()
   if binkMonsterRandDir ==4:
   	if bottomCheck(toplista,binkMonsterX,binkMonsterY+0.01) == True:
   		binkMonsterY  = binkMonsterY - dy/100.0
   	else:
   		binkMonsterRandDir = binkMonsterRandFunc()
#the end  of the bink monster movement conditions
#################################################################################################
#the start of the yallow monster movement conditions
   if yallowMosterRandDir==1:
   	if rightCheck(leftLista,yallowMonsterX-.05,yallowMonsterY) == True:
   		yallowMonsterX = yallowMonsterX + dx/100.0
   	else:
   		yallowMosterRandDir= yallowMonsterRandFunc()
   if yallowMosterRandDir==2:
   	if leftCheck(rightlista,yallowMonsterX,yallowMonsterY) == True:
   		yallowMonsterX = yallowMonsterX - dx/100.0
   	else:
   		yallowMosterRandDir = yallowMonsterRandFunc()
   if yallowMosterRandDir ==3:
   	if topCheck(bottomlista,yallowMonsterX,yallowMonsterY-0.01) == True:
   		yallowMonsterY  = yallowMonsterY + dy/100.0
   	else:
   		yallowMosterRandDir = yallowMonsterRandFunc()
   if yallowMosterRandDir ==4:
   	if bottomCheck(toplista,yallowMonsterX,yallowMonsterY+0.01) == True:
   		yallowMonsterY  = yallowMonsterY - dy/100.0
   	else:
   		yallowMosterRandDir = yallowMonsterRandFunc()
#the end  of the yallow monster movement conditions
###########################################################################################################################
#the begin of cheese collisions
   
   cheeseListcopy = cheeseList[:]
   for j in range(len(cheeseListcopy)):
     if cheeseListcopy[j][0]+.025 >= xpacman -0.02 >= cheeseListcopy[j][0]-.025 and ypacman-0.05<=cheeseListcopy[j][1]<=ypacman+0.05 :
        
          score+=1
          eat()
          del cheeseList[j]
          #break  #to solve the problem of out of index without using copy of list
   #check if the cheese has been moved
     if len(cheeseList)==0:
        bye() #play the bye bye music 
#the end of cheese collisions
###########################################################################################################################
#the collision of the monster and pacman 

   if (xpacman +.051 >= yallowMonsterX+.081 >= xpacman -.051 and ypacman+.081>=yallowMonsterY>=ypacman-.081) or(xpacman +.051 >= yallowMonsterX >= xpacman -.051 and ypacman+.081>=yallowMonsterY>=ypacman-.081) :
    bye()
   if (xpacman +.051 >= binkMonsterX+.081 >= xpacman -.051 and ypacman+.081>=binkMonsterY>=ypacman-.081) or(xpacman +.051 >= binkMonsterX >= xpacman -.051 and ypacman+.081>=binkMonsterY>=ypacman-.081) :
    bye()
   if (xpacman +.051 >= x2+.081 >= xpacman -.051 and ypacman+.081>=y2>=ypacman-.081) or(xpacman +.051 >= x2 >= xpacman -.051 and ypacman+.081>=y2>=ypacman-.081) :
    bye()
   if (xpacman +.051 >= x+.081 >= xpacman -.051 and ypacman+.081>=y>=ypacman-.081) or(xpacman +.051 >= x >= xpacman -.051 and ypacman+.081>=y>=ypacman-.081) :
    bye()
#end of the collisions pacman with monsters
###########################################################################################################################

   glutSwapBuffers()



    
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(1000, 400)
glutCreateWindow(b'MAZE')
glutDisplayFunc(display) 
glutSpecialFunc(keyboard)
glutIdleFunc(display)
init() # Any function name for initialization

glutMainLoop()
