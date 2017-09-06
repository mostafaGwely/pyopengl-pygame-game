
import numpy as np
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from cheese import *

def init(): 
   glClearColor(1.0, 1.0, 1.0, 0) 
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   glOrtho(-1.3, 1.3, -.5 , .5 , 0 , 1) # l,r,b,t,n,f
   glMatrixMode (GL_MODELVIEW)


def frame(TY=1):
   glLoadIdentity()
   glColor(0,0,1)
   glBegin(GL_LINE_STRIP)
   glVertex(-1.25,TY*.05)
   glVertex(-1.1,TY*.05)
   glVertex(-1.1,TY*.1)
   glVertex(-1.25,TY*.1)
   
   glVertex(-1.25,TY*0.4)
   glVertex(1.25,TY*.4)
   
   glVertex(1.25,TY*.1)
   glVertex(1.1,TY*.1)
   glVertex(1.1,TY*.05)
   glVertex(1.25,TY*.05)
   glEnd()
def G():
   glBegin(GL_LINE_LOOP)
   glVertex(-.6,.3)
   glVertex(-1,0.3)
   glVertex(-1,-.1)
   glVertex(-.6 ,-.1)
   
   glVertex(-.6 ,0.1)
   glVertex(-.8 ,0.1)
   glVertex(-.8 ,.07)
   glVertex(-.7 ,.07)
   
   glVertex(-.7,-.03) 
   glVertex(-.9 ,-.03)  
   
   glVertex(-.9 ,.2)
   glVertex(-.6 ,.2) 
   glEnd()





def O(TX=0,TY=0,TO=0):
   glBegin(GL_LINE_LOOP)    #negative TX,TY added to POSIVTIVE x,y 
   glVertex(-.2+TX,.1-TY)   #to obtain inside o and viceversa
   glVertex(0-TX ,.1-TY)
   glVertex(0-TX,-.1+TY+TO)    #TO MAkes  lower y equals zero
   glVertex(-.2+TX,-.1+TY+TO)
   glEnd()
   
def l():
   glBegin(GL_LINE_LOOP)
   glVertex(.6,.3)
   glVertex(.7 ,0.3)
   glVertex(0.7 ,-.1)
   glVertex(.6 ,-.1)
   glEnd()
def E():
   glBegin(GL_LINE_LOOP)
   glVertex(.8,.1)
   glVertex(1 ,0.1)
   glVertex(1 ,.03)
   glVertex(.84 ,.03)
   glVertex(.84,-.07)
   glVertex(1 ,-0.07)
   glVertex(1 ,-.1)
   glVertex(.8,-.1)
   glEnd()
   
   glLineWidth(4)
   
   glBegin(GL_LINE_LOOP)
   glVertex(.86,.08)
   glVertex(.96 ,.08)
   glVertex(.96,.05)
   glVertex(.86 ,.05)
   glEnd()
   
def thin_rect(TX=0):      #used to draw g and rects
   glBegin(GL_LINE_LOOP)
   glVertex(-.5,.3)
   glVertex(0+TX ,.3)
   glVertex(0+TX,.2)
   glVertex(-.5 ,.2)
   glEnd()

def small_rect(TY=1,TX=1):      #used to draw very small rects
   glBegin(GL_LINE_LOOP)
   glVertex(-1.15*TX,.3*TY)
   glVertex(-1.1 *TX,.3*TY)
   glVertex(-1.1*TX,.2*TY)
   glVertex(-1.15 *TX,.2*TY)
   glEnd()

def T():                   #under www
   glBegin(GL_LINE_LOOP)
   glVertex(.1,-.1)
   glVertex(.5 ,-.1)
   glVertex(.5 ,-.2)
   glVertex(.35 ,-.2)
   glVertex(.35 ,-.3)
   glVertex(.25,-.3)
   glVertex(.25 ,-.2)
   glVertex(.1 ,-.2)
   glVertex(.1,-.1)
   glEnd()

def AA(TY=0):               #used to draw under o
   glBegin(GL_LINE_LOOP)
   glVertex(-.2,-.2)
   glVertex(0 ,-.2)
   glVertex(0,-.4+TY)
   glVertex(-.2 ,-.4+TY)
   glEnd()



