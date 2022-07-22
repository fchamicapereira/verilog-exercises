import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.reset.value = 1
    await FallingEdge(dut.clk)

    counter = 0
    for i in range(10000):
        # make the probability of reseting really low
        # like 1 / 10000
        p=1/10000
        reset = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        dut.reset.value = reset

        await FallingEdge(dut.clk)
        
        counter = 0 if reset else (counter + 1) % 10000
        d0 = int(counter%10)
        d1 = int((counter%100-counter%10)/10)
        d2 = int((counter%1000-counter%100)/100)
        d3 = int((counter%10000-counter%1000)/1000)
        q = (d0 | (d1 << 4) | (d2 << 8) | (d3 << 12)) & 0xffffffff

        assert dut.q.value == q, f"test failed with reset={dut.reset.value}"
