import numpy as np
import PIL.Image as Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class PJ2Graph():
    def __init__(self):
        self.points = [[-0.5,-0.5,0],[0.5,-0.5,0],[0.5,0.5,0],[-0.5,0.5,0],[-0.5,-0.5,-0.2],[0.5,-0.5,-0.2],[0.5,0.5,-0.2],[-0.5,0.5,-0.2]]
        self.faces = [[0,1,2,3],[0,1,5,4],[1,2,6,5]]
        self.tex_cor = [[0.0,0.0],[1.0,0.0],[1.0,1.0],[0.0,1.0],[0.0,0.0],[1.0,0.0],[1.0,1.0],[0.0,1.0]]
        self.light_pos = [-3.0, 3.0, 2.0, 0.0]
        self.SetTexture()
        self.SetLight()

    def SetTexture(self):
        glEnable(GL_TEXTURE_2D);
        img = Image.open("texture.jpg")
        img = np.asarray(img, dtype=np.uint8)
        self.textures = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.textures)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.shape[0], img.shape[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img)

    def SetLight(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_pos)
        
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glRotatef(-30.0,0.0,1.0,0.0)
        glRotatef(-30.0,1.0,0.0,0.0)        
        
        glBegin(GL_QUADS)
        glNormal3f(0.0,0.0,1.0)
        for point in self.faces[0]:
            glTexCoord2fv(self.tex_cor[point])
            glVertex3fv(self.points[point])
        glNormal3f(0.0,1.0,0.0)
        for point in self.faces[1]:
            glTexCoord2fv(self.tex_cor[point])
            glVertex3fv(self.points[point])
        glNormal3f(-1.0,0.0,0.0)
        for point in self.faces[2]:
            glTexCoord2fv(self.tex_cor[point])
            glVertex3fv(self.points[point])
        glEnd()
        
        glPopMatrix()
        glFlush()
        
def main():
    glutInit()
    glutInitWindowSize(500,500)
    glutCreateWindow("PJ2")
    graph = PJ2Graph()
    glutDisplayFunc(graph.draw)
    glutMainLoop()
    
if __name__ == "__main__":
    main()
