from hub import port as porta
import runloop as lego 
import motor_pair as motores
import force_sensor as sensor_força
import motor

def sensor_pressionado():
    return sensor_força.pressed(porta.C)

def sensor_nao_pressionado():
    return not sensor_força.pressed(porta.C)

#Anda até o sensor ser pressionadoduration
async def main():

    motores.pair(motores.PAIR_1, porta.B, porta.A)

    while True:

        # vai pra frente, enquanto não pressionado
        await lego.until(sensor_nao_pressionado)

        motores.move(motores.PAIR_1, 0 ,velocity=750)

        # quando pressionado, vai pra trás e vira
        await lego.until(sensor_pressionado)

        motores.stop(motores.PAIR_1)
        await lego.sleep_ms(3000)

lego.run(main())



