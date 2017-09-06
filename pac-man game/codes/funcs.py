from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time  import sleep
import  random  
import sys
from sound import *
import pygame


def rect(tex_id, xo, yo, xf, yf):         #used to wrap monsters on quad
    glBindTexture(GL_TEXTURE_2D, tex_id)  #used to wrap pacman (defult) and when press right
    #glTranslate(-.5,-.5,0)
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex3f(xo, yo, 0)
    glTexCoord2f(0, 1)
    glVertex3f(xo, yf, 0)
    glTexCoord2f(1, 1)
    glVertex3f(xf, yf, 0)
    glTexCoord2f(1, 0)
    glVertex3f(xf, yo, 0)
    glEnd()


def rectl(tex_id, xo, yo, xf, yf):       #used to wrap pacman  when press left (make mouth toward left)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex3f(xf, yo, 0)
    glTexCoord2f(0, 1)
    glVertex3f(xf, yf, 0)
    glTexCoord2f(1, 1)
    glVertex3f(xo, yf, 0)
    glTexCoord2f(1, 0)
    glVertex3f(xo, yo, 0)
    glEnd()


def rectb(tex_id, xo, yo, xf, yf):      #used to wrap pacman  when press bottom (make mouth toward bottom)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glBegin(GL_QUADS)

    glTexCoord2f(0, 0)
    glVertex3f(xo, yf, 0)
    glTexCoord2f(0, 1)
    glVertex3f(xf, yf, 0)
    glTexCoord2f(1, 1)
    glVertex3f(xf, yo, 0)
    glTexCoord2f(1, 0)
    glVertex3f(xo, yo, 0)
    glEnd()


def rectt(tex_id, xo, yo, xf, yf):     #used to wrap pacman  when press top (make mouth toward top)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    #glTranslate(-.5,-.5,0)
    glBegin(GL_QUADS)

    glTexCoord2f(0, 1)
    glVertex3f(xo, yo, 0)
    glTexCoord2f(0, 0)
    glVertex3f(xf, yo, 0)
    glTexCoord2f(1, 0)
    glVertex3f(xf, yf, 0)
    glTexCoord2f(1, 1)
    glVertex3f(xo, yf, 0)
    glEnd()
def drawCheese(listaa): 
   for i in range(len(listaa)):
      glLoadIdentity()
      glColor(1,.851,0)
      glTranslate(listaa[i][0],listaa[i][1],0)
      glScale(.25,.25,0)
      glutSolidSphere(.1,30,30)


def G():
   glBegin(GL_LINE_LOOP)
   glVertex(-.6,.3)
   glVertex(-1,0.3) # top left for g
   glVertex(-1,-.1) #bottom left for g 
   glVertex(-.6 ,-.1)
   
   glVertex(-.6 ,0.1)
   glVertex(-.8 ,0.1)
   glVertex(-.8 ,.045)
   glVertex(-.7 ,.045)
   
   glVertex(-.7,-.045)  # change y to put cheese inside G
   glVertex(-.9 ,-.045)  # change  y to put cheese inside G
   
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
def g():
   glBegin(GL_LINE_LOOP)
   glVertex(.1,.1)
   glVertex(.5 ,0.1)
   glVertex(0.5 ,0)
   glVertex(.1,0)
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
   glVertex(.99 ,0.1)
   glVertex(.99,-0.1)
   glVertex(.8 ,-.1)
   glEnd()
   
def thin_rect(TX=0):      #used to draw g and rects
   glBegin(GL_LINE_LOOP)
   glVertex(-.5,.3)
   glVertex(0+TX ,.3)
   glVertex(0+TX,.2)
   glVertex(-.5 ,.2)
   glEnd()

def small_rect(TY=1,TX=1):   #used to draw very small rects
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
   glEnd()

def AA(TY=0):           #used to draw under o
   glBegin(GL_LINE_LOOP)
   glVertex(-.15,-.2)
   glVertex(-.05 ,-.2)
   glVertex(-.05,-.4+TY)
   glVertex(-.15 ,-.4+TY)
   glEnd()
   

def frame(TY=1):       #draw to draw outer frames
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


