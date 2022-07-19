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
    dut.reset.value = 1
    await FallingEdge(dut.clk)

    dut.i.value = 0
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    last_in = 0
    last_o = 0

    for _ in range(100):
        i = rand(8)
        reset = rand(1)

        dut.i.value = i
        dut.reset.value = reset

        if reset == 1:
            o = 0
        else:
            o = ((last_in & ~i) | last_o) % (2**8)

        last_in = i
        last_o = o

        await FallingEdge(dut.clk)
        assert dut.o.value == o, f"test failed with i={dut.i.value} reset={dut.reset.value}"
