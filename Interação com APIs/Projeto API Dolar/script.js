
const url = "https://economia.awesomeapi.com.br/json/last/USD-BRL";
window.alert("Para o uso correto deste projeto, não aperte a tecla Enter depois de ter inserido a quantidade de Reais. Se você não fizer isso, a página será recarregada e você perderá os dados inseridos. Vale lembrar também que para atualizar a data e o horário do câmbio, aperte o botão converter duas vezes. Este projeto foi feito inteiramente por Arthur Germano, aluno do 3ºE :)")



function converterRealDolar(){ // Declaração da função

    const valor_real = document.getElementById("valor_real").value; //Criação da constante valor_real e armazenamento dos dados

    fetch(url) //A função fetch() serve para fazer a requisisção dos dados por meio do url declarado.
    .then(response => response.json()) // Afunção .then serve para tratar os dados recebidos pela API. Nesta linha, a função .then serve para converter a resposta em notação json.
    .then(data => {  // Aqui a função .then serve está acessando dos dados do objeto JSON advindo da API.
        const horario = data["USDBRL"]["create_date"];
        const cotaçao_dolar = data["USDBRL"]["bid"];
        const valor_dolar = valor_real / cotaçao_dolar;
        const resultado = `R$ ${valor_real} equivale a US$ ${valor_dolar.toFixed(2)} doláres no dia ${horario}.`;
        document.getElementById("valor_cambio").innerHTML = resultado;
        
    })
}

