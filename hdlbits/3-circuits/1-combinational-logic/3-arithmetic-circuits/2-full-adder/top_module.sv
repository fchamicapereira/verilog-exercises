module top_module(
    input a, b, cin,
    output cout, sum
  );

  assign sum = a ^ b ^ cin;
  assign cout = (a & b) | (a & cin) | (b & cin);

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
