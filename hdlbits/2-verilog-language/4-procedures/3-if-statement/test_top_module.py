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
        a = rand(1)
        b = rand(1)

        sel_b1 = rand(1)
        sel_b2 = rand(1)

        dut.a.value = a
        dut.b.value = b

        dut.sel_b1.value = sel_b1
        dut.sel_b2.value = sel_b2

        await Timer(2, units="ns")

        if sel_b1 == 1 and sel_b2 == 1:
            assert dut.out_assign.value == b, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, sel_b1={dut.sel_b1.value}, sel_b2={dut.sel_b2.value}, and o={dut.out_assign.value}"
            assert dut.out_always.value == b, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, sel_b1={dut.sel_b1.value}, sel_b2={dut.sel_b2.value}, and o={dut.out_always.value}"
        else:
            assert dut.out_assign.value == a, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, sel_b1={dut.sel_b1.value}, sel_b2={dut.sel_b2.value}, and o={dut.out_assign.value}"
            assert dut.out_always.value == a, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, sel_b1={dut.sel_b1.value}, sel_b2={dut.sel_b2.value}, and o={dut.out_always.value}"
