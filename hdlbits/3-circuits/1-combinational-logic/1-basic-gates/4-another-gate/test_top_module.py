import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for i1 in range(2):
        for i2 in range(2):
            dut.i1.value = i1
            dut.i2.value = i2

            await Timer(2, units="ns")
            assert dut.o.value == (i1 & ~i2) % 2, f"test failed with i1={dut.i1.value} i2={dut.i2.value} o={dut.o.value}"
