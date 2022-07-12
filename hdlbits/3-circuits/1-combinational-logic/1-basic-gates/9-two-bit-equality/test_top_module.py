import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for A in range(2**2):
        for B in range(2**2):
            dut.A.value = A
            dut.B.value = B

            await Timer(2, units="ns")
            assert dut.z.value == (1 if (A == B) else 0), f"test failed with A={dut.A.value} B={dut.B.value} z={dut.z.value}"
