'use strict' // 'use strict' ativa o modo estrito no JavaScript que ajuda a capturar possíveis erros.


const switcher = document.querySelector(".btn"); // A constante 'switcher' armazena a seleção do elemento cujo id é '.btn'

switcher.addEventListener("click", function(){ /* O elemento 'addEventListener' adiciona um evento(listener) de clique ao elemento da constante switcher*/
    document.body.classList.toggle("dark-theme") /* 'document.body' se refere ao elemento body do html. 'classList' é uma propriedade que contém uma lista de classes CSS aplicadas ao elemento. 'toggle()' é um método que alterna a presença de uma classe na lista. Essa linha altera a classe "dark-theme" no elemtno body. Se a classe ja estiver presente, ela será removida, senão, será adicionada. */


    var tema_atual = document.body.className; // 'document.body.className' é uma expressão que recupera o nome da classe atual do elemtno body. Essa linha armazena o nome da classe atual do elemento 'body' do html na variável className.
    if(tema_atual == "light-theme"){ // Condicional para verificar a classe atual do 'body' do html.
        this.textContent = "Escuro"; // Se a classe atual for 'light-theme', o texto do botão para alterar o tema será 'Escuro'.
    }
    else{ // Se a classe atual não for 'light-theme', o texto do botão será 'claro'.
        this.textContent = "Claro";
    }
})