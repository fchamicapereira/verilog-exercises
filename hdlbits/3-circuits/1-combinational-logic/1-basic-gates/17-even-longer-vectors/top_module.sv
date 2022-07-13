module top_module(
    input [99:0] i,
    output [98:0] out_both,
    output [99:1] out_any,
    output [99:0] out_different
  );
  assign out_both      = i[98:0] & i[99:1];
  assign out_any       = i[99:1] | i[98:0];
  assign out_different = i ^ { i[0], i[99:1] };

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
