import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def lfsr(d):
    q4 = (d >> 0) & 0b1
    q3 = (d >> 4) & 0b1
    q2 = ((d >> 3) ^ (d >> 0)) & 0b1
    q1 = (d >> 2) & 0b1
    q0 = (d >> 1) & 0b1

    return (q0 | (q1 << 1) | (q2 << 2) | (q3 << 3) | (q4 << 4)) & 0b11111

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.reset.value = 1
    dut.q.value = 1
    q = 1

    await FallingEdge(dut.clk)

    dut.reset.value = 0

    for i in range(1000):
        p=1/100

        reset = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        
        dut.reset.value = reset

        await FallingEdge(dut.clk)

        if reset:
            q = 1
        else:
            q = lfsr(q)
        
        assert dut.q.value == q, f"test failed with reset={dut.reset.value}"
