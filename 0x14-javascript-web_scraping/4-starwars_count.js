#!/usr/bin/node
const request = require('request');

const id = '18';
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)
    );
    console.log(moviesWithWedgeAntilles.length);
  }
});
