module top_module(
    input [31:0] i,
    output [31:0] o
  );

  assign o = { i[7:0], i[15:8],  i[23:16], i[31:24] };

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
