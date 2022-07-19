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

    dut.reset.value = 1
    await FallingEdge(dut.clk)

    dut.reset.value = 0
    await FallingEdge(dut.clk)

    q = int(dut.q.value)

    for _ in range(100):
        reset = rand(1)
        dut.reset.value = reset

        if reset:
            q = 0
        else:
            q = (q + 1) % (2**4)

        await FallingEdge(dut.clk)
        assert dut.q.value == q, f"test failed with reset={dut.reset.value}"
