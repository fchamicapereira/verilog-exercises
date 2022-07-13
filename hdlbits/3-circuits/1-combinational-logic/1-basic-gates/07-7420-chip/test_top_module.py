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
        p1a = rand(1)
        p1b = rand(1)
        p1c = rand(1)
        p1d = rand(1)

        p2a = rand(1)
        p2b = rand(1)
        p2c = rand(1)
        p2d = rand(1)

        dut.p1a.value = p1a
        dut.p1b.value = p1b
        dut.p1c.value = p1c
        dut.p1d.value = p1d

        dut.p2a.value = p2a
        dut.p2b.value = p2b
        dut.p2c.value = p2c
        dut.p2d.value = p2d

        await Timer(2, units="ns")

        assert dut.p1y.value == (~(p1a & p1b & p1c & p1d)) % 2, f"test failed with p1a={dut.p1a.value} p1b={dut.p1b.value} p1c={dut.p1c.value} p1d={dut.p1d.value} p1y={dut.p1y.value}"
        assert dut.p2y.value == (~(p2a & p2b & p2c & p2d)) % 2, f"test failed with p2a={dut.p2a.value} p2b={dut.p2b.value} p2c={dut.p2c.value} p2d={dut.p2d.value} p2y={dut.p2y.value}"
