import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def muxdff(w, R, E, L, last_Q):
    Q = (R if L else (w if E else last_Q))
    return Q

def shift_register(ledr, sw, key):
    # MUXDFF muxdff0(clk, LEDR[1], SW[0], KEY[1], KEY[2], LEDR[0]);
    # MUXDFF muxdff1(clk, LEDR[2], SW[1], KEY[1], KEY[2], LEDR[1]);
    # MUXDFF muxdff2(clk, LEDR[3], SW[2], KEY[1], KEY[2], LEDR[2]);
    # MUXDFF muxdff3(clk, KEY[3],  SW[3], KEY[1], KEY[2], LEDR[3]);

    ledr0 = muxdff((ledr>>1)&1, (sw>>0)&1, (key>>0)&1, (key>>1)&1, (ledr>>0)&1)
    ledr1 = muxdff((ledr>>2)&1, (sw>>1)&1, (key>>0)&1, (key>>1)&1, (ledr>>1)&1)
    ledr2 = muxdff((ledr>>3)&1, (sw>>2)&1, (key>>0)&1, (key>>1)&1, (ledr>>2)&1)
    ledr3 = muxdff((key>>2)&1,  (sw>>3)&1, (key>>0)&1, (key>>1)&1, (ledr>>3)&1)

    return (ledr0 | (ledr1<<1) | (ledr2<<2) | (ledr3<<3)) & 0b1111

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.SW.value = 0
    dut.KEY.value = 0
    dut.LEDR.value = 0

    await FallingEdge(dut.clk)

    ledr = dut.LEDR.value
    for i in range(1000):
        sw = rand(4)
        key = rand(3)

        dut.SW.value = sw
        dut.KEY.value = key

        await FallingEdge(dut.clk)

        ledr = shift_register(ledr, sw, key)
        assert dut.LEDR.value == ledr, f"test failed with sw={dut.SW.value} key={dut.KEY.value}"      
