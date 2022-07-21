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

    dut.j.value = 0
    dut.k.value = 0
    dut.Q.value = 0

    await FallingEdge(dut.clk)

    last_q = 0

    for _ in range(1000):
        j = rand(1)
        k = rand(1)
        
        dut.j.value = j
        dut.k.value = k

        if (~j & ~k) % 2:
            q = last_q
        elif (~j & k) % 2:
            q = 0
        elif (j & ~k) % 2:
            q = 1
        else:
            q = (~last_q) % 2

        last_q = q

        await FallingEdge(dut.clk)
        assert dut.Q.value == q, f"test failed with j={dut.j.value} k={dut.k.value}"
