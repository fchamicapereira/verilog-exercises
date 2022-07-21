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
    OneHertz = 0

    for i in range(10000):
        # make the probability of reseting really low
        # like 1 / 10000
        reset = int(numpy.random.choice(numpy.arange(0, 2), p=[0.9999, 0.0001]))
        dut.reset.value = reset

        await RisingEdge(dut.clk)
        
        counter = 0 if reset else counter + 1
        OneHertz = 1 if reset == 0 and (counter % 1000) == 0 else 0

        assert dut.OneHertz.value == OneHertz, f"test failed with reset={dut.reset.value}"
