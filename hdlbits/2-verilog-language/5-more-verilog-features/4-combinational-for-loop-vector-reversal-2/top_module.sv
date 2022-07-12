module top_module(
    input [99:0] i,
    output reg [99:0] o
  );

  always @(*)
  begin
    for (int j = 0; j < $bits(o); j++)
    begin
      o[j] = i[$bits(o)-1-j];
    end
  end

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
