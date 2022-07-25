import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def lfsr(d):
    q = 0

    for i in range(32):
        qb = 0

        if i != 31:
            prev = (d >> (i+1)) & 0b1
        else:
            prev = 0

        if i in [ 0, 1, 21, 31 ]:
            qb = (prev ^ (d & 0b1)) & 0b1
        else:
            qb = prev & 0b1
        
        q = (q | (qb << i)) & 0xffffffff

    return q

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
