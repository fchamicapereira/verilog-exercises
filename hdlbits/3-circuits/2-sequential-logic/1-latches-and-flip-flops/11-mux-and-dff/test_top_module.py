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

    dut.L.value = 0
    dut.r_in.value = 0
    dut.q_in.value = 0

    await FallingEdge(dut.clk)

    for L in range(2**1):
        for r_in in range(2**1):
            for q_in in range(2**1):
                dut.L.value = L
                dut.r_in.value = r_in
                dut.q_in.value = q_in

                await FallingEdge(dut.clk)
                assert dut.Q.value == (r_in if L else q_in), f"test failed with L={dut.L.value} r_in={dut.r_in.value} q_in={dut.q_in.value}"
