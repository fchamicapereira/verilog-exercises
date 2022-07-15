module top_module(
    input a, b,
    output cout, sum
  );

  assign sum = a ^ b;
  assign cout = a & b;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
