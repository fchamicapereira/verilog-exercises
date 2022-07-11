module top_module(
    input a,
    input b,
    output wire out_assign,
    output reg out_alwaysblock
  );

  assign out_assign = a & b;
  always @(*) out_alwaysblock = a & b;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
