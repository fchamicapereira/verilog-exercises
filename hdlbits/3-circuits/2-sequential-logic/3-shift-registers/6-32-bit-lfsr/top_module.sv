module top_module(
    input clk,
    input reset,    // Active-high synchronous reset to 32'h1
    output reg [31:0] q
  );

  always @(posedge clk)
  begin
    if (reset)
      q <= 32'h1;
    else
    begin
      for (int i = 0; i < 32; i++)
      begin
        if (i == 31 || i == 21 || i == 1 || i == 0)
          q[i] <= ((i == 31) ? 1'b0 : q[i + 1]) ^ q[0];
        else
          q[i] <= (i == 31) ? 1'b0 : q[i + 1];
      end
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
