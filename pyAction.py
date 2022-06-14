from tempfile import SpooledTemporaryFile
import pyxel
import SpObj

WIDTH=256
HEIGHT=256
FPS=60

class App:

    #床描画
    def drwflr(self):
        x=0
        for x in range(0,WIDTH,16):
            pyxel.blt(x,HEIGHT-16, 1, 0,0, 16,16)


    def __init__(self):
        #self.newsp = SpObj.sprite(10,10,-8,-8,True)
        #self.newsp.spset(0,0,0,15)

        #self.plsp = SpObj.sprite(100,100,0,0,True)
        #self.plsp.spset(0, 0,0, 15)

        self.plsp = SpObj.sprite()
        self.plsp.spset(0, 16,16, 8,8, 0,0, 15)
        self.plsp.sphome(8,8)
        self.plsp.spshow(True)
        self.plsp.spcolc(8)
        self.plsp.spcolr(0,0,16,16)


        self.ensp = SpObj.sprite()
        self.ensp.spset(0, 16,16, 8,8, 16,0, 15)
        self.ensp.spshow(True)
        self.ensp.spcolc(8)
        self.ensp.spcolr(0,0,16,16)

        self.ex=WIDTH   #enemy pos
        self.ey=HEIGHT-32

        pyxel.init(WIDTH, HEIGHT, "pyActionTest", FPS)
        pyxel.load("./assets/pyActTest.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.px = pyxel.mouse_x
        self.py = pyxel.mouse_y

        self.ex -=4
        if self.ex<-16:
            self.ex=WIDTH


    def draw(self):
        pyxel.cls(1)

        #床
        self.drwflr()

        #PlayerChar
        self.plsp.spdraw(self.px, self.py)
        #self.plsp.show_collision_c(0)
        self.plsp.show_collision_r(False)

        #障害物
        self.ensp.spdraw(100, 100)
        self.ensp.show_collision_r(False)
        #self.ensp.show_collision_c(0)

        if self.plsp.sphitr(self.ensp) == True:
            self.ensp.show_collision_r(True)


        #pyxel.line(0,0, self.px, self.py,9)

App()
