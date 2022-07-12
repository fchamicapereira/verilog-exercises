import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for _ in range(100):
        a = rand(8)
        b = rand(8)
        c = rand(8)
        d = rand(8)

        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d

        _min = min(a,b,c,d)

        await Timer(2, units="ns")
        assert dut.min.value == _min, f"randomized test failed with a={dut.a.value} b={dut.b.value} c={dut.c.value} d={dut.d.value}"
