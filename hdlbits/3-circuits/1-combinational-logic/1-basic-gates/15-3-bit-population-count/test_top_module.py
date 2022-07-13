import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def population_count(d):
    count = 0
    for i in range(3):
        count += d & 1
        d = d >> 1
    return count

@cocotb.test()
async def test(dut):
    for i in range(2**3):
        dut.i.value = i
        await Timer(2, units="ns")

        assert dut.o.value == population_count(i), f"test failed with i={dut.i.value} o={dut.o.value}"
