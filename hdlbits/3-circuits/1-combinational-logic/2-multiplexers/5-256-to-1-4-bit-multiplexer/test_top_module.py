import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for _ in range(100):
        i = rand(1024)
        sel = rand(8)
        
        dut.i.value = i
        dut.sel.value = sel

        await Timer(2, units="ns")
        assert dut.o.value == int(bin(i)[2:].zfill(256)[::-1][sel*4:sel*4+4][::-1], 2), f"test failed with i={dut.i.value} sel={dut.sel.value} o={dut.o.value}"
