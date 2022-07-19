module top_module(
    input clk,
    input reset,
    input [31:0] i,
    output reg [31:0] o
  );

  reg [31:0] last_in;
  always @(posedge clk)
  begin
    last_in <= i;
    if (reset)
      o <= 32'b0;
    else
      o <= (last_in & ~i) | o;
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
