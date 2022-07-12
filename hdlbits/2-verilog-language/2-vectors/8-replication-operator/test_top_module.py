import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def sign_extend(i):
    _8bit = bin(i)[2:].zfill(8)
    _32bit = _8bit[0] * 24 + _8bit
    return int(_32bit, 2)

@cocotb.test()
async def test(dut):
    for i in range(100):
        i = rand(8)
        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o.value == sign_extend(i), f"test failed with i={dut.i.value},o={dut.o.value}"
