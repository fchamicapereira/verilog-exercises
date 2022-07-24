import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def rotate(d, direction):
    hundred_bit_mask = 0xfffffffffffffffffffffffff

    if direction == 0b01:
        rbit = d & 0b1
        return ((d >> 1) | (rbit << 99)) & hundred_bit_mask
    elif direction == 0b10:
        lbit = (d >> 99) & 0b1
        return ((d << 1) | lbit) & hundred_bit_mask
    else:
        return d & hundred_bit_mask

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    q = 1
    dut.q.value = 1
    await FallingEdge(dut.clk)

    for i in range(1000):
        p=1/150

        load = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        ena = rand(2)
        data = rand(100)
        
        dut.load.value = load
        dut.ena.value = ena
        dut.data.value = data

        await FallingEdge(dut.clk)

        if load:
            q = data
        else:
            q = rotate(q, ena)

        assert dut.q.value == q, f"test failed with load={dut.load.value} ena={dut.ena.value} data={dut.data.value}"
