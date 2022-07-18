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
    await FallingEdge(dut.clk)

    last_in = 0

    for _ in range(100):
        i = rand(8)        
        dut.i.value = i

        anyedge = (i ^ last_in) % (2**8)
        last_in = i

        await FallingEdge(dut.clk)
        assert dut.anyedge.value == anyedge, f"test failed with i={dut.i.value} pledge={dut.pledge.value}"
