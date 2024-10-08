from hub import port as porta
from hub import light_matrix as tela
import runloop as Lego
import motor_pair as motores
from motor import run_for_degrees as motor_graus

async def main():
    #Conta 3...2...1
    await tela.write('3')
    await Lego.sleep(1000)
    await tela.write('2')
    await Lego.sleep(1000)
    await tela.write('1')
    await Lego.sleep(1000)

    #Cria um par de motores com os motores da porta A e B
    motores.pair(motores.PAIR_1, porta.A, porta.B)
    await motores.move_for_time(motores.PAIR_1, duration=7000,steering=0,velocity=500)
Lego.run(main())