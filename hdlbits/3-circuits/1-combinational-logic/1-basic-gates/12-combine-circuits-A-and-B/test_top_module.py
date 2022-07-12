import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def A(x,y):
    return ((x^y) & x) % 2

def B(x,y):
    return (~(x^y)) % 2

def AB(x,y):
    return ((A(x,y) | B(x,y)) ^ (A(x,y) & B(x,y))) % 2

@cocotb.test()
async def test(dut):
    for x in range(2):
        for y in range(2):
            dut.x.value = x
            dut.y.value = y

            await Timer(2, units="ns")
            assert dut.z.value == AB(x,y), f"test failed with x={dut.x.value} y={dut.y.value} z={dut.z.value}"
