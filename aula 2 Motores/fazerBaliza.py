from hub import port as porta
import runloop as Lego
import motor
import motor_pair as par_motor
#fazer baliza
async def main():
    motor_pair.pair(par_motor.PAIR_1, porta.B, porta.A)

    await motor_pair.move_tank_for_time(par_motor.PAIR_1, 1000,2000,2000)
    await motor.run_for_degrees(porta.A, degrees=277, velocity=720)
    await motor.run_for_degrees(porta.A, degrees=277, velocity=720)
    await motor.pair.move_tank_for_time(par_motor.PAIR_1, 1000,2000,2000)

    #Anda fazendo curva
    await motor_pair.move_for_time(par_motor.PAIR_1, 20000,20,velocity=400)

    #Anda reto
    await motor_pair.move_for_time(par_motor.PAIR_1, 1000,-20,velocity=-400)