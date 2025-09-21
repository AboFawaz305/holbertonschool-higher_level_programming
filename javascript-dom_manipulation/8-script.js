/**
  * It gives a promise to fetch the value of hello
  * @returns {Promise<str>} a promise containing the value of hello
  */
const fetchHello = () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const hello = fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // Parse the result and return the hello
      return data.hello;
    })
    .catch((error) => {
      // Log the error
      console.log(error);
      // Throw it again because I dont care about it.
      throw error;
    });
  return hello;
};
// After fetching the whole page loads fetch the hello and display it.
document.addEventListener('DOMContentLoaded', () => {
  fetchHello()
    .then((hello) => {
      const helloBox = document.querySelector('#hello');
      helloBox.innerText = hello;
    });
});
