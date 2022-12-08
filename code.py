# import random
# from Diamond import Diamond, Ball
# import displayio
# import board
# import time
# def collision(group,ball,diamonds):
#     idx = -1
#     for i, diamond in enumerate(diamonds):
#         x1 = diamond.tl1.x
#         y1 = diamond.tl1.y
#         x2 = ball.posx
#         y2 = ball. posy
#     if d< 3:
#         idx = i
#     if idx >= 0:
#         del group [idx]
#         del diamonds[idx]

# ball=Ball()
# group=displayio.Group(max_size=10)
# diamonds=[
# for i in range(1):
#     d1= Diamond(random.randint(50,230), random.randint(50,230))
#     diamonds.append(d1)
#     group.append(d1.getGroup())

# group.append(ball.getGroup())
# board.DISPLAY.show(group)
# while True:
#     ball.update()
#     time.sleep(1/60)


import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    pixels.fill((255, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
