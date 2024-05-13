module ALU(
    input [31:0] A,
    input [31:0] B,

    input [3:0] Sel,

    output reg ZF,
    output reg [31:0] Out
);

always @(*) begin
    case (Sel)
        4'b0000: Out = A & B;
        4'b0001: Out = A | B;
        4'b0010: Out = A + B;
        4'b0110: Out = A - B;
        4'b0111: Out = (A < B) ? 1 : 0;
        4'b1100: Out = ~(A | B);
        default: Out = 0;
    endcase
    ZF = (Out == 0) ? 1 : 0;
end

endmodule
