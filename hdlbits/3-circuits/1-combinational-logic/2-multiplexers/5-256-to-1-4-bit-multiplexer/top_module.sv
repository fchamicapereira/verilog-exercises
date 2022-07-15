module top_module(
    input [1023:0] i,
    input [7:0] sel,
    output [3:0] o
  );

  assign o = i[sel*4 +:4];

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
