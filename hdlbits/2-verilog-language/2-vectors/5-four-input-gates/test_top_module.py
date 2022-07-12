import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def o_and(i):
    return ((i >> 0) & (i >> 1) & (i >> 2) & (i >> 3)) & 0b1

def o_or(i):
    return ((i >> 0) | (i >> 1) | (i >> 2) | (i >> 3)) & 0b1

def o_xor(i):
    return ((i >> 0) ^ (i >> 1) ^ (i >> 2) ^ (i >> 3)) & 0b1

@cocotb.test()
async def test(dut):
    for i in range(100):
        i = rand(4)
        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o_and.value == o_and(i), f"o_and test failed with i={dut.i.value},o_and={dut.o_and.value}"
        assert dut.o_or.value == o_or(i), f"o_or test failed with i={dut.i.value}, o_or={dut.o_or.value}"
        assert dut.o_xor.value == o_xor(i), f"o_xor test failed with i={dut.i.value}, o_xor={dut.o_xor.value}"
