module top_module(
    input [3:0] i,
    output reg [1:0] pos
  );
  always @(*)
  begin
    case (i)
      4'h0:
        pos = 2'd0; // 0
      4'h1:
        pos = 2'd0; // 1
      4'h2:
        pos = 2'd1; // 10
      4'h3:
        pos = 2'd0; // 11
      4'h4:
        pos = 2'd2; // 100
      4'h5:
        pos = 2'd0; // 101
      4'h6:
        pos = 2'd1; // 110
      4'h7:
        pos = 2'd0; // 111
      4'h8:
        pos = 2'd3; // 1000
      4'h9:
        pos = 2'd0; // 1001
      4'ha:
        pos = 2'd1; // 1010
      4'hb:
        pos = 2'd0; // 1011
      4'hc:
        pos = 2'd2; // 1100
      4'hd:
        pos = 2'd0; // 1101
      4'he:
        pos = 2'd1; // 1110
      4'hf:
        pos = 2'd0; // 1111
    endcase
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
