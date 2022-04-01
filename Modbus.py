from pyModbusTCP.client import ModbusClient as Modbus
client = Modbus(host='192.168.1.7', port=8899, unit_id=10)
client.open()

consumoKW=potkvarh=voltage=current=activepower=powerfactor=frequency=0

try:
    lerDadosMbus=client.read_holding_registers(0,50)
    consumoKW=(float((str(lerDadosMbus[0] << 8)) + str(lerDadosMbus[1])))/100
    potkvarh=(float((str(lerDadosMbus[12] << 8)) + str(lerDadosMbus[13])))/100
    voltage=(float(lerDadosMbus[22]))/10
    current=(float(lerDadosMbus[25]))/100
    activepower=(float(lerDadosMbus[30]))/1000
    powerfactor=(float(lerDadosMbus[43]))/1000
    frequency=(float(lerDadosMbus[17]))/100
except:    
    print('Erro leitura modbus')


client.close()

print(f'{consumoKW} kWh')
print(f'{potkvarh} kvarh')
print(f'{voltage} V')
print(f'{current} A')
print(f'{activepower} kW')
print(f'{powerfactor} ')
print(f'{frequency} Hz')