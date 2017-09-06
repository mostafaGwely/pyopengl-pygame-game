
from OpenGL.GL import * 
from OpenGL.GLUT import * 
from OpenGL.GLU import * 
import pygame

class tex:
	
	def __init__(self,idt):
		self.id=idt

	def load(self,str):
		imgload = pygame.image.load( str)  
		glBindTexture(GL_TEXTURE_2D,self.id)
		img = pygame.image.tostring(imgload, "RGBA", 1)     #0 make all textures inverted
		width=imgload.get_width()
		height=imgload.get_height()
		glBindTexture(GL_TEXTURE_2D,self.id)
		glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)           # solve the problem of changing color by glTexImage2D and make the polygon of texture white
		glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)