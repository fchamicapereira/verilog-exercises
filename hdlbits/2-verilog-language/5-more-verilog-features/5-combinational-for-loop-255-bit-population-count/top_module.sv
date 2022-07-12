module top_module(
    input [254:0] i,
    output reg [7:0] o
  );
  always @(*)
  begin
    o = 0;
    for(int j = 0; j < $bits(i); j++)
    begin
      o = o + i[j];
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
