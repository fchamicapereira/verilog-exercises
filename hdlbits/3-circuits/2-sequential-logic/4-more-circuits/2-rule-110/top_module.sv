module top_module(
    input clk,
    input load,
    input [511:0] data,
    output reg [511:0] q
  );

  always @(posedge clk)
  begin
    if (load)
      q <= data;
    else
    begin
      for (int i = 0; i < 512; i++)
      begin
        case ({((i<511) ? q[i+1] : 1'b0),q[i],((i>0) ? q[i-1] : 1'b0)})
          3'b111:
            q[i] <= 1'b0;
          3'b110:
            q[i] <= 1'b1;
          3'b101:
            q[i] <= 1'b1;
          3'b100:
            q[i] <= 1'b0;
          3'b011:
            q[i] <= 1'b1;
          3'b010:
            q[i] <= 1'b1;
          3'b001:
            q[i] <= 1'b1;
          3'b000:
            q[i] <= 1'b0;
        endcase
      end
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
