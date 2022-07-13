module top_module(
    input [3:0] i,
    output [2:0] out_both,
    output [3:1] out_any,
    output [3:0] out_different
  );

  assign out_both = i[2:0] & i[3:1];
  assign out_any = i[3:1] | i[2:0];
  assign out_different = i ^ {i[0], i[3:1]};

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
