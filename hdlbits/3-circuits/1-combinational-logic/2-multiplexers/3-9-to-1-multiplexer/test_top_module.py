import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for _ in range(100):
        a = rand(16)
        b = rand(16)
        c = rand(16)
        d = rand(16)
        e = rand(16)
        f = rand(16)
        g = rand(16)
        h = rand(16)
        i = rand(16)

        sel = rand(4)
        
        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d
        dut.e.value = e
        dut.f.value = f
        dut.g.value = g
        dut.h.value = h
        dut.i.value = i

        dut.sel.value = sel
        s = [ a, b, c, d, e, f, g, h, i ]

        await Timer(2, units="ns")
        assert dut.out.value == (s[sel] if sel < len(s) else 0xffff), f"test failed with a={dut.a.value} b={dut.b.value} sel={dut.sel.value} out={dut.out.value}"
