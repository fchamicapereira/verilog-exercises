import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for a in range(2):
        for b in range(2):
            for cin in range(2):
                dut.a.value = a
                dut.b.value = b
                dut.cin.value = cin

                await Timer(2, units="ns")
                assert dut.cout.value == int((a + b + cin) / 2), f"test failed with a={dut.a.value} b={dut.b.value} cout={dut.cout.value}"
                assert dut.sum.value == (a + b + cin) % 2, f"test failed with a={dut.a.value} b={dut.b.value} sum={dut.sum.value}"
