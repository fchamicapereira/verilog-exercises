import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for a in range(2):
        for b in range(2):
            for sel in range(2):
                dut.a.value = a
                dut.b.value = b
                dut.sel.value = sel

                await Timer(2, units="ns")
                assert dut.out.value == (a if sel == 0 else b), f"test failed with a={dut.a.value} b={dut.b.value} sel={dut.sel.value} out={dut.out.value}"
