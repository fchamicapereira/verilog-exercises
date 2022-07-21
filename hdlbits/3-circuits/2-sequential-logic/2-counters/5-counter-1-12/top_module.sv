module count4(
    input clk,
    input enable,
    input load,
    input [3:0] d,
    output reg [3:0] q
  );

  always @(posedge clk)
  begin
    if (load)
      q <= d;
    else if (enable)
      q <= q + 4'b1;
  end
endmodule

module top_module(
    input clk,
    input reset,
    input enable,
    output reg [3:0] Q,
    output reg c_enable,
    output reg c_load,
    output reg [3:0] c_d
  );

  assign c_d = 4'b1;

  always @(*)
  begin
    if (reset)
    begin
      c_load = 1'b1;
      c_enable = 1'b0;
    end
    else if (enable && Q == 4'd12)
    begin
      c_load = 1'b1;
      c_enable = enable;
    end
    else
    begin
      c_load = 1'b0;
      c_enable = enable;
    end
  end

  count4 the_counter (clk, c_enable, c_load, c_d, Q);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
