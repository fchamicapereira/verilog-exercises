import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

STATE_A = 0
STATE_B = 1

def rand(bits):
    return random.randint(0, 2**bits - 1)

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    dut.i.value = 1
    dut.state.value = STATE_B

    dut.areset.value = 1
    await RisingEdge(dut.areset)

    dut.areset.value = 0
    await FallingEdge(dut.areset)

    state = STATE_B
    await FallingEdge(dut.clk)

    for _ in range(1000):
        p = 1/10
        areset = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        i = rand(1)

        dut.i.value = i

        if areset:
            dut.areset.value = 1
            await RisingEdge(dut.areset)
            
            dut.areset.value = 0
            await FallingEdge(dut.areset)

            state = STATE_B
            assert dut.o.value == state, f"reset test failed with i={dut.i.value} areset={dut.areset.value}"
    

        await FallingEdge(dut.clk)
        if i == 0: state = STATE_A if state == STATE_B else STATE_B

        assert dut.o.value == state, f"test failed with i={dut.i.value} areset={dut.areset.value}"
