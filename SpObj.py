import pyxel

class sprite:
    def __init__(self):
        self._x = -100      #スプライト表示座標
        self._y = -100

        self._w = 16    #スプライトサイズ  
        self._h = 16

        self._ox = 0 #self._w / 2    #原点(スプライト左上原点を0,0とした相対座標)
        self._oy = 0 #self._h / 2
        
        self._col_r = -1   #collision round size
        self._show = False

        self._imgpage = 0 #スプライト参照ページ

        self._imgu = 0 #参照座標
        self._imgv = 0

        self._imgc = 15  #マスクカラー

    #スプライト情報設定
    def spset(self, imgpage=0, w=16,h=16, ox=0, oy=0, u=0, v=0, mask_color=15):
        self._imgpage = imgpage

        self._w = w    #スプライトサイズ  
        self._h = h

        self._ox = ox  #原点
        self._oy = oy        

        self._imgu = u #リソース画像の参照座標
        self._imgv = v
        
        self._imgc = mask_color  #透過Color

    #原点設定
    def sphome(self, ox, oy):
        self._ox = ox    #原点
        self._oy = oy
    
    def spshow(self, show:bool):
        self._show = show

    #スプライト描画
    def spdraw(self, x, y):
        self._x = x
        self._y = y
        if self._show == True:
            pyxel.blt(self._x-self._ox, self._y-self._oy, self._imgpage, self._imgu, self._imgv, self._w, self._h, self._imgc)
            #pyxel.blt(self.__x, self.__y, self.__imgpage, self.__imgu, self.__imgv, self.__w, self.__h, self.__imgc)
    
    #コリジョン円設定[半径]
    def spcolc(self, r):
        self._col_r = r
    
    #コリジョン判定(円形)
    def sphitc(self, spobj):
        d = pyxel.sqrt((self._x-spobj._x)**2 + (self._y-spobj._y)**2)
        if d <= (self._col_r + spobj._col_r):
            return True
        else:
            return False
    
    #コリジョン範囲表示(DEBUG)
    #fill=0 塗りつぶさない / fill=1 塗りつぶす
    def show_collision_c(self, fill=0):
        if self._col_r != -1:
            if fill==0:
                pyxel.circb(self._x, self._y, self._col_r, 8)
            else:
                pyxel.circ(self._x, self._y, self._col_r, 8)

    #コリジョン矩形
    def spcolr(self, x,y, w,h):
        self._col_x = x
        self._col_y = y
        self._col_w = w
        self._col_h = h

    def show_collision_r(self, fill=0):
        pass
