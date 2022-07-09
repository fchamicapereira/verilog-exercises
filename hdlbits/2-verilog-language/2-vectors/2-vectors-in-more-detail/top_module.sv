`default_nettype none     // Disable implicit nets. Reduces some types of bugs.
module top_module(
    input wire [15:0] i,
    output wire [7:0] o_hi,
    output wire [7:0] o_lo
  );

  assign { o_hi, o_lo } = i;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
