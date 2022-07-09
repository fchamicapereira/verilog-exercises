import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

@cocotb.test()
async def test(dut):
    for i in range(10):
        a = random.randint(0, 1)
        b = random.randint(0, 1)

        dut.a.value = a
        dut.b.value = b

        await Timer(2, units="ns")
        assert dut.o.value == (~(a | b)) % 2, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, and o={dut.o.value}"
