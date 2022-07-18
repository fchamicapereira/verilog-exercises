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

    dut.resetn.value = 0
    await RisingEdge(dut.clk)

    dut.resetn.value = 1
    await RisingEdge(dut.clk)

    last_d = 0

    for d in range(2**8):
        for byteena in range(2**1):
            for resetn in range(2**1):
                dut.resetn.value = resetn
                dut.byteena.value = byteena
                dut.d.value = d

                if (~resetn) % 2:
                    q = 0
                else:
                    q = last_d

                    if byteena & 1:
                        q |= d & 0xff
                    if (byteena >> 1) & 1:
                        q |= d & 0xff00

                await FallingEdge(dut.clk)
                assert dut.q.value == q, f"test failed with d={dut.d.value} byteena={dut.byteena.value} resetn={dut.resetn.value} q={dut.q.value}"

                last_d = q
