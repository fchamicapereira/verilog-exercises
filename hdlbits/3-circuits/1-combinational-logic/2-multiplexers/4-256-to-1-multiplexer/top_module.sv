module top_module(
    input [255:0] i,
    input [7:0] sel,
    output o
  );

  assign o = i[sel];

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
