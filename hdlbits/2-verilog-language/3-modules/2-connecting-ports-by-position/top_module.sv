module mod_a(
    output o1,
    output o2,
    input in1,
    input in2,
    input in3,
    input in4
  );

  assign o1 = in1 | in2;
  assign o2 = in3 & in4;

endmodule

module top_module(
    input a,
    input b,
    input c,
    input d,
    output o1,
    output o2
  );

  mod_a mod_a_instance(
          .in1(a),
          .in2(b),
          .in3(c),
          .in4(d),
          .o1(o1),
          .o2(o2)
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
