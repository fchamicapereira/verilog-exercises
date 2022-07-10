module mod_a(
    input in1,
    input in2,
    output o
  );

  assign o = in1 | in2;

endmodule

module top_module(
    input a,
    input b,
    output o
  );

  mod_a inst1 (
          .in1(a), 	// Port"in1"connects to wire "a"
          .in2(b),	// Port "in2" connects to wire "b"
          .o(o)	// Port "out" connects to wire "out"
          // (Note: mod_a's port "out" is not related to top_module's wire "out".
          // It is simply coincidence that they have the same name)
        );

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
