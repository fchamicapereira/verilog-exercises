import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def km(a,b,c,d):
    return (~(
        (a & b  & ~c & ~d) | (~a & b & ~c & d) | (a & b & ~c & d) | (~a & ~b & c & d) | (a & b & c & ~d) | (a & ~b & c & ~d)
    )) % 2
    
@cocotb.test()
async def test(dut):
    for a in range(1):
        for b in range(1):
            for c in range(1):
                for d in range(1):
                    dut.a.value = a
                    dut.b.value = b
                    dut.c.value = c
                    dut.d.value = d

                    await Timer(2, units="ns")
                    assert dut.out.value == km(a,b,c,d), f"test failed with a={dut.a.value} b={dut.b.value} c={dut.c.value} d={dut.d.value} out={dut.out.value}"
