from hub import light_matrix as tela
import runloop as Lego  
async def main():
    tela.show(tela.IMAGE_DUCK)
    await Lego.sleep(500)
    tela.clear()
Lego.run(main())