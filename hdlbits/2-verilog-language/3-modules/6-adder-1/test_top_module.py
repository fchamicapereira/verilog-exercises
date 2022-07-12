import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for i in range(100):
        a = rand(32)
        b = rand(32)

        dut.a.value = a
        dut.b.value = b

        await Timer(2, units="ns")
        assert dut.sum.value == (a + b) % (2**32), f"FAILED: a={dut.a.value}, b={dut.b.value}, sum={dut.sum.value}"
