import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for i in range(10):
        in_value = rand(1)
        dut.i.value = in_value

        await Timer(2, units="ns")
        assert dut.o.value == in_value, f"randomized test failed with i={dut.i.value} and o={dut.o.value}"
