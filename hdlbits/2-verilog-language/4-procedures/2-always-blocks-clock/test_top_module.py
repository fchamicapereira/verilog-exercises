import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())
    
    await FallingEdge(dut.clk)

    for i in range(100):
        a = rand(1)
        b = rand(1)

        dut.a.value = a
        dut.b.value = b

        await FallingEdge(dut.clk)

        assert dut.out_assign.value == a ^ b, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, and o={dut.out_assign.value}"
        assert dut.out_always_comb.value == a ^ b, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, and o={dut.out_always_comb.value}"
        assert dut.out_always_ff.value == a ^ b, f"randomized test failed with a={dut.a.value}, b={dut.b.value}, and o={dut.out_always_ff.value}"
