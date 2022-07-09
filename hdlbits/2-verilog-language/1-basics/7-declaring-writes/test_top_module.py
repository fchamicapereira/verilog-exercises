import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def out(a,b,c,d):
    return (a & b) | (c & d)

@cocotb.test()
async def test(dut):
    for i in range(10):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0, 1)
        d = random.randint(0, 1)

        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d

        await Timer(2, units="ns")
        assert dut.o.value == out(a,b,c,d) and dut.o_n.value == (~out(a,b,c,d)) % 2, \
            f"randomized test failed with a={dut.a.value}, b={dut.b.value}, " + \
            f"c={dut.c.value}, d={dut.d.value}, o={dut.o.value} o_n={dut.o_n.value}"
