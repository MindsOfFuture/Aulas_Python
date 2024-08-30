from hub import light_matrix as tela
from hub import port as porta
import color_sensor as sensor_de_luz
import color
import runloop as lego

async def main():
    while True:
        if sensor_de_luz.color(porta.A) is color.RED:
            tela.show_image(tela.IMAGE_ANGRY)

        elif sensor_de_luz.color(porta.A) is color.BLUE:
            tela.show_image(tela.IMAGE_SAD)

        elif sensor_de_luz.color(porta.A) is color.GREEN:
            tela.show_image(tela.IMAGE_SILLY)

        elif sensor_de_luz.color(porta.A) is color.YELLOW:
            tela.show_image(tela.IMAGE_GIRAFFE)

        elif sensor_de_luz.color(porta.A) is color.BLACK:
            tela.show_image(tela.IMAGE_SKULL)

        else:
            tela.clear()

lego.run(main())




