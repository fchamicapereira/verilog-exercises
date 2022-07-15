import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def mod_a_o1(in1,in2,in3,in4):
    return in1 | in2

def mod_a_o2(in1,in2,in3,in4):
    return in3 & in4

@cocotb.test()
async def test(dut):
    for i in range(100):
        a = rand(1)
        b = rand(1)
        c = rand(1)
        d = rand(1)

        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d

        await Timer(2, units="ns")
        assert dut.o1.value == mod_a_o1(a,b,c,d), f"randomized test failed with a={dut.a.value}, b={dut.b.value}, and o1={dut.o1.value}"
        assert dut.o2.value == mod_a_o2(a,b,c,d), f"randomized test failed with c={dut.c.value}, d={dut.d.value}, and o2={dut.o2.value}"
