import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def shift(d):
    return (d >> 1) & 0xf

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.areset.value = 1
    await RisingEdge(dut.areset)

    dut.areset.value = 0
    await FallingEdge(dut.areset)

    q = 0
    for i in range(1000):
        p=1/20

        areset = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        load = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        ena = int(numpy.random.choice(numpy.arange(0, 2), p=[p, 1-p]))
        data = rand(4)
        
        dut.areset.value = areset
        dut.load.value = load
        dut.ena.value = ena
        dut.data.value = data

        if areset:
            await RisingEdge(dut.areset)
            dut.areset.value = 0
            await FallingEdge(dut.areset)
            q = 0
        else:
            await FallingEdge(dut.clk)
            if load:
                q = data
            elif ena:
                q = shift(q)
        
        assert dut.q.value == q, f"test failed with areset={dut.areset.value} load={dut.load.value} ena={dut.ena.value} data={dut.data.value}"
