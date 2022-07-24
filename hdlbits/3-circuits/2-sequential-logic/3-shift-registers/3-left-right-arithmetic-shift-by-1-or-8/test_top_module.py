import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def _64b_arithmetic_shift(d, amount):
    _64_bit_mask = (2**64)-1
    if amount == 0b00:
        return (d << 1) & _64_bit_mask
    elif amount == 0b01:
        return (d << 8) & _64_bit_mask
    elif amount == 0b10:
        msb = (d >> 63) & 0b1
        return ((d >> 1) | (msb << 63)) & _64_bit_mask
    elif amount == 0b11:
        msb = (d >> 63) & 0b1
        for _ in range(8):
            d = ((d >> 1) | (msb << 63)) & _64_bit_mask
        return d

    assert(False and "Should not be here")

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    q = 1
    dut.q.value = 1
    await FallingEdge(dut.clk)

    for i in range(10000):
        p=1/150

        load = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        ena = rand(1)
        amount = rand(2)
        data = rand(64)
        
        dut.load.value = load
        dut.ena.value = ena
        dut.amount.value = amount
        dut.data.value = data

        await FallingEdge(dut.clk)

        if load:
            q = data
        elif ena:
            q = _64b_arithmetic_shift(q, amount)

        assert dut.q.value == q, f"test failed with load={dut.load.value} ena={dut.ena.value} amount={dut.amount.value} data={dut.data.value}"
