module top_module(
    input [3:0] i,
    output o_and,
    output o_or,
    output o_xor
  );

  assign o_and = i[0] & i[1] & i[2] & i[3];
  assign o_or  = i[0] | i[1] | i[2] | i[3];
  assign o_xor = i[0] ^ i[1] ^ i[2] ^ i[3];

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
