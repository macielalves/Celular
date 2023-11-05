from dispositivo import Bateria, Celular, mei_gen, serial_gen

# # seriais
# serial_bat = []


# def code_gen():
#     # global serial_bat
#     try:
#         serial_final = serial_bat[0]
#     except IndexError as e:
#         if not serial_bat:
#             serial_bat.insert(0, serial := hex(0))
#             return serial
#         raise e

#     serial_bat.insert(0, serial := hex(int(serial_final, 16) + 1))
#     return serial
print(f'{" Celular 1 ":#^30}\n')
cel1 = Celular(mei_gen(), bateria=Bateria.get_bateria())
cel1.carregar(100)
cel1.ligarDesligar()
cel1.ligarDesligarWIFI()
print(cel1.bateria.percentual_carga)
print(cel1.ligado)
cel1.assistirVideo(10)
print(cel1.bateria.percentual_carga)
cel1.assistirVideo(10)
print(cel1.bateria.percentual_carga)
print(cel1.ligado)

print(f'\n{" Celular 2 ":#^30}\n')

cel2 = Celular("1234c")
cel2.colocarBateria(Bateria("1234b", 3500, 38))
cel2.ligarDesligar()
print(cel2.ligado)
cel2.assistirVideo(5)
cel2.ligarDesligarWIFI()
cel2.assistirVideo(5)
print(cel2.bateria.percentual_carga)
cel2.assistirVideo(5)
cel2.descarregar(8)
print(cel2.bateria.percentual_carga)
cel2.descarregar(8)
print(cel2.bateria.percentual_carga)
cel2.ligarDesligar()
print(cel2.ligado)


print(f'\n{" Celular 3 ":#^30}\n')
c3 = Celular(mei_gen())
bat = Bateria(serial_gen(), 1000)
c3.colocarBateria(bat)
c3.ligarDesligar()
print(c3.ligado)
c3.retirarBateria()
print(c3.ligado)
c3.retirarBateria()
c3.carregar(220)
c3.descarregar(220)


print(f'\n{" Celular 4 ":#^30}\n')
c4 = Celular(mei_gen(), Bateria.gerarBateriaCarregada(serial_gen(), 99999))
c4.ligarDesligar()
