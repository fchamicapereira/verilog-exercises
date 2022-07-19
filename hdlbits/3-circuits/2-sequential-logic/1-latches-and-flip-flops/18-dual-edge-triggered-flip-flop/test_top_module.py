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

    dut.d.value = 0
    dut.p.value = 0
    dut.n.value = 0
    dut.q.value = 0
    last_q = 0

    await FallingEdge(dut.clk)

    for _ in range(100):
        d = rand(1)
        dut.d.value = d

        await RisingEdge(dut.clk)
        assert dut.q.value == last_q, f"rising test failed with d={dut.d.value}"

        last_q = d
        d = rand(1)
        dut.d.value = d

        await FallingEdge(dut.clk)
        assert dut.q.value == last_q, f"falling test failed with d={dut.d.value}"

        last_q = d
