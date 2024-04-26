module ALU(
    input [31:0] op1,
    input [31:0] op2,
    input [3:0] sel,
    output reg [31:0] res,
    output reg zf
);

always @(*) begin
    case (sel)
        4'b0000: res = op1 & op2;
        4'b0001: res = op1 | op2;
        4'b0010: res = op1 + op2;
        4'b0110: res = op1 - op2;
        4'b0111: res = (op1 < op2) ? 1 : 0;
        4'b1100: res = ~(op1 | op2);
        default: res = 0;
    endcase
    zf = (res == 0) ? 1 : 0;
end

endmodule
