import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.i.value = 0
    dut.o.value = 0
    last_o = 0
    await FallingEdge(dut.clk)

    for i in range(10):
        i = rand(1)
        dut.i.value = i
        
        await FallingEdge(dut.clk)
        o = i ^ last_o
        assert dut.o.value == o, f"test failed with i={dut.i.value} o={dut.o.value}"
        last_o = o
