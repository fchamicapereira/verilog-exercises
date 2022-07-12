import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

def bcd_add(d1, d2, cin):
    assert(len(bin(d1)[2:]) <= 4)
    assert(len(bin(d2)[2:]) <= 4)
    assert(cin == 0 or cin == 1)

    return (d1 + d2 + cin) % (2**4), int((d1 + d2 + cin) / (2**4))

def bcd_100d_add(d1, d2, cin):
    res = 0

    for i in range(100):
        _d1 = d1 & 0b1111
        _d2 = d2 & 0b1111

        s, cout = bcd_add(_d1, _d2, cin)
        res += s << (i * 4)

        d1 = d1 >> 4
        d2 = d2 >> 4
        cin = cout
    
    return res, cin

@cocotb.test()
async def test(dut):
    for _ in range(100):
        a = rand(400)
        b = rand(400)
        cin = rand(1)

        dut.a.value = a
        dut.b.value = b
        dut.cin.value = cin

        await Timer(2, units="ns")
        res, cout = bcd_100d_add(a,b,cin)

        assert dut.sum.value == res, f"randomized test failed with a={dut.a.value} b={dut.b.value} cin={dut.cin.value} sum={dut.sum.value} cout={dut.cout.value}"
        assert dut.cout.value == cout, f"randomized test failed with a={dut.a.value} b={dut.b.value} cin={dut.cin.value} sum={dut.sum.value} cout={dut.cout.value}"
