module BAND(
    input A,
    input B,
    
    output reg Out
);

always @(*) begin
    Out = A & B;
end 

endmodule

