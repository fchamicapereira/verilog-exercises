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
    for i in range(10):
        in1 = rand(1)
        in2 = rand(1)
        in3 = rand(1)
        in4 = rand(1)

        dut.in1.value = in1
        dut.in2.value = in2
        dut.in3.value = in3
        dut.in4.value = in4

        await Timer(2, units="ns")
        assert dut.o1.value == mod_a_o1(in1,in2,in3,in4), f"randomized test failed with in1={dut.in1.value}, in2={dut.in2.value}, and o1={dut.o1.value}"
        assert dut.o2.value == mod_a_o2(in1,in2,in3,in4), f"randomized test failed with in3={dut.in3.value}, in4={dut.in4.value}, and o2={dut.o2.value}"
