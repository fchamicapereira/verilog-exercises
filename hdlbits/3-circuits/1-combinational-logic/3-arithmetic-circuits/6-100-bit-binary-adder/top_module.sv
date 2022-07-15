module top_module (
    input [99:0] a, b,
    input cin,
    output cout,
    output [99:0] sum
  );

  assign {cout, sum}  = a + b + cin;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
