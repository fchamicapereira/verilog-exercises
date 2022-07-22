module top_module(
    input clk,
    input reset,   // Synchronous active-high reset
    output reg [3:1] ena,
    output reg [15:0] q
  );

  localparam [3:0] ROLLOVER = 4'd9;

  always @(posedge clk)
  begin
    if (reset)
    begin
      ena <= 3'b0;
      q <= 16'd0;
    end
    else
    begin
      ena[1] <= q[3:0] == (ROLLOVER-4'd1);
      ena[2] <= q[3:0] == (ROLLOVER-4'd1) && q[7:4] == ROLLOVER;
      ena[3] <= q[3:0] == (ROLLOVER-4'd1) && q[7:4] == ROLLOVER && q[11:8] == ROLLOVER;

      q[3:0] <= (q[3:0] == ROLLOVER) ? 4'd0 : q[3:0]  + 4'd1;

      if (ena[1])
        q[7:4] <= (q[7:4] == ROLLOVER) ? 4'd0 : q[7:4] + 4'd1;

      if (ena[2])
        q[11:8] <= (q[11:8] == ROLLOVER) ? 4'd0 : q[11:8] + 4'd1;

      if (ena[3])
        q[15:12] <= (q[15:12] == ROLLOVER) ? 4'd0 : q[15:12] + 4'd1;
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
