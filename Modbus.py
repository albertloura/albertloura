# Modbus Client
from ast import Continue
from pyModbusTCP.client import ModbusClient #Biblioteca Modbus
from time import sleep #Comando para delay
import os #Biblioteca para limpar a tela

client=ModbusClient(host="192.168.0.7", port=8899)
try:
    print('Client starting...')
    client.unit_id(10)
    client.open()
    print('Client is online.')
    sleep(2)
    while True:
        os.system('cls') or None
        dados = list(client.read_holding_registers(0,50))
        print(f'Potência consumida: {dados[1]/100}W')
        print(f'Tensão elétrica: {dados[22]/10}V')
        print(f'Corrente elétrica: {dados[25]/100}A')
        sleep(1)
        Continue
except:
    print('Client closing...')
    client.close()
    print('Client is offline.')
