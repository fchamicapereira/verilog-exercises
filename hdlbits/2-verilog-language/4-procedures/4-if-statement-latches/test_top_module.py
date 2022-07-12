import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for i in range(100):
        cpu_overheated = rand(1)
        arrived = rand(1)
        gas_tank_empty = rand(1)

        dut.cpu_overheated.value = cpu_overheated
        dut.arrived.value = arrived
        dut.gas_tank_empty.value = gas_tank_empty

        await Timer(2, units="ns")

        shut_off_computer = cpu_overheated
        keep_driving = 0 if arrived or gas_tank_empty else 1

        assert dut.shut_off_computer.value == shut_off_computer, f"randomized test failed with cpu_overheated={dut.cpu_overheated.value}, shut_off_computer={dut.shut_off_computer.value}"
        assert dut.keep_driving.value == keep_driving, f"randomized test failed with arrived={dut.arrived.value}, gas_tank_empty={dut.gas_tank_empty.value}, keep_driving={dut.keep_driving.value}"
