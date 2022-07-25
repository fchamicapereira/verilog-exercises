import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def lfsr(ledr, key1, sw):
    ledr0 = ((sw >> 0) & 0b1) if key1 & 0b1 else ((ledr >> 2) & 0b1)
    ledr1 = ((sw >> 1) & 0b1) if key1 & 0b1 else ((ledr >> 0) & 0b1)
    ledr2 = ((sw >> 2) & 0b1) if key1 & 0b1 else (((ledr >> 1) ^ (ledr >> 2)) & 0b1)

    return ((ledr2 << 2) | (ledr1 << 1) | ledr0 ) & 0b111

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    ledr = 0
    dut.SW.value = 0
    dut.L.value = 0
    dut.LEDR.value = ledr

    await FallingEdge(dut.clk)
    print(dut.clk, dut.LEDR.value)

    for i in range(1000):
        sw = rand(3)
        l = rand(1)

        dut.SW.value = sw
        dut.L.value = l

        await FallingEdge(dut.clk)

        ledr = lfsr(ledr, l, sw)
        
        assert dut.LEDR.value == ledr, f"test failed with sw={dut.SW.value} l={dut.L.value}"
