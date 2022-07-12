import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def mod_a(a,b):
    return a | b

@cocotb.test()
async def test(dut):
    for i in range(100):
        a = rand(1)
        b = rand(1)

        dut.a.value = a
        dut.b.value = b

        await Timer(2, units="ns")
        assert dut.o.value == mod_a(a,b), f"randomized test failed with a={dut.a.value}, b={dut.b.value}, and o={dut.o.value}"
