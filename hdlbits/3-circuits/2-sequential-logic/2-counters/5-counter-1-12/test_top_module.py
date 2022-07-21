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
    dut.Q.value = 1
    await FallingEdge(dut.clk)

    dut.reset.value = 0
    await FallingEdge(dut.clk)

    q = int(dut.Q.value)

    for _ in range(1000):
        # lets make reseting lets probable...
        # lets say 1/32
        reset = 1 if rand(5) == 0 else 0

        enable = rand(1)

        dut.reset.value = reset
        dut.enable.value = enable

        if reset:
            q = 1
        elif enable:
            if q == 12:
                q = 1
            else:
                q = (q + 1) % (2**4)

        await FallingEdge(dut.clk)
        assert dut.Q.value == q, f"test failed with reset={dut.reset.value} enable={dut.enable.value}"
