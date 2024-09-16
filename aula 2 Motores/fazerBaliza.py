from hub import port as porta
import runloop as Lego
import motor
import motor_pair
#fazer baliza
async def main(): 
    motor_pair.pair(motor_pair.PAIR_1, porta.B, porta.A)

    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, 2000, 2000)
    await motor.run_for_degrees(porta.A, 277, 720)
    await motor.run_for_degrees(porta.A, 277, 720)
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000,2000,2000)

    #Anda fazendo curva
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2000,20, velocity=400)

    #Anda reto
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000,-20, velocity=-400)

Lego.run(main())
