import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val        

@cocotb.test()
async def test(dut):
    for _ in range(100):
        a = rand(100)
        b = rand(100)
        cin = rand(1)

        dut.a.value = a
        dut.b.value = b
        dut.cin.value = cin

        await Timer(2, units="ns")
        assert dut.cout.value == int((a+b+cin) / 2**100), f"test failed with a={dut.a.value} b={dut.b.value} cin={dut.cin.value} cout={dut.cout.value} sum={dut.sum.value}"
        assert dut.sum.value == int((a+b+cin) % 2**100), f"test failed with a={dut.a.value} b={dut.b.value} cin={dut.cin.value} cout={dut.cout.value} sum={dut.sum.value}"
