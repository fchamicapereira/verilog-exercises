import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for i in range(100):
        a = rand(1)
        b = rand(1)
        c = rand(1)

        dut.a.value = a
        dut.b.value = b
        dut.c.value = c

        await Timer(2, units="ns")

        assert dut.w.value == a, f"randomized test failed with a={dut.a.value} and w={dut.w.value}"
        assert dut.x.value == b, f"randomized test failed with b={dut.b.value} and w={dut.x.value}"
        assert dut.y.value == b, f"randomized test failed with b={dut.b.value} and w={dut.y.value}"
        assert dut.z.value == c, f"randomized test failed with c={dut.c.value} and w={dut.z.value}"

