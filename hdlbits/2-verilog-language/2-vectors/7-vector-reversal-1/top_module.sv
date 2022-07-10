module top_module(
    input [7:0] i,
    output [7:0] o
  );

  assign o = { i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7] };

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
