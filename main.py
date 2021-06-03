import pygame as pg
import time
import math

# globals
window_width = 1280
window_height = 950
fps = 60
gravity = 6

# predefined colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
selected_red = (255, 100, 100)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_green = (0, 255, 0)
yellow = (255, 255, 0)

pg.init()
dis = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("phy")
fpsclk = pg.time.Clock()


def event_handler():

    for event in pg.event.get():
        if (event.type == pg.constants.QUIT):
            pg.quit()
            quit()


def displayfps(frametime):
    font = pg.font.Font(None, 18)
    if frametime > 0:
        fps_achived = 1/(frametime)
        fps_achived = "%.2f" % round(fps_achived, 2)
        text = str(fps_achived)
    else:
        text = "0"

    txt_surface = font.render(text, True, white)
    dis.blit(txt_surface, (0, 0))


def slider(slider_pos):
    slider_box_pos = (600, 200)
    slider_box_height = 200
    slider_box_width = 50
    slider_handel_height = 10
    slider_handel_width = 45
    slider_box_colour = white
    slider_handel_colour = red

    # box dimentions
    left = slider_box_pos[0]
    right = slider_box_pos[0] + slider_box_width
    top = slider_box_pos[1]
    bottom = top + slider_box_height

    # slider dimentions
    left_s = left + \
        (slider_box_width - slider_handel_width)/2
    right_s = left_s + slider_handel_width
    top_s = ((((slider_box_height - slider_handel_height)/100)
              * slider_pos) + slider_box_pos[1])
    bottom_s = top_s + slider_handel_height

    mouse = pg.mouse.get_pos()
    clicked = pg.mouse.get_pressed()

    pg.draw.rect(dis, slider_box_colour, (left, top,
                                          slider_box_width, slider_box_height))

    pg.draw.rect(dis, black, ((left+slider_box_width/2)-5, top+1,
                              10, slider_box_height-1))

    if mouse[0] > left and mouse[0] < right and mouse[1] > top and mouse[1] < bottom:
        if clicked[0] == 1:

            slider_pos = (
                (mouse[1]-slider_box_pos[1])/slider_box_height)*100

        if slider_pos < 0:
            slider_pos = 0
        if slider_pos > 100:
            slider_pos = 100
        slider_pos = round(slider_pos)
        pg.draw.rect(dis, blue, (left_s, top_s,
                                 slider_handel_width, slider_handel_height))

    else:
        pg.draw.rect(dis, slider_handel_colour, (left_s, top_s,
                                                 slider_handel_width, slider_handel_height))

    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render(str(slider_pos), True, white)
    textRect = text.get_rect()
    textRect.center = (window_width/2, window_height-50)
    dis.blit(text, textRect)

    return slider_pos


def main_loop():
    slider_pos = 0
    frametime = 0
    while(True):
        curr = time.time()
        event_handler()
        displayfps(frametime)
        slider_pos = slider(slider_pos)
        pg.display.update()
        dis.fill(black)
        fpsclk.tick(fps)
        frametime = ((time.time() - curr) + frametime)/2


main_loop()
