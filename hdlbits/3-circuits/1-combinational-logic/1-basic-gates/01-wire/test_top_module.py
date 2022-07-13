import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    dut.i.value = 0
    await Timer(2, units="ns")
    assert dut.o.value == 0, f"test failed with i={dut.i.value} o={dut.o.value}"

    dut.i.value = 1
    await Timer(2, units="ns")
    assert dut.o.value == 1, f"test failed with i={dut.i.value} o={dut.o.value}"
