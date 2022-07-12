import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def population_count(d):
    res = 0
    for i in range(100):
        res += d & 1
        d = d >> 1
    return res

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(100)

        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o.value == population_count(i), f"randomized test failed with i={dut.i.value} o={dut.o.value}"
