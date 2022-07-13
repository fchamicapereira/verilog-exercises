module top_module( input [1:0] A, input [1:0] B, output z );
  assign z = (A==B) ? 1'b1 : 1'b0;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
