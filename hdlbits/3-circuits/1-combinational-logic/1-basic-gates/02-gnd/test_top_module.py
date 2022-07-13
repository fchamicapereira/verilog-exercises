import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    await Timer(2, units="ns")
    assert dut.o.value == 0, f"test failed with o={dut.o.value}"
