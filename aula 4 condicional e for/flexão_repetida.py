from hub import port
import runloop as lego
import motor_pair as motores
from hub import light_matrix as tela 
from app import sound as som
#Anda até o sensor ser pressionadoduration
async def main():

    motores.pair(motores.PAIR_1, port.B, port.A)
    for index in range (5):
        await motores.move_for_time(motores.PAIR_1, duration=1000,steering=0,velocity=-50)
        await tela.write( str(index+1))
        if ( index == 5):
            som.play('Applause 1')
        else:
            som.play('Coin')
        await motores.move_for_time(motores.PAIR_1, duration=1000,steering=0,velocity=50)

lego.run(main())



