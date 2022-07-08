import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

@cocotb.test()
async def test(dut):
    # clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # cocotb.start_soon(clock.start())  # Start the clock

    # await FallingEdge(dut.clk)  # Synchronize with the clock

    await Timer(1, units="ns")
    assert dut.zero.value == 0, f"output zero should always == 0"
