from hub import port as porta
import runloop as Lego
import motor
import motor_pair as par_motor
#fazer baliza
async def main():

    motor_pair.pair(par_motor.PAIR_1, porta.B, porta.A)

    await motor_pair.move_for_time(par_motor.PAIR_1, 900,0,velocity=720)
    await motor.run_for_degrees(porta.A, degrees=330, velocity=500)
    await motor_pair.move_for_time(par_motor.PAIR_1, 2000,0,velocity=720)
    await motor.run_for_degrees(porta.A, degrees=-310, velocity=500)
    await motor_pair.move_for_time(par_motor.PAIR_1, 3200,0,velocity=720)
    await motor.run_for_degrees(porta.A, degrees=320, velocity=500)
    await motor_pair.move_for_time(par_motor.PAIR_1, 1000,0,velocity=720)
    await motor.run_for_degrees(porta.A, degrees=50, velocity=500)
    await motor_pair.move_for_time(par_motor.PAIR_1, 2000,0,velocity=-500)

    await motor_pair.run_for_degrees(par_motor.PAIR_1,600,500) #180 graus no chão aproximadamente
Lego.run(main())
