import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def truth_table(x1,x2,x3):
    return ((~x1 & x2 & ~x3) | (x1 & x2 & ~x3) | (x1 & ~x2 & x3) | (x1 & x2 & x3)) % 2

@cocotb.test()
async def test(dut):
    for x1 in range(2):
        for x2 in range(2):
            for x3 in range(2):
                dut.x1.value = x1
                dut.x2.value = x2
                dut.x3.value = x3

                await Timer(2, units="ns")
                assert dut.f.value == truth_table(x1,x2,x3), f"test failed with x1={dut.x1.value} x2={dut.x2.value} x3={dut.x3.value} f={dut.f.value}"
