import pyxel
import SpObj

class App:
    def __init__(self):
        self.newsp = SpObj.sprite(10,10,16,16,-8,-8,True)
        self.newsp.spset(0,0,0,15)

        pyxel.init(512, 512, title="pyActionTest")
        pyxel.load("./assets/pyActTest.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #pass

    def draw(self):
        pyxel.cls(0)
        #pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        #pyxel.blt(61, 66, 0, 0, 0, 38, 16)

        self.newsp.alive = True
        self.newsp.spdraw(10,10)

App()
