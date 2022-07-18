import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    await FallingEdge(dut.clk)

    for d in range(2**8):
        dut.d.value = d

        await FallingEdge(dut.clk)
        assert dut.q.value == d, f"test failed with d={dut.d.value} q={dut.q.value}"
