import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def out_both(i):
    res = 0
    for b in range(99):
        both = (i & 1) & ((i >> 1) & 1)
        res = res | (both << b)
        i = i >> 1
    return res

def out_any(i):
    res = 0
    for b in range(99):
        _any = ((i >> 1) & 1) | (i & 1)
        res = res | (_any << b)
        i = i >> 1
    return res

def out_different(i):
    res = 0
    first_bit = i & 1
    for b in range(100):
        if b == 99:
            diff = (i & 1) ^ first_bit
        else:
            diff = (i & 1) ^ ((i >> 1) & 1)
        res = res | (diff << b)
        i = i >> 1
    return res

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(100)
        dut.i.value = i
        await Timer(2, units="ns")
        assert dut.out_both.value == out_both(i), f"out_both test failed with i={dut.i.value} out_both={dut.out_both.value}"
        assert dut.out_any.value == out_any(i), f"out_any test failed with i={dut.i.value} out_any={dut.out_any.value}"
        assert dut.out_different.value == out_different(i), f"out_different test failed with i={dut.i.value} out_different={dut.out_different.value}"
