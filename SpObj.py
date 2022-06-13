import pyxel

class sprite:
    def __init__(self, x, y, ox, oy, alive):
        self.__x = x      #スプライト表示座標
        self.__y = y
        self.__ox = ox    #原点
        self.__oy = oy
        self.__r = 16   #collision round size
        self.__alive = alive

    #スプライト情報設定
    def spset(self, img, u, v, col):
        self.__img = img
        self.__imgu = u
        self.__imgv = v
        self.__imgc = col  #マスクカラー

    #原点設定
    def sphome(self, ox, oy):
        self.__ox = ox    #原点
        self.__oy = oy
    
    #スプライト描画
    def spdraw(self, x, y, w, h):
        if self.__alive == True:
            pyxel.blt(self.__x + self.__ox, self.__y+self.__oy, self.__img, self.__imgu, self.__imgv, w, h, self.__imgc)
    
    #コリジョン円直径
    def spcolc(self, r):
        self.__r = r

