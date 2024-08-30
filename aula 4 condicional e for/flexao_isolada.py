from hub import port as porta
import runloop as lego
import motor_pair as motores

#Anda até o sensor ser pressionadoduration
async def main():

    motores.pair(motores.PAIR_1, porta.B, porta.A)
    for index in range (5):
        await motores.move_for_time(motores.PAIR_1, duration=1000,steering=0,velocity=-50)
        await motores.move_for_time(motores.PAIR_1, duration=1000,steering=0,velocity=50)

lego.run(main())



