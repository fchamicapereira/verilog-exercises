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

def rule110(data):
    _512_bit_mask = 2**512 - 1
    new_data = 0

    for i in range(512):
        left   = (0 if i == 511 else (data>>(i+1))) & 1
        right  = (0 if i == 0 else (data>>(i-1))) & 1
        center = (data >> i) & 1

        truth_table = {
            '111': 0,
            '110': 1,
            '101': 1,
            '100': 0,
            '011': 1,
            '010': 1,
            '001': 1,
            '000': 0,
        }

        value = truth_table[f'{left}{center}{right}'] & 1
        new_data = new_data | (value << i)
    
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

        data = rule110(data)
        assert dut.q.value == data, f"test failed with load={dut.load.value} data={dut.data.value}"
