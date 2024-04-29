function Soma()
{
    var v1 = parseInt(document.getElementById("valor_1").value);
    var v2 = parseInt(document.getElementById("valor_2").value);
    var resultado = v1 + v2;

    document.getElementById("resposta").innerHTML = "Resposta da adição: " + resultado;
}

function Subtrair()
{
    var v1 = parseInt(document.getElementById("valor_1").value);
    var v2 = parseInt(document.getElementById("valor_2").value);
    var resultado = v1 - v2; 

    document.getElementById("resposta").innerHTML = "Resposta da subtração: " + resultado;
}

function Multiplicar()
{
    var v1 = parseInt(document.getElementById("valor_1").value);
    var v2 = parseInt(document.getElementById("valor_2").value);
    var resultado = v1 * v2; 

    document.getElementById("resposta").innerHTML = "Resposta da multiplicação: " + resultado;
}

function Dividir()
{
    var v1 = parseInt(document.getElementById("valor_1").value);
    var v2 = parseInt(document.getElementById("valor_2").value);
    var resultado = v1 / v2; 

    document.getElementById("resposta").innerHTML = "Resposta da divisão: " + resultado;
}