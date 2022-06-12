import pyxel

class sprite:
    #self.Enable = True

    def __init__(self, x, y, ox, oy, alive):

        self.__x = x      #スプライト表示座標
        self.__y = y
        #self.__w = w      #スプライト幅、高さ
        #self.__h = h
        self.__ox = ox    #原点
        self.__oy = oy

        self.__alive = alive

    @property
    def alive(self):
        return self.__alive
    
    #@property
    #def sphome(self):
    #    return self.__ox,self.__oy

    @alive.setter
    def alive(self, val):
        self.__alive = val

    def spset(self, img, u, v, col):
        self.__img = img
        self.__imgu = u
        self.__imgv = v
        self.__imgc = col  #マスクカラー

    def sphome(self, ox, oy):
        self.__ox = ox    #原点
        self.__oy = oy
   
    def spdraw(self, x, y, w, h):
        if self.__alive == True:
            pyxel.blt(self.__x + self.__ox, self.__y+self.__oy, self.__img, self.__imgu, self.__imgv, w, h, self.__imgc)
    
