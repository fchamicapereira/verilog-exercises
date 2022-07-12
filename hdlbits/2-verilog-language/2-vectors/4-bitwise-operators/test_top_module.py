import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def out_or_bitwise(a,b):
    return a | b

def out_or_logical(a,b):
    return 0 if (a | b) == 0 else 1

def out_not(a,b):
    return (((~b) % 2**3) << 3) | (((~a) % 2**3) << 0)

@cocotb.test()
async def test(dut):
    for i in range(100):
        a = rand(3)
        b = rand(3)

        dut.a.value = a
        dut.b.value = b

        await Timer(2, units="ns")

        assert dut.out_or_bitwise.value == out_or_bitwise(a,b), f"out_or_bitwise test failed with a={dut.a.value}, b={dut.b.value}, out_or_bitwise={dut.out_or_bitwise.value}"
        assert dut.out_or_logical.value == out_or_logical(a,b), f"out_or_logical test failed with a={dut.a.value}, b={dut.b.value}, out_or_logical={dut.out_or_logical.value}"
        assert dut.out_not.value == out_not(a,b), f"out_not test failed with a={dut.a.value}, b={dut.b.value}, out_not={dut.out_not.value}"
        