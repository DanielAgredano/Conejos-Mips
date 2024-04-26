module AluControl(
	input [5:0]funct,
	input [2:0]sel,

	output reg [3:0]AluOp
);

always @(*)
begin
    if(sel==3'b000)begin
        case (funct)
            6'b100000:
                AluOp = 4'b0010;
            6'b100010:
                AluOp = 4'b0110;
            6'b100100:
                AluOp = 4'b0000;
            6'b100101:
                AluOp = 4'b0001;
            6'b100111:
                AluOp = 4'b1100;
            6'b101010:
                AluOp = 4'b0111;
        endcase
    end
end

endmodule


