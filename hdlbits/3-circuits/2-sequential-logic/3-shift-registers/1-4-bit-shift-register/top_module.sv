module top_module(
    input clk,
    input areset,  // async active-high reset to zero
    input load,
    input ena,
    input [3:0] data,
    output reg [3:0] q
  );

  always @(posedge clk, posedge areset)
  begin
    if (areset)
    begin
      q <= 4'b0;
    end
    else if (load)
      q <= data;
    else if (ena)
    begin
      q <= { 1'b0, q[3], q[2], q[1] };
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
