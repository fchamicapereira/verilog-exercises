import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def rev(d):
    return int(bin(d)[2:].zfill(100)[::-1], 2)

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(100)

        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o.value == rev(i), f"randomized test failed with i={dut.i.value} o={dut.o.value}"
