import pyxel

class sprite:
    def __init__(self):
        self.__x = -100      #スプライト表示座標
        self.__y = -100

        self.__w = 16    #スプライトサイズ  
        self.__h = 16

        self.__ox = self.__w / 2    #原点
        self.__oy = self.__h / 2
        
        self.__col_r = -1   #collision round size
        self.__show = False

        self.__imgpage = 0 #スプライト参照ページ

        self.__imgu = 0 #参照座標
        self.__imgv = 0

        self.__imgc = 15  #マスクカラー

    #スプライト情報設定
    def spset(self, imgpage, w,h, ox, oy, u, v, mask_color):
        self.__imgpage = imgpage

        self.__w = w    #スプライトサイズ  
        self.__h = h

        self.__ox = ox*-1  #原点
        self.__oy = oy*-1        

        self.__imgu = u #リソース画像の参照座標　
        self.__imgv = v
        
        self.__imgc = mask_color  #マスクカラー

    #原点設定
    def sphome(self, ox, oy):
        self.__ox = ox*-1    #原点
        self.__oy = oy*-1
    
    def spshow(self, show:bool):
        self.__show = show

    #スプライト描画
    def spdraw(self, x, y):
        self.__x = x
        self.__y = y
        if self.__show == True:
            pyxel.blt(self.__x+self.__ox, self.__y+self.__oy, self.__imgpage, self.__imgu, self.__imgv, self.__w, self.__h, self.__imgc)
            #pyxel.blt(self.__x, self.__y, self.__imgpage, self.__imgu, self.__imgv, self.__w, self.__h, self.__imgc)
    
    #コリジョン円半径
    def spcolc(self, r):
        self.__col_r = r
    
    #コリジョン範囲表示
    def show_collision_r(self):
        if self.__col_r != -1:
            pyxel.circb(self.__x, self.__y, self.__col_r, 8)

