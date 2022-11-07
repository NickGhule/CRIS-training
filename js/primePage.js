// fetch movies from json file
function fetchMovies() {
    // load jason file and then parse
    fetch('data/movies.json')
        .then(response => response.json())
        .then(json => {
            // store data in global variable
            movies = json;
            // call function to display movies
            console.log(movies);
            displayMovies(movies);
        }
    );

}

// display movies
function displayMovies(movies) {
    const movieList = document.querySelector('div.movie-list');
    console.log("passed 20");
    movieList.innerHTML = '';
    movies.forEach(movie => {
        const movieItem = document.createElement('div');
        movieItem.classList.add('movie-item');
        movieItem.innerHTML = `
            <div class="movie-item__image">
                <img src="${movie.src}" alt="${movie.title}">
            </div>
            <div class="movie-item__content">
                <h3 class="movie-item__title">${movie.name}</h3>
                <div class="movie-item__description">
                    <p class="movie-item__year">${movie.year}</p>
                </div>
                <div class="movie-item__description">
                    <p class="movie-item__duration">${movie.duration}</p>
                </div>
                <button class="movie-item__button">Watch</button>
            </div>
        `;
        movieList.appendChild(movieItem);
    });
}
