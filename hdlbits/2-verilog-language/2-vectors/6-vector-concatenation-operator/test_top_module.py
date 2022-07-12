import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for i in range(100):
        a = rand(5)
        b = rand(5)
        c = rand(5)
        d = rand(5)
        e = rand(5)
        f = rand(5)

        dut.a.value = a
        dut.b.value = b
        dut.c.value = c
        dut.d.value = d
        dut.e.value = e
        dut.f.value = f

        final = "".join([ bin(x)[2:].zfill(5) for x in [ a,b,c,d,e,f ] ]) + "11"

        w = int(final[0:8], 2)
        x = int(final[8:16], 2)
        y = int(final[16:24], 2)
        z = int(final[24:32], 2)

        await Timer(2, units="ns")
        assert dut.w.value == w, f"w test failed with a={dut.a.value},b={dut.b.value},w={dut.w.value}"
        assert dut.x.value == x, f"x test failed with b={dut.b.value},c={dut.c.value},d={dut.d.value},x={dut.x.value}"
        assert dut.y.value == y, f"y test failed with d={dut.d.value},e={dut.e.value},y={dut.y.value}"
        assert dut.z.value == z, f"z test failed with e={dut.e.value},f={dut.f.value},z={dut.z.value}"

