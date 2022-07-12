module top_module(
    input [7:0] i,
    output parity
  );

  assign parity = ^i[7:0];

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
