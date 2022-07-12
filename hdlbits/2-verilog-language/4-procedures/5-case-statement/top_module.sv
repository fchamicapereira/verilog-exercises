module top_module(
    input [2:0] sel,
    input [3:0] data0,
    input [3:0] data1,
    input [3:0] data2,
    input [3:0] data3,
    input [3:0] data4,
    input [3:0] data5,
    output reg [3:0] o
  );

  always@(*)
  begin
    case (sel)
      3'd0:
        o = data0;
      3'd1:
        o = data1;
      3'd2:
        o = data2;
      3'd3:
        o = data3;
      3'd4:
        o = data4;
      3'd5:
        o = data5;
      default:
        o = 4'd0;
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
