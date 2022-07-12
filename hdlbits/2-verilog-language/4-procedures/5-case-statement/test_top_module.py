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
        sel = rand(3)
        datas = [ rand(4) for x in range(6) ]

        dut.sel.value = sel
        dut.data0.value = datas[0]
        dut.data1.value = datas[1]
        dut.data2.value = datas[2]
        dut.data3.value = datas[3]
        dut.data4.value = datas[4]
        dut.data5.value = datas[5]

        await Timer(2, units="ns")

        o = 0 if sel > 5 else datas[sel]
        assert dut.o.value == o, f"randomized test failed with sel={dut.sel.value}"
