import pyxel

pyxel.init(200,200)

angle = pyxel.rndi(30, 150)
vx = pyxel.cos(angle)
vy = pyxel.sin(angle)
ballx = pyxel.rndi(0, 199)
bally = 0
padx = 100
speed=1
point=0

def update():
    global ballx, bally, vx, vy, padx,speed,point
    int(point)
    ballx += vx #ballx+=vx*speedでも可
    bally += vy #bally+=vy*speedでも可
    if ballx>=200 or ballx<0:
        vx*=-1
    padx = pyxel.mouse_x
    if bally>=195:
        if padx-20<=ballx<=padx+20:
            point+=1
            ballx=pyxel.rndi(0, 199)
            bally=0
            speed+=1
            angle = pyxel.rndi(30, 150)
            vx = pyxel.cos(angle)
            vy = pyxel.sin(angle)
        
    if bally >= 200:
        ballx = pyxel.rndi(0, 199)
        bally = 0
        speed+=1
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)

def draw():
    global ballx, bally, vx, vy, padx,speed,point
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(20,20,"point="+str(point),0)

pyxel.run(update, draw)
