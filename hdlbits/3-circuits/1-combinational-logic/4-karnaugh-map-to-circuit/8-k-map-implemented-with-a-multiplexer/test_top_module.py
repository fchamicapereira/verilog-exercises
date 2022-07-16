import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def km(c,d):
    mux_in = 0
    mux_in |= (((~(~c & ~d)) & 0b1) << 0)
    mux_in |= ((0 & 0b1) << 1)
    mux_in |= ((((~c & ~d) | (c & ~d)) & 0b1) << 2)
    mux_in |= (((c & d) & 0b1) << 3)
    return mux_in

@cocotb.test()
async def test(dut):
    for c in range(2**1):
        for d in range(2**1):
            dut.c.value = c
            dut.d.value = d

            await Timer(2, units="ns")
            assert dut.mux_in.value == km(c,d), f"test failed with c={dut.c.value} d={dut.d.value} mux_in={dut.mux_in.value}"
