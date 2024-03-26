#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (!error) {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const moviesWithWedgeAntilles = films.filter(film =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(moviesWithWedgeAntilles);
    }
  } else {
    console.error(error);
  }
});