def redMonsterRandFunc():   #used to select random number for random motion  for red monster
   r = random.randrange(1,5)
   return r 
   
def blueMonsterRandFunc():   #used to select random number for random motion for blue monster
   r = random.randrange(1,5)
   return r 

def binkMonsterRandFunc():   #used to select random number for random motion for pink monster
    r = random.randrange(1,5)
    return r 
def yallowMonsterRandFunc():   #used to select random number for random motion for yellow monster
    r = random.randrange(1,5)
    return r 




leftLista = [((-1,0.3),(-1,-.1)),\
((-.7 ,.045),(-.7 ,-.045)),\
((-.8 ,0.1),(-.8 ,0.045)),\
#end of G
((-.2,.1),(-.2,-0.1)),\
#end of right o 
((-.5,.1),(-0.5,-0.1)),\
#end of elft  o
((-.5,.3),(-.5,.2)),\
((.1,.3),(.1,.2)),\
((.1,.1),(.1,0)),\
((.1,-.1),(.1,-0.2)),\
((.25,-.2),(.25,-0.3)),\

((.6,-.2),(.6,-0.3)),\

((-.2,-.2),(-.2,-0.3)),\
((-.5,-.2),(-.5,-0.3)),\
((-1,-.2),(-1,-0.3)),\

((-1.15,.3),(-1.15,.2)),\
#above is the small rect in the left top 
((-1.15,-.2),(-1.15,-0.3)),\
#above is the small rect in the left bootom


((.6,.3),(.6,-.1)),\
# L
((.8,.3),(.8,.2)),\


((1.25,1),(1.25,-.7)),\
((1.1,-0.05),(1.1,-.1)),\

((1.25,.7),(1.25,.1)),\
((1.1,0.1),(1.1,.05)),\
((.8,.1),(.8 ,-.1))
]
#rightlista=[]
rightlista=[
((-.6 ,0.1),(-.6 ,-0.1)),\
((-.6 ,0.3),(-.6 ,0.2)),\
((-.9 ,0.2),(-.9 ,-0.045)),\
#end of G
((0,.1),(0,-.1)),\
#end of right o 
((-.3,.1),(-.3,-.1)),\
#end of left o 
((-1.15,.3),(-1.15 ,.2)),\
#the top left rect 
((.5,.3),(.5,.2)),\

((.0,.3),(.0,.2)),\

((.5,.1),(.5,0)),\
((.5,-.1),(.5,-.2)),\

((.35,-.2),(.35,-.3)),\

((.7,.3),(.7,-.1)),\
((1.15,.3),(1.15,.2)),\

((1.15,-.2),(1.15,-.3)),\

((0,-.2),(0,-.3)),\
((-.3,-.2),(-.3,-.3)),\
((-.6,-.2),(-.6,-.3)),\

((.99 ,0.1),(.99,-0.1)),\


((-1.3,-.1),(-1.3,-.7)),\

((-1.3,.7),(-1.3,-.71)),\

((-1.15,-0.05),(-1.15,-.1)),\
((-1.15,0.1),(-1.15,.05)),\

((-1.15,-.2),(-1.15 ,-.3)),\
#the bottom left rect 
           ]



def rightCheck(leftLista,x,y):
    for i in range(len(leftLista)):   #check on right motion of pacman
        if x<= leftLista[i][0][0]:
            a = leftLista[i][0][1]  #a is the heighest y 
            b = leftLista[i][1][1]  # b is the lowest y
            #if  x+.09 >= leftLista[i][0][0] and x+.09 <= leftLista[i][0][0]+.01   and y-.03<= a  and y+.03 >= b :
            if 0.1 >= x-leftLista[i][0][0]+0.04 >=-0.1  and y-.03<= a  and y+.03 >= b:
                return False    #there is an obstcal
    return True 



def leftCheck(rightlista,x,y):      #check on left motion of pacman
    for i in range(len(rightlista)):
        if x>= rightlista[i][0][0]:
            a = rightlista[i][0][1]   #a is the heighest y
            b = rightlista[i][1][1]   # b is the lowest y
            #if  x+.09 >= leftLista[i][0][0] and x+.09 <= leftLista[i][0][0]+.01   and y-.03<= a  and y+.03 >= b :
            if 0.05 >= x-rightlista[i][0][0]>=-0.021 and y-.03<= a  and y+.03 >= b:
                return False
    return True 
 
