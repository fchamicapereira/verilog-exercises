import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    dut.d.value = 0
    dut.ena.value = 1
    await Timer(2, units="ns")

    last_d = 0

    for d in range(2**1):
        for ena in range(2**1):
            dut.d.value = d
            dut.ena.value = ena

            q = d if ena else last_d

            await Timer(2, units="ns")
            assert dut.q.value == q, f"test failed with d={dut.d.value} ena={dut.ena.value} q={dut.q.value}"

            last_d = q
