/**
  * It gives a promise to fetch movies titles
  * @returns {Promise<str>} a promise containing the movies titles
  */
const fetchMovieTitles = () => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  const movieTitles = fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Parse the result and return the movie titles only
      return data.results.map((e) => e.title);
    })
    .catch((error) => {
      // Log the error
      console.log(error);
      // Throw it again because I dont care about it.
      throw error;
    });
  return movieTitles;
};
const createLi = (text) => {
  const li = document.createElement('li');
  if (text) {
    li.innerText = text;
  }
  return li;
};
// After fetching the movies titles display them in the movie titles list.
fetchMovieTitles()
  .then((movieTitles) => {
    const moviesList = document.querySelector('#list_movies');
    movieTitles.forEach((title) => {
      moviesList.appendChild(createLi(title));
    });
  });
