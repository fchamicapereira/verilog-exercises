import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def xnor(a,b,c,d,e):
    _a = bin(a)[2:]
    _b = bin(b)[2:]
    _c = bin(c)[2:]
    _d = bin(d)[2:]
    _e = bin(e)[2:]

    top = 5*_a + 5*_b + 5*_c + 5*_d + 5*_e
    bottom = 5*(_a+_b+_c+_d+_e)

    top = int(top,2)
    bottom = int(bottom,2)

    return (~top ^ bottom) % (2 ** 25)

@cocotb.test()
async def test(dut):
    for i in range(10):
        a = rand(1)
        b = rand(1)
        c = rand(1)
        d = rand(1)
        e = rand(1)

        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d
        dut.e.value = e

        await Timer(2, units="ns")
        assert dut.o.value == xnor(a,b,c,d,e), \
            f"test failed with a={dut.a.value},b={dut.b.value}," + \
            f"c={dut.c.value},d={dut.d.value},e={dut.e.value},o={dut.o.value}"

