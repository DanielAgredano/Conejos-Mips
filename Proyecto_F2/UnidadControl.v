module CTRL_U(
	input [5:0]op,

    output reg RegDst,
    output reg Branch,
    output reg MemRead,
	output reg MemToReg,
    output reg [2:0]AluOp,
	output reg MemWrite,
	output reg AluSrc,
	output reg RegWrite
);

always @(*) begin
    case (op)
        5'b00000:begin
            RegDst      = 1'b1 ;
            Branch      = 1'b0 ;
            MemRead     = 1'bx ;
            MemToReg    = 1'b0 ;
            AluOp       = 3'b000 ;
            MemWrite    = 1'b0 ;
            AluSrc      = 1'b0 ;
            RegWrite    = 1'b1 ;
        end
    endcase
end
endmodule

