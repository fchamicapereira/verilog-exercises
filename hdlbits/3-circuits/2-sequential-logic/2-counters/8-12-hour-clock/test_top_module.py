import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def twelve_hour_clock(hh,mm,ss,pm):
    if ss == 59:
        ss = 0
        if mm == 59:
            mm = 0
            if hh == 12:
                hh = 1
            else:
                hh += 1
        else:
            mm += 1
    else:
        ss += 1
    
    if hh == 12 and mm == 00 and ss == 00:
        pm = 1 if pm == 0 else 0
    
    return hh,mm,ss,pm

def int_to_bcd(d):
    return (((int(d/10) << 4) & 0xff) | ((d % 10) & 0xff)) & 0xffff

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.reset.value = 1
    dut.ena.value = 1
    await FallingEdge(dut.clk)

    hh = 12
    mm = 0
    ss = 0
    pm = 0

    hour_laps=10
    seconds_in_hour=60*60

    for i in range(hour_laps * seconds_in_hour):
        # make the probability of reseting really low
        p = 2 / (hour_laps * seconds_in_hour)
        reset = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        dut.reset.value = reset

        await FallingEdge(dut.clk)

        if reset:
            hh = 12
            mm = 0
            ss = 0
            pm = 0  
        else:        
            hh,mm,ss,pm = twelve_hour_clock(hh,mm,ss,pm)
        
        assert dut.hh.value == int_to_bcd(hh), f"wrong hours reset={dut.reset.value}"
        assert dut.mm.value == int_to_bcd(mm), f"wrong minutes reset={dut.reset.value}"
        assert dut.ss.value == int_to_bcd(ss), f"wrong seconds reset={dut.reset.value}"
        assert dut.pm.value == pm, f"wrong pm reset={dut.reset.value}"
