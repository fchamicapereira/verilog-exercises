module top_module(
    input clk,
    input load,
    input [511:0] data,
    output reg [511:0] q
  );

  always @(posedge clk)
  begin
    if (load)
      q <= data;
    else
    begin
      q[0] <= q[1];
      for (int i = 1; i < 511; i++)
        q[i] <= q[i-1] ^ q[i+1];
      q[511] <= q[510];
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
