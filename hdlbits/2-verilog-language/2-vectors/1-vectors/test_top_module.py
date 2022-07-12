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
        vec = rand(3)
        dut.vec.value = vec

        await Timer(2, units="ns")
        assert dut.outv.value == vec and dut.o2.value == (vec >> 2) & 1 and dut.o1.value == (vec >> 1) & 1 and dut.o0.value == (vec >> 0) & 1, \
            f"randomized test failed with vec={bin(dut.vec.value)}, outv={bin(dut.outv.value)}, " + \
            f"o0={dut.o0.value}, o1={dut.o1.value}, o2={dut.o2.value}"
