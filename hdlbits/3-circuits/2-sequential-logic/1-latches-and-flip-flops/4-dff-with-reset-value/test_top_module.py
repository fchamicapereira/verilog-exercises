import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    await RisingEdge(dut.clk)

    for d in range(2**8):
        for reset in range(2**1):
            dut.reset.value = reset
            dut.d.value = d

            await RisingEdge(dut.clk)
            assert dut.q.value == (0x34 if reset else d), f"test failed with d={dut.d.value} reset={dut.reset.value} q={dut.q.value}"
