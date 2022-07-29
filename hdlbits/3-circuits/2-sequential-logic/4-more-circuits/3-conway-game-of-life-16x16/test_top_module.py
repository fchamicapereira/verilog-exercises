import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge

import random
import numpy

def rand(bits):
    return random.randint(0, 2**bits - 1)

def shift(d):
    return (d >> 1) & 0xf

def game_of_life(data):
    def cell(d,row,col):
        row = row % 16
        col = col % 16
        return (d>>(row*16+col)) & 1
    
    def update_cell(d,row,col,value):
        row = row % 16
        col = col % 16
        d |= (value << (row*16+col))
        return d
    
    new_data = 0
    grid_mask = 2**(16*16)-1

    for row in range(16):
        for col in range(16):
            neighbours = 0

            neighbours += cell(data,row-1,col-1)
            neighbours += cell(data,row-1,col)
            neighbours += cell(data,row-1,col+1)

            neighbours += cell(data,row,col-1)
            neighbours += cell(data,row,col+1)

            neighbours += cell(data,row+1,col-1)
            neighbours += cell(data,row+1,col)
            neighbours += cell(data,row+1,col+1)

            if neighbours == 2:
                new_data = update_cell(new_data, row, col, cell(data,row,col))
            elif neighbours == 3:
                new_data = update_cell(new_data, row, col, 1)
            else:
                new_data = update_cell(new_data, row, col, 0)
    
    return new_data & grid_mask

@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 1, units="ns")
    cocotb.start_soon(clock.start())

    data = rand(16*16)

    dut.load.value = 1
    dut.data.value = data

    await FallingEdge(dut.clk)
    assert dut.data.value == data, f"loading test failed with load={dut.load.value} data={dut.data.value}"

    dut.load.value = 0

    for i in range(1000):
        # make the probability of reseting really low
        # like 1 / 10000
        p=1/100
        load = int(numpy.random.choice(numpy.arange(0, 2), p=[1-p, p]))
        data_to_load = rand(16*16)

        dut.data.value = data_to_load
        dut.load.value = load

        await FallingEdge(dut.clk)

        if load == 1:
            data = data_to_load
        else:
            data = game_of_life(data)

        assert dut.q.value == data, f"test failed with load={dut.load.value} data={dut.data.value}"
