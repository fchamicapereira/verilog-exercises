module bcdcount(
    input clk,
    input reset,
    input enable,
    output reg [3:0] q
  );

  always @(posedge clk)
  begin
    if (reset)
      q <= 4'b0;
    else if (enable)
    begin
      if (q == 4'd9)
        q <= 0;
      else
        q <= q + 4'b1;
    end
  end
endmodule


module top_module(
    input clk,
    input reset,
    output reg OneHertz,
    output reg [2:0] c_enable
  );

  wire [3:0] one, ten, hundred;

  assign c_enable = { one == 4'd9 && ten == 4'd9, one == 4'd9, 1'b1 };
  assign OneHertz = (one == 4'd9) & (ten == 4'd9) & (hundred == 4'd9);

  bcdcount counter0 (clk, reset, c_enable[0], one);
  bcdcount counter1 (clk, reset, c_enable[1], ten);
  bcdcount counter2 (clk, reset, c_enable[2], hundred);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
