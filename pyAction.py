#from tempfile import SpooledTemporaryFile
from numpy import True_
import pyxel
import SpObj

WIDTH=256
HEIGHT=256
FPS=60

FloorList =[]  #床管理リスト

class App:

    #床オブジェクト　
    def initFlr(self):
        for x in range(0,WIDTH,16):
            flr = SpObj.sprite()
            flr.spset(1, 16,16, 0,0, 0,0, 15)
            flr.spshow(True)
            flr.spcolr(0,0,16,16)

            FloorList.append(flr)

            #print(x)

    def drwFlr(self):
        x=0
        #print(len(FloorList))
        for i in range(len(FloorList)):
            FloorList[i].spdraw(x, HEIGHT-16)
            FloorList[i].show_collision_r(False)
            x+=16

    def __init__(self):


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

        self.initFlr()

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
        self.drwFlr()

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
        
        #床との接触判定
        for i in range(len(FloorList)):
            if self.plsp.sphitr(FloorList[i])==True:
                #print("Hit")
                FloorList[i].show_collision_r(True)
                

        #pyxel.line(0,0, self.px, self.py,9)

App()
