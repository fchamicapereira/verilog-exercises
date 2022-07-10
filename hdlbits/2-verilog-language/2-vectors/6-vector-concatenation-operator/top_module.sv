module top_module(
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z
  );

  assign { w, x, y, z } = { a, b, c, d, e, f, 2'b11 };

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
