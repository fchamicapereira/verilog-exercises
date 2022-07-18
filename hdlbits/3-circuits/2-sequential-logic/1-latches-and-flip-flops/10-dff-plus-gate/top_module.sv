module top_module(
    input clk,
    input i,
    output reg o
  );

  always @(posedge clk)
  begin
    o <= i ^ o;
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
