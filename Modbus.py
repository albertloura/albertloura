# Modbus Client
from ast import Continue
from pyModbusTCP.client import ModbusClient #Biblioteca Modbus
from time import sleep #Comando para delay
import os #Biblioteca para limpar a tela

client=ModbusClient(host="192.168.0.7", port=8899)
try:
    print('Client starting...')
    client.unit_id(0)
    client.open()
    print('Client is online.')
    while True:
        os.system('cls') or None
        pot=client.read_holding_registers(1,1)
        ten=client.read_holding_registers(22,1)
        cor=client.read_holding_registers(25,1)
        print(f'Potência consumida: {pot[0]/100}W')
        print(f'Tensão elétrica: {ten[0]/10}V')
        print(f'Corrente elétrica: {cor[0]/100}A')
        sleep(1)
        Continue
except:
    print('Client closing...')
    client.close()
    print('Client is offline.')
