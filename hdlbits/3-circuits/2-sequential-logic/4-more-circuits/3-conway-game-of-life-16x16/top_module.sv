module top_module#(
    parameter GRID_WIDTH=16
  )(
    input clk,
    input load,
    input [GRID_WIDTH*GRID_WIDTH-1:0] data,
    output reg [GRID_WIDTH*GRID_WIDTH-1:0] q
  );

  logic [3:0] neighbours;
  logic [4:0] t, b, l, r;
  logic [GRID_WIDTH*GRID_WIDTH-1:0] new_q;

  always_comb
  begin
    for (int row = 0; row < GRID_WIDTH; row++)
    begin
      for (int col = 0; col < GRID_WIDTH; col++)
      begin
        t = (row == GRID_WIDTH - 1) ? 0 : (row + 1);
        b = (row == 0) ? (GRID_WIDTH - 1) : (row - 1);
        l = (col == GRID_WIDTH - 1) ? 0 : (col + 1);
        r = (col == 0) ? (GRID_WIDTH - 1) : (col - 1);

        neighbours = q[t*GRID_WIDTH+l] + q[row*GRID_WIDTH+l] + q[b*GRID_WIDTH+l]
                   + q[t*GRID_WIDTH+col] + q[b*GRID_WIDTH+col]
                   + q[t*GRID_WIDTH+r] + q[row*GRID_WIDTH+r] + q[b*GRID_WIDTH+r];

        if (neighbours == 4'd0 || neighbours == 4'd1 || neighbours >= 4'd4)
          new_q[row*GRID_WIDTH+col] = 1'b0;
        else if (neighbours == 4'd3)
          new_q[row*GRID_WIDTH+col] = 1'b1;
        else
          new_q[row*GRID_WIDTH+col] = q[row*GRID_WIDTH+col];
      end
    end
  end

  always @(posedge clk)
  begin
    if (load)
      q <= data;
    else
      q <= new_q;
  end

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
