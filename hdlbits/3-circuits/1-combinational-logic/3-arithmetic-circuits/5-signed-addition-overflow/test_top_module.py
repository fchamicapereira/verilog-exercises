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
        a = rand(8)
        b = rand(8)

        dut.a.value = a
        dut.b.value = b

        _a = twos_comp(a,8)
        _b = twos_comp(b,8)
        _s = twos_comp((a+b) & 0xff,8)

        await Timer(2, units="ns")
        assert dut.s.value == (a+b) % 2**8, f"test failed with a={dut.a.value} b={dut.b.value} s={dut.s.value}"
        assert dut.overflow.value == (1 if ((_a*_b > 0) and (_s*_a < 0)) else 0), f"test failed with a={dut.a.value} b={dut.b.value} s={dut.s.value} overflow={dut.overflow.value}"
