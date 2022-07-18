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

    await RisingEdge(dut.clk)

    dut.areset.value = 1
    await RisingEdge(dut.areset)

    dut.areset.value = 0
    await FallingEdge(dut.areset)

    for d in range(2**8):
        areset = rand(1)

        if areset:
            dut.areset.value = 1
            await RisingEdge(dut.areset)
            
            dut.areset.value = 0
            await FallingEdge(dut.areset)

            assert dut.q.value == 0, f"reset test failed with d={dut.d.value} areset={dut.areset.value} q={dut.q.value}"

        dut.d.value = d
        await FallingEdge(dut.clk)

        assert dut.q.value == d, f"test failed with d={dut.d.value} areset={dut.areset.value} q={dut.q.value}"
