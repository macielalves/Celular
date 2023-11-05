"""
"""
__author__ = "Maciel Alves Pereira"
__version__ = "0.0.1"

# De um exercício do Instituto Fedaral do Piauí
# objetivo: fazer associação de classes 1:1
# - Exemplo: associar a bateria a um celular assim.
from random import randrange
import os


# Não requisitado pelo exercício (start)
def load_serial():
    if os.path.exists(s := "seriais.txt"):
        with open(s, "r") as seriais:
            return [code.replace("\n", "") for code in seriais.readlines()]
    else:
        for _ in "a":
            open(s, "a").close()
            load_serial()
        return []


def write_serial(serial):
    with open("seriais.txt", "a") as serial_file:
        serial_file.write(serial + "\n")
    serial_file.close()


def serial_gen():
    try:
        # Cuidado ao alterar os seguintes parâmetros
        serial_final = load_serial()[-1]
    except IndexError as e:
        if not load_serial():
            write_serial(serial := hex(0))
            return serial
        raise e
    write_serial(serial := hex(int(serial_final, 16) + 1))
    return serial


def load_mei():
    if os.path.exists(m := "MEI.txt"):
        with open(m, "r") as meis:
            return [code.replace("\n", "") for code in meis.readlines()]
    else:
        for _ in "a":
            open(m, "a").close()
            load_mei()
        return []


def write_mei(serial):
    with open("MEI.txt", "a") as serial_file:
        serial_file.write(serial + "\n")
    serial_file.close()


def mei_gen():
    try:
        # Cuidado ao alterar os seguintes parâmetros
        mei_final = load_mei()[-1]
    except IndexError as e:
        if not load_mei():
            write_mei(mei := hex(0))
            return mei
        raise e
    write_mei(mei := hex(int(mei_final, 16) + 1))
    return mei


# Não requisitado pelo exercício (and)


class Bateria:
    def __init__(self, codigo, mah, percentual_carga=0):
        self.__codigo = codigo
        self.__mAh = mah
        self.__percentual_carga = percentual_carga

    @property
    def codigo(self):
        return self.__codigo

    @property
    def percentual_carga(self):
        return self.__percentual_carga

    @property
    def capacidade(self):
        return self.__mAh

    def carregar(self, valor):
        """A carga pode carregar até um máximo de 100"""
        try:
            valor = int(valor)
        except ValueError as e:
            raise e
        else:
            if 0 < (x := self.__percentual_carga + valor) < 100:
                self.__percentual_carga += valor
            if x >= 100:
                if not self.percentual_carga == 100:
                    self.__percentual_carga = 100
                print("\033[1;32m" + "Carga Cheia!" + "\033[0m")

    def descarregar(self, valor):
        """A carga pode descarregar até um valor mínimo de 0"""
        try:
            valor = int(valor)
            if valor <= 0:
                valor = abs(valor)
        except ValueError as e:
            raise e
        else:
            if 0 < (x := self.__percentual_carga - valor) < 100:
                self.__percentual_carga -= valor
            if x <= 0:
                if not self.percentual_carga == 0:
                    self.__percentual_carga = 0
                print("\033[1;31m" + "Completamente descarregado!" + "\033[0m")

    # Bônus
    @classmethod
    def gerarBateriaCarregada(cls, codigo, mha):
        return cls(codigo, mha, 100)

    @classmethod
    def get_bateria(cls):
        try:
            return cls(serial_gen(), randrange(100, 4000, 100))
        except NameError:
            print("Não foi possível criar a bateria")
            return


class Celular:
    def __init__(self, mei, bateria: Bateria | None = None, wifi="desligado"):
        self.__ligado = False
        self.__mei = mei
        self.__bateria = bateria
        self.__wifi = wifi

    @property
    def bateria(self):
        return self.__bateria

    @property
    def ligado(self):
        if (
            self.__ligado
            and self.__bateria is not None
            and isinstance(self.__bateria, Bateria)
        ):
            # O celular vai desligar se chegar a 5%
            if self.__bateria.percentual_carga <= 5:
                self.ligarDesligar()
                return self.__ligado

        return self.__ligado

    @property
    def mei(self):
        return self.__mei

    @property
    def wifi(self):
        return self.__wifi

    def ligarDesligar(self):
        if not self.__ligado:
            if self.__bateria is None:
                print("Não é possível ligar pois não a bateria!")
                return
            elif isinstance(self.__bateria, Bateria):
                if self.__bateria.percentual_carga == 0:
                    print("Não é possível ligar por falta de carga!")
                    print("Por favor conecte o carregador!")
                    return
                else:
                    self.__ligado = True
                    print(f"Carga atual: {self.__bateria.percentual_carga}%")
        else:
            print("Desligando...")
            self.__ligado = False

    def colocarBateria(self, bateria):
        if isinstance(bateria, Bateria) and self.__bateria is None:
            self.__bateria = bateria
        elif bool(self.__bateria):
            print("Ja Possui Bateria!")

    def retirarBateria(self):
        if not self.__bateria is None:
            self.__bateria = None
            self.__ligado = False
            self.__wifi = "desligado"
        elif not bool(self.__bateria):
            print("Nenhuma bateria para ser retirada!")

    def ligarDesligarWIFI(self):
        if self.__ligado:
            self.__wifi = "ligado" if not self.wifi == "ligado" else "desligado"

    def assistirVideo(self, tempo):
        if self.__ligado:
            if (t_consumo := tempo * 5) <= (
                b_percent := self.__bateria.percentual_carga
            ):
                if self.wifi == "ligado":
                    print(f"Assistindo Vídeo de {int(t_consumo/5)}m")
                    self.descarregar(t_consumo)
                else:
                    # supondo que funcione o vídeo só com internet
                    print("Para assistir ao vídeo, ligue o WIFI")
            else:
                print(f"É necessário {t_consumo}% de bateria para assistir ao vídeo!")

    def carregar(self, valor):
        if self.__bateria is not None and isinstance(self.__bateria, Bateria):
            self.__bateria.carregar(valor)
        elif self.__bateria is None:
            print("Insira uma bateria para poder carrega-la!")

    def descarregar(self, valor):
        if self.__ligado:
            self.__bateria.descarregar(valor)  # type: ignore
            self.ligado
