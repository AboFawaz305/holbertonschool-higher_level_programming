/**
  * It gives a promise to fetch the name.
  * @returns {Promise<str>} a promise containing the value of the name.
  */
const fetchName = () => {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  const name = fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      return data.name;
    })
    .catch((error) => {
      // Log the error
      console.log(error);
      // Throw it again because I dont care about it.
      throw error;
    });
  return name;
};
// After fetching the name display it on the screen.
fetchName()
  .then((name) => {
    const character = document.querySelector('#character');
    character.innerText = name;
    return name;
  });