listx=[[],[],[],[],[],[],[],[],[]]
def draw_circle(r=1,x0=0,y0=0):
    #glColor(0,0,1)
    glBegin(GL_POLYGON)
    for theta in  np.arange(0,2*pi,0.1):
        x=x0+r*cos(theta)
        y=y0+r*sin(theta)
        glVertex2d(x,y)
    glEnd()
    
count=1    #because we draw indvidual piece of cheese 
##########################################################################################################################################   
def cheese2():
   global count  #"count" represents the number of cheese in maze
   global listx
   glLoadIdentity()
   #1
   for dx in  np.arange(-1.20,1.25,0.1) :#frist row of cheese f
        #draw_circle(.019,dx,.35)    #dx represents the coordinate of x of center 
        count+=1                    # for piece because the default of center equals zero
        listx[0].append(dx)
      
   #2
   for dx in  np.arange(-1.20,1.25,0.1) : #second row of cheese
          if (dx>=.75) or (dx<=.6 and dx>.1) or (dx<=0.01 and dx>=-.5) or(dx<=-.55 and dx>=-.85)or (dx<-1):
             #draw_circle(.019,dx,.15)
             count+=1
             listx[1].append(dx)
   ####  3   #### third row of cheese##############        
   #inside G
   for dx in  np.arange(-1.20,1.25,0.06) :   
          if  (dx>=-.88 and dx<-.72):
             draw_circle(.019,dx,.02)
             count+=1
             listx[2].append(dx)
             
   draw_circle(.019,-.85,.09)    #individual point inside G

   #under g
   for dx in  np.arange(-1.20,1.25,0.1) :
          if  (dx<=.6 and dx>.06):
             draw_circle(.019,dx,-.05)
             count+=1
             listx[3].append(dx)

   #inside e
   for dx in  np.arange(-1.20,1.25,0.1) :
          if  (dx>=.84 and dx<1.1):
             draw_circle(.019,dx,-.02)
             count+=1
             listx[4].append(dx)
   #########################################      
   
   #4
   for dx in  np.arange(-1.20,1.25,0.1):  #forth row of cheese
        if (dx>.55 or dx<=.1):
           draw_circle(.019,dx,-.15)
           count+=1
           listx[5].append(dx)

   
   #5
   for dx in  np.arange(-1.20,1.25,0.1) :  #fifth row of cheese
          if  (dx>=-1.25 and dx<-1.15)  or (dx>= -.59 and dx <=-.5)or (dx >=-.29 and dx <= -.2) or (dx>=0.01and dx<= .25) or (dx>=.35 and dx<=.6)or(dx>=1.01 and dx<=1.1)or(dx>=1.15 and dx<=1.25):
             draw_circle(.019,dx,-.25)
             count+=1
             listx[6].append(dx)
   #6          
   for dx in  np.arange(-1.20,1.25,0.1): #the last row of cheese
        if (dx>=.06 or dx<=-.2):
           draw_circle(.019,dx,-.35)
           count+=1
           listx[7].append(dx)
   listx[8].append(-.85)
   return count,listx
   ################################################################################################################3

def counter():  #to know the number of cheese
   c,m=cheese2()   #write it outside the display because every time
   #print(m)  #display will run it & changes count as it is added the last value of "count" to it"co.." from the previous display to the current
#c,m=cheese2()
def drawText(string, x, y):
        glLineWidth(5)
        glColor(1,0,0)  
        glLoadIdentity()
        glTranslate(x,y,0)
        glScale(.0005,.0005,0)
        string = string.encode() 
        for c in string:
                glutStrokeCharacter(GLUT_STROKE_ROMAN , c )

key_1=0
key_2=0
def arrow_keys(key,x,y):

    global key_1
    global key_2
    if (key==100 and key_1>=-1.25+.04*2):            #left arrow
        key_1-=.08
    if (key==102 and key_1<1.25-.04*2):                #right arrow
        key_1+=.08

        
    if (key==103 and key_2>=-.4+.04):            #bottom arrow
        key_2-=.08
    if (key==101 and key_2<.4-.04):                #top arrow
        key_2+=.08
 




score=0

