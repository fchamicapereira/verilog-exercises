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

    await FallingEdge(dut.clk)

    dut.r.value = 1
    await FallingEdge(dut.clk)

    dut.r.value = 0
    await FallingEdge(dut.clk)

    for _ in range(100):
        d = rand(1)
        r = rand(1)

        dut.d.value = d
        dut.r.value = r

        await FallingEdge(dut.clk)            
        assert dut.q.value == (0 if r else d), f"test failed with d={dut.d.value} r={dut.r.value} q={dut.q.value}"
