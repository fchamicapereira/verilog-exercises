module bcd_counter_2d(
    input clk,
    input reset,   // Synchronous active-high reset
    input ena,
    input [7:0] reset_value,
    input [7:0] min,
    input [7:0] max,
    output rollover,
    output reg [7:0] q
  );
  localparam [3:0] ROLLOVER = 4'h9;

  assign rollover = (q == max);

  always @(posedge clk)
  begin
    if (reset)
      q <= reset_value;
    else if (ena)
    begin
      if (rollover)
        q <= min;
      else
      begin
        q[3:0] <= (q[3:0] == ROLLOVER) ? 4'h0 : q[3:0]  + 4'h1;

        if (q[3:0] == ROLLOVER)
          q[7:4] <= (q[7:4] == ROLLOVER) ? 4'h0 : q[7:4] + 4'h1;
      end
    end
  end
endmodule

module top_module(
    input clk,
    input reset,
    input ena,
    output reg pm,
    output reg [7:0] hh,
    output reg [7:0] mm,
    output reg [7:0] ss
  );

  wire rollover_hh;
  wire rollover_mm;
  wire rollover_ss;

  bcd_counter_2d bcd_counter_2d_hh(clk, reset, ena && rollover_ss && rollover_mm, 8'h12, 8'h01, 8'h12, rollover_hh, hh);
  bcd_counter_2d bcd_counter_2d_mm(clk, reset, ena && rollover_ss, 8'h00, 8'h00, 8'h59, rollover_mm, mm);
  bcd_counter_2d bcd_counter_2d_ss(clk, reset, ena, 8'h00, 8'h00, 8'h59, rollover_ss, ss);

  always @(posedge clk)
  begin
    if (reset)
      pm <= 1'b0;
    else if (hh == 8'h11 && mm == 8'h59 && ss == 8'h59)
      pm <= ~pm;
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
