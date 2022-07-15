import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for a in range(1):
        for b in range(1):
            for c in range(1):
                dut.a.value = a
                dut.b.value = b
                dut.c.value = c

                await Timer(2, units="ns")
                assert dut.out.value == (0 if a == 0 and b == 0 and c == 0 else 1), f"test failed with a={dut.a.value} b={dut.b.value} c={dut.c.value} out={dut.out.value}"
