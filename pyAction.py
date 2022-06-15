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
            flr.sphome(0,0)
            flr.spshow(True)
            flr.spcolr(0,0,16,16)

            FloorList.append(flr)

            #print(x)

    def drwFlr(self):
        x=0
        #print(len(FloorList))
        for i in range(len(FloorList)):
            FloorList[i].spdraw(x, HEIGHT-16)
            #FloorList[i].show_collision_r(False)
            x+=16

    def __init__(self):

        self.px=60
        self.py=HEIGHT-32

        self.vx = 0
        self.vy = 0
        self.initVy = -10
        self.gravity = 1
        self.flgJmp=False

        self.plsp = SpObj.sprite()
        self.plsp.spset(0, 16,16, 8,8, 0,0, 15)
        #self.plsp.sphome(8,8)
        self.plsp.sphome(0,0)
        self.plsp.spshow(True)
        self.plsp.spcolc(8)
        self.plsp.spcolr(0,0,16,16)


        self.initFlr()

        pyxel.init(WIDTH, HEIGHT, "pyActionTest", FPS)
        pyxel.load("./assets/pyActTest.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


        #LR
        if pyxel.btn(pyxel.KEY_LEFT):
            #self.vx = -2
            self.px -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.px += 2
            #self.vx = 2


        #移動
        #self.px += self.vx

        self.vx=0

        #Jump
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.flgJmp == False:
                self.vy = self.initVy
                self.flgJmp = True
        
        if self.flgJmp == True:
            self.py += self.vy
            self.vy += self.gravity

        #プレイヤーのコリジョン領域を更新
        self.plsp.spcolr_set(self.px, self.py)

        #床との接触判定
        for i in range(len(FloorList)):
            if self.plsp.sphitr(FloorList[i])==True:
                #FloorList[i].show_collision_r(True)
                self.flgJmp = False
                #self.vy=0
                self.py=FloorList[i]._y-16
                #print(FloorList[i]._y)
                #print(self.py)
                break
                
    def draw(self):
        pyxel.cls(1)

        #PlayerChar
        self.plsp.spdraw(self.px, self.py)
        #self.plsp.show_collision_c(0)
        self.plsp.show_collision_r(False)

        #床表示
        self.drwFlr()
 

        #pyxel.line(0,0, self.px, self.py,9)

App()
