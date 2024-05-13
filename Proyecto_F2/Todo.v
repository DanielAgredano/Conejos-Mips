module Todo(
	input [31:0]instruccionTR,
	output Tr_zf
);


reg [31:0]instruccion;
assign instruccion=instruccionTR;

wire [31:0]uno;
wire [31:0]dos;
wire [31:0]tres;
wire [3:0]cuatro;
wire [31:0]cinco;
wire [31:0]seis;
wire siete;
wire ocho;
wire nueve;
wire [2:0]diez;

Bancoreg ba( 
	.ra1(instruccion[25:21]),
	.ra2(instruccion[20:16]),
	.dir(instruccion[15:11]),
	.di(seis),
	
	.reg_write(siete),

	.dr1(dos),
	.dr2(uno)
);

ALU alu(
	.op1(dos),
	.op2(uno),

	.sel(cuatro),

	.zf(Tr_zf),
	.res(tres)
);

Memoria mem(
	.direccion(tres),
	.dato(uno),

	.sel(ocho),

	.salida(cinco)
);

Multiplexor mux(
	.a(tres),
	.b(cinco),

	.sel(nueve),

	.salida(seis)
);

AluControl aluc(
	.funct(instruccion[5:0]),
	
	.sel(diez),

	.AluOp(cuatro)
);

UnidadControl uc(
	.op(instruccion[31:26]),

	.MemToReg(nueve),
	.MemToWrite(ocho),
	.AluOp(diez),
	.RegWrite(siete)
);




endmodule