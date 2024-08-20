from hub import port as porta
import runloop as Lego
from motor import run_for_degrees as motor_graus

async def main():
    #Roda os motores A por 360 graus a 720 graus por segundo
    motor_graus(porta.A, degrees=360, velocity= 720)
    #Roda os motores B por 360 graus a 720 graus por segundo
    motor_graus(porta.B, degrees=360, velocity= 720)
Lego.run(main())