function GetPersonajes(done){

    const resultado = fetch("https://rickandmortyapi.com/api/character");

    resultado
        .then(Response => Response.json())
        .then(data => {
            done(data)
        });
}

GetPersonajes(data => {
    data.resultado.forEach(personaje => {

        const article = document.createRange().createContextualFragment(
        /*html*/
        `
        <article>   

            <div class="imagen_personaje">
                <img src="${personaje.image}" alt="Personaje">
            </div>

            <h2>${personaje.name}</h2>
            <span>${personaje.status}</span>

        </article>  
        `);

        const main = document.querySelector("main");

        main.append(article);         
    });
});