module top_module(
    input [99:0] i,
    output out_and,
    output out_or,
    output out_xor
  );

  assign out_and = & i[99:0];
  assign out_or  = | i[99:0];
  assign out_xor = ^ i[99:0];

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
