import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.enable.value = 0
    dut.S.value = 0
    dut.A.value = 0
    dut.B.value = 0
    dut.C.value = 0
    dut.Z.value = 0

    await FallingEdge(dut.clk)

    for i in range(1000):
        data = rand(8)
        
        # writing data to LUT
        dut.enable.value = 1
        for i in range(8):
            dut.S.value = (data >> i) & 1
            await FallingEdge(dut.clk)
        
        dut.enable.value = 0
        await FallingEdge(dut.clk)

        # reading data from LUT
        for i in range(8):
            dut.A.value = (i >> 2) & 1
            dut.B.value = (i >> 1) & 1
            dut.C.value = (i >> 0) & 1
            await FallingEdge(dut.clk)

            Z = (data >> (7-i)) & 1
            assert dut.Z.value == Z, f"test failed with data={bin(data)} ({data}) A={dut.A.value} B={dut.B.value} C={dut.C.value}"
