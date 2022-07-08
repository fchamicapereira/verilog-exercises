// This file is public domain, it can be freely copied without restrictions.
// SPDX-License-Identifier: CC0-1.0

module my_design(
  input logic clk,
  input  rst,
  input  button_in,
  output button_valid
);
  timeunit 1s;
  timeprecision 1ns;

  logic my_signal_1;
  logic my_signal_2;

  assign my_signal_1 = 1'bx;
  assign my_signal_2 = 0;

  // the "macro" to dump signals
  `ifdef COCOTB_SIM
  initial begin
    $dumpfile ("my_design.vcd");
    $dumpvars (0, my_design);
    #1;
  end
  `endif

endmodule
