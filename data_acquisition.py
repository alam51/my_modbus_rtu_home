from pymodbus.client.sync import ModbusSerialClient
import datetime
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from modbus_initialize import SlaveAcuvim2
import traceback

port_name = 'com4'
baud_rate = 19200
time_out_second = .2
modbus_rtu_master = ModbusSerialClient(method='rtu', port=port_name, baudrate=baud_rate, timeout=time_out_second)
a = 9

slave_id_name_dict = {
    1: '230kV T3',
    2: '230KV Mongla-2',
    3: '230KV Mongla-1',
    4: '132KV TR-3',
}

slave_obj_list = []
for i, slave_id in enumerate(slave_id_name_dict.keys()):
    try:
        slave_obj_list.append(SlaveAcuvim2(modbus_rtu_master, slave_id=slave_id))
    except:
        traceback.print_exc()
"""Initialization Complete"""
# slave_obj_list = [1,2,3]

for i, slave in zip(slave_id_name_dict.keys(), slave_obj_list):
    try:
        f = slave.get_frequency()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} f = {f}')

        v = slave.get_voltage_LL_average()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} v = {v}')

        ia = slave.get_current_a()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} ia = {ia}')

        ib = slave.get_current_b()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} ib = {ib}')

        ic = slave.get_current_c()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} ic = {ic}')

        i_n = slave.get_current_neutral()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} in = {i_n}')

        p = slave.get_real_power_total()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} p = {p}')

        q = slave.get_reactive_power_total()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} q = {q}')

        p_import = slave.get_import_real_energy_total()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} p_import = {p_import}')

        q_import = slave.get_import_reactive_energy_total()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} q_import = {q_import}')

        p_export = slave.get_export_real_energy_total()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} p_export = {p_export}')

        q_export = slave.get_export_reactive_energy_total()
        print(f'{datetime.datetime.now()}: {slave_id_name_dict[i]} q_export = {q_export}')
    except Exception:
        traceback.print_exc()

