module ALU_CTRL(
	input [5:0]Funct,
	input [2:0]Sel,

	output reg [3:0]Out
);

always @(*) begin
    if(Sel==3'b000)begin
        case (Funct)
            6'b100000:
                Out = 4'b0010;
            6'b100010:
                Out = 4'b0110;
            6'b100100:
                Out = 4'b0000;
            6'b100101:
                Out = 4'b0001;
            6'b100111:
                Out = 4'b1100;
            6'b101010:
                Out = 4'b0111;
        endcase
    end
end

endmodule


