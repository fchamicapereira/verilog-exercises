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

    dut.sel.value = 0
    dut.d.value = 0
    await FallingEdge(dut.clk)

    assert dut.sel.value == 0, f"FAILED init: i={i}, j={j}, prev={prev_d}, sel={dut.sel.value} d={dut.d.value}, q={dut.q.value}"
    assert dut.q.value == 0, f"FAILED init: i={i}, j={j}, prev={prev_d}, sel={dut.sel.value} d={dut.d.value}, q={dut.q.value}"

    prev_d = 0
    for i in range(100):
        for sel in range(4):
            d = rand(8)

            dut.sel.value = sel
            dut.d.value = d

            await FallingEdge(dut.clk)

            # wait for it...
            for j in range(sel-2):
                await FallingEdge(dut.clk)
                assert dut.q.value == prev_d, f"FAILED: i={i}, j={j}, prev={prev_d}, sel={dut.sel.value}, d={dut.d.value}, q={dut.q.value}"

            await FallingEdge(dut.clk)
            assert dut.q.value == d, f"FAILED: i={i}, prev={prev_d}, sel={dut.sel.value}, d={dut.d.value}, q={dut.q.value}"
            prev_d = d
