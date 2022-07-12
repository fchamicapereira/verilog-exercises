import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def priority_encoder(d):
    for i,b in enumerate(bin(d)[2:].zfill(4)[::-1]):
        if b == "1":
            return i
    return 0

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(4)

        dut.i.value = i
        await Timer(2, units="ns")

        assert dut.pos.value == priority_encoder(i), f"randomized test failed with i={dut.i.value} pos={dut.pos.value}"
