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

    dut.resetn.value = 0
    dut.i.value = 0
    dut.o.value = 0

    await FallingEdge(dut.clk)

    dut.resetn.value = 1

    o = dut.o.value
    for i in range(1000):
        p=1/100

        i = rand(1)
        resetn = int(numpy.random.choice(numpy.arange(0, 2), p=[p, 1-p]))
        
        dut.i.value = i
        dut.resetn.value = resetn

        await FallingEdge(dut.clk)

        if resetn == 0:
            assert dut.o.value == 0, f"test failed with resetn={dut.resetn.value}"
            o = 0
            continue

        await FallingEdge(dut.clk)
        assert dut.o.value == o, f"test failed with resetn={dut.resetn.value}"

        await FallingEdge(dut.clk)
        assert dut.o.value == o, f"test failed with resetn={dut.resetn.value}"

        await FallingEdge(dut.clk)
        assert dut.o.value == i, f"test failed with resetn={dut.resetn.value}"

        o = i
        
