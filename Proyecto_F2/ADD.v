module ADD(
    input [31:0] In,
    
    output reg [31:0] Out
);

always @(*) begin
    Out = In + 4;
end 

endmodule
