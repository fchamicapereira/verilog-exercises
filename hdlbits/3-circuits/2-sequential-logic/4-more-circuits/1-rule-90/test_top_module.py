import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def shift(d):
    return (d >> 1) & 0xf

def rule90(data):
    _512_bit_mask = 2**512 - 1
    new_data = (data>>1) & 1

    for i in range(1, 511, 1):
        left  = (data>>(i+1)) & 1
        right = (data>>(i-1)) & 1
        value = (left ^ right) & 1
        new_data = new_data | (value << i)
    
    new_data = new_data | (((data>>510) & 1) << 511)
    return new_data & _512_bit_mask

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    data = rand(512)

    dut.load.value = 1
    dut.data.value = data

    await FallingEdge(dut.clk)
    assert dut.data.value == data, f"loading test failed with load={dut.load.value} data={dut.data.value}"

    dut.load.value = 0

    for i in range(1000):
        await FallingEdge(dut.clk)

        data = rule90(data)
        assert dut.q.value == data, f"test failed with load={dut.load.value} data={dut.data.value}"
