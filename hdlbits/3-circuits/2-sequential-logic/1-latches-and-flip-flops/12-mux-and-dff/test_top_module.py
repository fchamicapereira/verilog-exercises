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

    dut.w.value = 0
    dut.R.value = 0
    dut.E.value = 0
    dut.L.value = 0
    dut.Q.value = 0

    await FallingEdge(dut.clk)

    last_Q = 0
    for w in range(2**1):
        for R in range(2**1):
            for E in range(2**1):
                for L in range(2**1):
                    dut.w.value = w
                    dut.R.value = R
                    dut.E.value = E
                    dut.L.value = L

                    Q = (R if L else (w if E else last_Q))
                    last_Q = Q

                    await FallingEdge(dut.clk)
                    assert dut.Q.value == Q, f"test failed with w={dut.w.value} R={dut.R.value} E={dut.E.value} L={dut.L.value}"
