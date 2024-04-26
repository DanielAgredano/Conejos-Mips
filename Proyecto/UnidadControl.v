module UnidadControl(
	input [5:0]op,

	output reg MemToReg,
	output reg MemToWrite,
	output reg [2:0]AluOp,
	output reg RegWrite
);

always @(*)
begin
    case (op)
        5'b00000:begin
        MemToReg    =1'b0 ;
        MemToWrite  =1'b0 ;
        AluOp       =3'b000 ;
        RegWrite    =1'b1 ;
        end
    endcase
end

endmodule

