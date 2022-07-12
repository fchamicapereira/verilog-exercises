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
        i = rand(16)
        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o_hi.value == (i >> 8) & 0xff and dut.o_lo.value == (i >> 0) & 0xff, \
            f"randomized test failed with i={bin(dut.i.value)}, o_hi={bin(dut.o_hi.value)}, o_lo={dut.o_lo.value}"
