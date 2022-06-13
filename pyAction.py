from tempfile import SpooledTemporaryFile
import pyxel
import SpObj

WIDTH=512
HEIGHT=512
FPS=60

class App:

    def drwflr(self):
        x=0
        for x in range(0,WIDTH,16):
            pyxel.blt(x,HEIGHT-16, 1, 0,0, 16,16)
    


    def __init__(self):
        #self.newsp = SpObj.sprite(10,10,-8,-8,True)
        #self.newsp.spset(0,0,0,15)

        #self.plsp = SpObj.sprite(100,100,0,0,True)
        #self.plsp.spset(0, 0,0, 15)

        self.ensp = SpObj.sprite()
        self.ensp.spset(0, 16,16, 8,8, 16,0, 15)
        self.ensp.spshow(True)
        self.ensp.spcolc(8)

        self.x1=100
        self.y1=100
        self.r1=25

        self.x2=130
        self.y2=130
        self.r2=15

        self.ex=WIDTH   #enemy pos
        self.ey=HEIGHT-32

        pyxel.init(WIDTH, HEIGHT, "pyActionTest", FPS)
        pyxel.load("./assets/pyActTest.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.x2 = pyxel.mouse_x
        self.y2 = pyxel.mouse_y

        self.ex -=4
        if self.ex<-16:
            self.ex=WIDTH


    def draw(self):
        pyxel.cls(0)

        #床
        self.drwflr()

        #障害物
        #pyxel.blt(self.ex,self.ey, 0, 16,0, 16, 16)
        self.ensp.spdraw(200, 200)
        self.ensp.show_collision_r()


        #円形コリジョンの衝突判定
        #self.dist = pyxel.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        #self.color = 6
        #if self.dist < (self.r1 + self.r2):
        #    self.color= 8

        #pyxel.circ(self.x1, self.y1, self.r1, self.color)
        #pyxel.circ(self.x2, self.y2, self.r2, 6)

        #pyxel.text(10,10,str(round(self.dist,2)),7)

        pyxel.line(0,0, 200,200,9)


App()
