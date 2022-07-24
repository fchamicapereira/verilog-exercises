module top_module(
    input clk,
    input reset,    // Active-high synchronous reset to 5'h1
    output reg [4:0] q
  );

  always @(posedge clk)
  begin
    if (reset)
      q <= 5'b1;
    else
    begin
      q[4] <= q[0];
      q[3] <= q[4];
      q[2] <= q[3] ^ q[0];
      q[1] <= q[2];
      q[0] <= q[1];
    end
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
