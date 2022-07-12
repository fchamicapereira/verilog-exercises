import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def parity(d):
    p = 0
    for b in bin(d)[2:].zfill(8):
        p ^= int(b)
    return p

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(8)

        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.parity.value == parity(i), f"randomized test failed with i={dut.i.value} parity={dut.parity.value}"
