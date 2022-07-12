import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def out_and(d):
    res = 0
    for b in bin(d)[2:].zfill(100):
        res &= int(b)
    return res

def out_or(d):
    res = 0
    for b in bin(d)[2:].zfill(100):
        res |= int(b)
    return res

def out_xor(d):
    res = 0
    for b in bin(d)[2:].zfill(100):
        res ^= int(b)
    return res

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(100)

        dut.i.value = i

        await Timer(2, units="ns")
        assert dut.out_and.value == out_and(i), f"randomized test failed with i={dut.i.value} out_and={dut.out_and.value}"
        assert dut.out_or.value == out_or(i), f"randomized test failed with i={dut.i.value} out_and={dut.out_or.value}"
        assert dut.out_xor.value == out_xor(i), f"randomized test failed with i={dut.i.value} out_and={dut.out_xor.value}"
