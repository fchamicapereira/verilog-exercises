module top_module(
    input ring,
    input vibrate_mode,
    output ringer,       // Make sound
    output motor         // Vibrate
  );

  assign ringer = ~vibrate_mode & ring;
  assign motor = vibrate_mode & ring;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
