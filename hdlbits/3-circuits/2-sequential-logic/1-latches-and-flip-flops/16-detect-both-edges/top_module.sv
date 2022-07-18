module top_module(
    input clk,
    input [7:0] i,
    output reg [7:0] anyedge
  );

  reg [7:0] last_in;
  always @(posedge clk)
  begin
    last_in <= i;
    anyedge <= i ^ last_in;
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
