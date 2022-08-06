module top_module(
    input clk,
    input areset,    // Asynchronous reset to state B
    input i,
    output o);//

  parameter A=0, B=1;
  reg state, next_state;

  always @(*)
  begin    // This is a combinational always block
    case (state)
      A:
        next_state = (i == 1'b1) ? A : B;
      B:
        next_state = (i == 1'b1) ? B : A;
    endcase
  end

  always @(posedge clk, posedge areset)
  begin    // This is a sequential always block
    if (areset)
      state <= B;
    else
      state <= next_state;
  end

  // Output logic
  assign o = (state == A) ? A : B;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
