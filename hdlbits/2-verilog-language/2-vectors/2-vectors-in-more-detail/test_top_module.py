import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

@cocotb.test()
async def test(dut):
    for i in range(10):
        i = random.randint(0, 2**16 - 1)
        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o_hi.value == (i >> 8) & 0xff and dut.o_lo.value == (i >> 0) & 0xff, \
            f"randomized test failed with i={bin(dut.i.value)}, o_hi={bin(dut.o_hi.value)}, o_lo={dut.o_lo.value}"