listy=[.35,.15,.02,-.05,-.02,-.15,-.25,-.35,.09]   #coordinates for rows of cheese
"""def score(x,y):
   global listx
   global score
   global listy
   for y  in listy:
      i=listy.index(y)
      for x  in listx[i]:
         if (.04-.019)**2<= (x-xo)**2+(y-yo)**2 <(.04+.019):
            score+=1      #function to write the new score
            color(1,1,1)           #to erase 
            draw_circle(.019,xo,y)
            listx[i].remove(xo)   #to remove the xo of cheese that was removed
            print(score)"""
def cheese():
   global listx
   global listy
   global key_1
   global key_2
   for y in listy: 
        i=listy.index(y)
        if listx[i]==[]:
           listy.remove(y)
        else:
           for x in listx[i]:
              if x+.019>=key_1-.05>=x-.019:
                 j=listx[i].index(x)
                 del listx[i][j]
                                                                     
                 score+=1
              draw_circle(.019,x,listy[i])
"""

def cheese():
   global listx
   global listy
   global key_1
   global key_2
   global score
   for i in range(0,8):                                                   #for y in listY:
      for x in listx[i]:                                                    #i=listy.index(y)
                                                                            #if list[i]==[]:
                                                                              #listy.remove(y)
        if (.04-.019)**2<= (key_1-x)**2+(key_2-listy[i])**2 <(.04+.019):    #else:
               x=x+1000                                                       #for x in listx[i]:
               #score+=1
        draw_circle(.019,x,listy[i])"""
listxy=[]      
def xy(listxy):
  global listy
  global listx
  for i  in range(len(listy)):
    for x in (listx[i]):
      listxy.append((x,listy[i]))
  print(listxy)

    
c=0    



def display():
   global c
   
   glClear(GL_COLOR_BUFFER_BIT) 
   
   glMatrixMode(GL_MODELVIEW)     # try this
   glLoadIdentity()
   glLineWidth(5)
   frame(1)      #upper frame
   frame(-1)     #lower frame
   G()           #G letter
   O(0,0,0)        #outer left o
   O(.05,.05,0)        #inner left o
   
   glTranslate(-.3,0,0)#outer right o
   O(0,0,0)        
   O(.05,.05,0)        #inner right o

   glLoadIdentity()        #g ##ww
   glTranslate(.6,-.2,0)
   thin_rect(-.1)

   glLoadIdentity()
   l()                #l
   E()                #e

   ########### the rest of maze########
   small_rect(1,1)    #top left     very small rect
   small_rect(-1,1)   #bottom left  very small rect
   small_rect(1,-1)    #top right   very small rect
   small_rect(-1,-1)   #bottom right very small rect
  
   thin_rect()          #above double o
   
   glTranslate(.6,0,0)   #above g ##www
   thin_rect(-.1)

   glLoadIdentity()     #above E
   glTranslate(1,0,0) 
   glScale(2/5,1,1)
   thin_rect(0)

   glLoadIdentity()     #under G
   glTranslate(-.6,-.5,0) 
   glScale(4/5,1,1)
   thin_rect(0)

   glLoadIdentity()
   T()                  #T   (under g)
   AA(0)                #under left o
   glTranslate(-.3,0,0) #under right o
   AA(.1)
   
   glLoadIdentity()
   glTranslate(1,-.5,0) #under l&e
   glScale(4/5,1,1)
   thin_rect(0)
   
   glLoadIdentity()
   string="score : "+str(10)
   drawText(string,-1.25,.45)
   
   glLoadIdentity()
   #score(key_1,key_2)
   glTranslate(key_1,key_2,0)
   glColor(1,0,0)
   draw_circle(.04,0,0)
   
   glLoadIdentity()
   glColor(0,0,1)
   cheese2() #draw cheese
   xy(listxy)


   

   glutSwapBuffers()  
 

    
glutInit()            #must be called before other GL/GLUT functions
glutInitWindowSize(1000, 400) 
glutCreateWindow(b'MAZE')
counter()#called it before display because display will change the "count"
glutDisplayFunc(display)
glutSpecialFunc(arrow_keys)
glutIdleFunc(display)
init() # Any function name for initialization
glutMainLoop()
