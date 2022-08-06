module top_module(
    input clk,
    input reset,    // Asynchronous reset to state B
    input i,
    output reg o);//

  parameter A=0, B=1;
  reg present_state, next_state;

  always_comb
  begin
    case (present_state)
      A:
        next_state = (i == 1'b1) ? A : B;
      B:
        next_state = (i == 1'b1) ? B : A;
    endcase
  end

  always @(posedge clk)
  begin
    if (reset)
    begin
      present_state <= B;
    end
    else
    begin
      // State flip-flops
      present_state <= next_state;
    end
  end

  assign o = (present_state == A) ? 1'b0 : 1'b1;

`ifdef COCOTB_SIM

  initial
  begin
    $dumpfile ("top_module.vcd");
    $dumpvars (0, top_module);
    #1;
  end
`endif
endmodule
