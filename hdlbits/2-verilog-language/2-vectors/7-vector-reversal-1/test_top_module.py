import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def rev(i):
    return int(bin(i)[2:].zfill(8)[::-1], 2)

@cocotb.test()
async def test(dut):
    for i in range(100):
        i = rand(8)
        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o.value == rev(i), f"test failed with i={dut.i.value},o={dut.o.value}"
