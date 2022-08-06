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

A = 0
B = 1

def fsm(i, state):
    o = None

    if state == A:
        state = B if i == 0 else A
    elif state == B:
        state = A if i == 0 else B
    
    o = 1 if state == B else 0
    
    return o, state

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    state = B

    dut.i.value = 1
    dut.present_state.value = state
    dut.reset.value = 1
    await FallingEdge(dut.clk)

    dut.reset.value = 0
    await FallingEdge(dut.clk)

    for _ in range(1000):
        p = 1/10
        reset = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        i = rand(1)

        dut.i.value = i
        dut.reset.value = reset

        await FallingEdge(dut.clk)

        prev = state
        
        if reset:
            state = B
            o = 1
        else:
            o, state = fsm(i, state)

        assert dut.o.value == o, f"test failed with i={dut.i.value} reset={dut.reset.value}"
