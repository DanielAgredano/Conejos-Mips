module PC(
    input [31:0] In,
    input CLK,

    output reg [31:0] Out
);

always @(posedge CLK) begin
    Out = In;
end

initial begin
    Out = 31'd0;
end

endmodule
