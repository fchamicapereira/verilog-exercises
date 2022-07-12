import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import FallingEdge

import random

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    for a in range(2):
        for b in range(2):
            dut.a.value = a
            dut.b.value = b

            await Timer(2, units="ns")
            assert dut.out_and.value == (a & b) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_and={dut.out_and.value}"
            assert dut.out_or.value == (a | b) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_or={dut.out_or.value}"
            assert dut.out_xor.value == (a ^ b) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_xor={dut.out_xor.value}"
            assert dut.out_nand.value == (~(a & b)) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_nand={dut.out_nand.value}"
            assert dut.out_nor.value == (~(a | b)) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_nor={dut.out_nor.value}"
            assert dut.out_xnor.value == (~(a ^ b)) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_xnor={dut.out_xnor.value}"
            assert dut.out_anotb.value == (a & ~b) % 2, f"test failed with a={dut.a.value} b={dut.b.value} out_anotb={dut.out_anotb.value}"
