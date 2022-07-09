import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

@cocotb.test()
async def test(dut):
    for i in range(10):
        in_value = random.randint(0, 1)
        dut.i.value = in_value

        await Timer(2, units="ns")
        assert dut.o.value == in_value, f"randomized test failed with i={dut.i.value} and o={dut.o.value}"
