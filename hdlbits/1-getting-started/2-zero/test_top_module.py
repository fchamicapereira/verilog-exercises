import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

@cocotb.test()
async def test(dut):
    await Timer(1, units="ns")
    assert dut.zero.value == 0, f"output zero should always == 0"
