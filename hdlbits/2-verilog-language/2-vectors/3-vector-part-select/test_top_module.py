import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def swap_endianness(d):
    return (d >> 24) & 0xff | \
        ((d >> 16) & 0xff) << 8 | \
        ((d >> 8) & 0xff) << 16 | \
        ((d >> 0) & 0xff) << 24

@cocotb.test()
async def test(dut):
    for i in range(10):
        i = random.randint(0, 2**32 - 1)
        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.o.value == swap_endianness(i), \
            f"randomized test failed with i={hex(dut.i.value)}, o={hex(dut.o.value)}"
