`timescale 1ns/1ns
module Todo_F2();

reg CLK;
//Formato de cables: W_<Modulo de origen>_<Salida especifica>
//Si el modulo solo tiene una salida no se especifica la salida
wire [31:0] W_PC1;

wire [31:0] W_ADD1;

wire 		W_AND1;

wire [31:0]	W_INS1;

wire [31:0]	W_BR1_O1;
wire [31:0]	W_BR1_O2;

wire [31:0]	W_ALU1;
wire 		W_ALU1_ZF;

wire [31:0]	W_MEM1;

wire [3:0]	W_ALUC1;

wire 		W_UC1_RD;
wire 		W_UC1_Br;
wire 		W_UC1_MR;
wire 		W_UC1_MtR;
wire [2:0]	W_UC1_AOp;
wire 		W_UC1_MW;
wire 		W_UC1_ASr;
wire 		W_UC1_RW;

wire [31:0]	W_MUX1;
wire [31:0]	W_MUX2;
wire [31:0]	W_MUX3;
wire [4:0] 	W_MUX4;

PC PC1(
	.In(W_MUX2),
	.CLK(CLK),

	.Out(W_PC1)
);

ADD ADD1(
	.In(W_PC1),

	.Out(W_ADD1)
);

BAND AND1(
	.A(W_UC1_Br),
	.B(W_ALU1_ZF),

	.Out(W_AND1)
);

INS_MEM INS1(
    .Dir(W_PC1),

    .Out(W_INS1)
);

REG_BANK BR1( 
	.RDir1(W_INS1[25:21]),
	.RDir2(W_INS1[20:16]),
	.WDir(W_MUX4),
	.WData(W_MUX1),
	
	.RW(W_UC1_RW),

	.ROut1(W_BR1_O1),
	.ROut2(W_BR1_O2)
);

ALU ALU1(
	.A(W_BR1_O1),
	.B(W_MUX3),

	.Sel(W_ALUC1),

	.ZF(W_ALU1_ZF),
	.Out(W_ALU1)
);

RMEM MEM1(
	.WData(W_BR1_O2),
	.WDir(W_ALU1),

	.Sel(W_UC1_MW),

	.Out(W_MEM1)
);

ALU_CTRL ALUC1(
	.Funct(W_INS1[5:0]),
	
	.Sel(W_UC1_AOp),

	.Out(W_ALUC1)
);

CTRL_U UC1(
	.op(W_INS1[31:26]),

	.RegDst(W_UC1_RD),
	.Branch(W_UC1_Br),
	.MemRead(W_UC1_MR),
	.MemToReg(W_UC1_MtR),
	.AluOp(W_UC1_AOp),
	.MemWrite(W_UC1_MW),
	.AluSrc(W_UC1_ASr),
	.RegWrite(W_UC1_RW)
);

MUX MUX1(
	.B(W_MEM1),
	.A(W_ALU1),

	.Sel(W_UC1_MtR),

	.Out(W_MUX1)
);

MUX MUX2(
    .A(W_ADD1),
    .B(),//Vacío

    .Sel(W_AND1),

    .Out(W_MUX2)
);

MUX MUX3(
	.A(W_BR1_O2),
	.B(),//vacio

	.Sel(W_UC1_ASr),

	.Out(W_MUX3)
);

MUX_5 MUX4(
    .A(W_INS1[20:16]),
    .B(W_INS1[15:11]),

    .Sel(W_UC1_RD),

    .Out(W_MUX4)
);


initial
begin
	CLK 	= 1'b0;
	forever #100 CLK = ~CLK;
end
endmodule
