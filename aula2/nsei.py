from hub import port as porta
import runloop as Lego
import motor_pair as par_motor
async def main():
    motor_pair(motor_pair.PAIR_1, porta.B, porta.A)

    await motor_pair.move_for_time(par_motor.PAIR_1, 4500,0,velocity=500)
    await motor_pair.move_for_time(par_motor.PAIR_1, 1000,0,velocity=-300)
    await motor_pair.move_for_time(par_motor.PAIR_1, 1200,0,velocity=-300)
    await motor_pair.move_for_time(par_motor.PAIR_1, 1000,0,velocity=-300)
    await motor_pair.move_for_time(par_motor.PAIR_1, 500,0,velocity=400)

Lego.run(main())