bottomlista =[
((-.9 ,.2),(-.65 ,.2)),\
((-.85 ,.045),(-.7 ,.045)),\
((-1.05,-.1),(-.65 ,-.1)),\
#end of G
 ((-0.25,-.1),(-.05,-.1)),\
 #end of right o 
 ((-0.55,-.1),(-.35,-.1)),\
 #end of left  o 
((-1.2,.2),(-1.15 ,.2)),\

((.75,-0.1),(.95 ,-.1)),\
((-1.2,-.3),(-1.15 ,-.3)),\
##small ect botton left 
((-1.05,-.3),(-.65 ,-.3)),\
((-.55,-.3),(-.35 ,-.3)),\
((-.25,-.3),(-.05 ,-.3)),\


((+.55,-.3),(1.1 ,-.3)),\

((+.55,-.1),(.65 ,-.1)),\


((.05 ,-.2),(.25 ,-.2)),\

((.2 ,-.3),(.3 ,-.3)),\
((.3 ,-.2),(.45 ,-.2)),\
((.05 ,0),(.45 ,0)),\
((.05 ,.2),(.45 ,0.2)),\

((.75 ,.2),(1.1 ,0.2)),\



((-.55 ,.2),(-.05 ,0.2)),\

((-1.35 ,.4),(1.35 ,0.4)),\

((-1.3,.05),(-1.15,.05)),\

((-1.3,-.1),(-1.15,-.1)),\

((1.05,.05),(2,.05)),\

((1.05,-.1),(2,-.1)),\

              ]



def topCheck(bottomlista,x,y):      #check on top motion of pacman
    for i in range(len(bottomlista)):
        if y <= bottomlista[i][0][1]:
            a = bottomlista[i][1][0]   #a is the most right x
            b = bottomlista[i][0][0]   #b is the most left x
            #if  x+.09 >= leftLista[i][0][0] and x+.09 <= leftLista[i][0][0]+.01   and y-.03<= a  and y+.03 >= b :
            if 0.1 >= y-bottomlista[i][0][1]-.04 >=-0.1  and x-.03<= a  and x+.03 >= b:
                return False
    return True 


toplista = [
((-1,.3),(-0.6,0.3)),\
((-.8 ,0.1),(-.6 ,0.1)),\
((-.9 ,-.045),(-.7 ,-.045)),\
# #for the top  of G
((-.2,.1),(0 ,.1)),\
 #end of right o 
((-.5,.1),(-0.3 ,.1)),\
#end of elft  o
((-.5,.3),(0,.3)),\
((.1,.3),(.5,.3)),\
((.1,.1),(.5,.1)),\
((.1,-.1),(.5,-.1)),\

((-.2,-.2),(0 ,-.2)),\
((-.5,-.2),(-.3 ,-.2)),\
((-1,-.2),(-.6 ,-.2)),\

((-1.15,-.2),(-1.1 ,-.2)),\
((-1.15,.3),(-1.1 ,.3)),\

((-1.35 ,-.4),(1.35 ,-0.4)),\


((.8,.1),(.99 ,0.1)),\


((.6,.3),(.7,.3)),\
((.8,.3),(1.15,.3)),\

((.6,-.2),(1.15,-.2)),\


((-1.3,.1),(-1.1,.1)),\

((-1.3,-.05),(-1.1,-.05)),\

((1.1,.1),(2,.1)),\

((1.1,-.05),(2,-.05)),\


]
def bottomCheck(toplista,x,y):      #check on bottom motion of pacman
    for i in range(len(toplista)):
        if y >= toplista[i][0][1]:
            a = toplista[i][1][0]  #a is the most right x
            b = toplista[i][0][0]  #b is the most left x
            #if  x+.09 >= leftLista[i][0][0] and x+.09 <= leftLista[i][0][0]+.01   and y-.03<= a  and y+.03 >= b :
            if 0.1 >= y-toplista[i][0][1]+0.04 >=-0.1  and x+0.01<= a and x+.08 >= b:
                return False
    return True 

