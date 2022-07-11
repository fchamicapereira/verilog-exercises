import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    T = 2
    T_units = "ns"

    clock = Clock(dut.clk, T, units=T_units)
    cocotb.start_soon(clock.start())

    await FallingEdge(dut.clk)
    dut.d.value = 0
    await Timer(3*T, units=T_units)
    await FallingEdge(dut.clk)

    prev_d = 0
    for i in range(10):
        await FallingEdge(dut.clk)

        d = 1 if prev_d == 0 else 0
        dut.d.value = d

        await FallingEdge(dut.clk)
        assert dut.q.value != d, f"randomized test failed with i={i}, T=1, prev={prev_d}, d={dut.d.value}, q={dut.q.value}"

        await FallingEdge(dut.clk)
        assert dut.q.value != d, f"randomized test failed with i={i}, T=2, prev={prev_d}, d={dut.d.value}, q={dut.q.value}"

        await FallingEdge(dut.clk)
        assert dut.q.value == d, f"randomized test failed with i={i}, T=3, prev={prev_d}, d={dut.d.value}, q={dut.q.value}"

        prev_d = d
