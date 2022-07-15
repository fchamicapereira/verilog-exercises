import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def km(a,b,c,d):
    return (
        (c&d) | (~a&~b&c&~d)
    ) % 2
    
@cocotb.test()
async def test(dut):
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    dut.a.value = a
                    dut.b.value = b
                    dut.c.value = c
                    dut.d.value = d

                    await Timer(2, units="ns")
                    assert dut.out_sop.value == km(a,b,c,d), f"test failed with a={dut.a.value} b={dut.b.value} c={dut.c.value} d={dut.d.value} out_sop={dut.out_sop.value}"
                    assert dut.out_pos.value == km(a,b,c,d), f"test failed with a={dut.a.value} b={dut.b.value} c={dut.c.value} d={dut.d.value} out_pos={dut.out_pos.value}"
