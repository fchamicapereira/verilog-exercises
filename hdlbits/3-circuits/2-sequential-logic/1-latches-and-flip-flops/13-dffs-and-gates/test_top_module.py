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

    dut.x.value = 0

    dut.reset.value = 1
    await FallingEdge(dut.clk)

    dut.reset.value = 0
    await FallingEdge(dut.clk)

    await FallingEdge(dut.clk)

    last_q0 = 0
    last_q1 = 0
    last_q2 = 0

    for _ in range(100):
        x = rand(1)
        
        dut.x.value = x

        q0 = (x ^ last_q0) % 2
        q1 = (x & (~last_q1)) % 2
        q2 = (x | (~last_q2)) % 2

        last_q0 = q0 % 2
        last_q1 = q1 % 2
        last_q2 = q2 % 2

        z = (~(q0 | q1 | q2)) % 2

        await FallingEdge(dut.clk)
        assert dut.z.value == z, f"test failed with x={dut.x.value}"
