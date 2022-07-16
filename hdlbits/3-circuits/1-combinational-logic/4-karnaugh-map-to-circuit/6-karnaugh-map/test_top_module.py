import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def km(x1,x2,x3,x4):
    return (
        (x3 & ~x1) | (x1&x2&~x3&x4)
    ) % 2
    
@cocotb.test()
async def test(dut):
    for x in range(2**4):
        dut.x.value = x

        await Timer(2, units="ns")
        assert dut.f.value == km((x>>0)&1,(x>>1)&1,(x>>2)&1,(x>>3)&1), f"test failed with x={dut.x.value} f={dut.f.value}"
