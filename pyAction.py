import pyxel
import SpObj

WIDTH=512
HEIGHT=512
FPS=60

class App:
    def __init__(self):
        self.newsp = SpObj.sprite(10,10,-8,-8,True)
        self.newsp.spset(0,0,0,15)

        self.x1=100
        self.y1=100
        self.r1=25

        self.x2=130
        self.y2=130
        self.r2=15


        pyxel.init(WIDTH, HEIGHT, "pyActionTest", FPS)
        pyxel.load("./assets/pyActTest.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.x2 = pyxel.mouse_x
        self.y2 = pyxel.mouse_y

        #self.dist = pyxel.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)

        #pass

    def draw(self):
        pyxel.cls(0)
        #pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        #pyxel.blt(61, 66, 0, 0, 0, 38, 16)

        self.dist = pyxel.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)

         
        if self.dist < (self.r1 + self.r2):
            self.color= 8
        else:
            self.color = 6

        pyxel.circ(self.x1, self.y1, self.r1, self.color)
        pyxel.circ(self.x2, self.y2, self.r2, 6)



        self.newsp.alive = True
        self.newsp.spdraw(10,10, -16, 16)

        pyxel.text(10,10,str(round(self.dist,2)),7)



App()
