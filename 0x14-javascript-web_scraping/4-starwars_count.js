#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles character ID

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  const moviesWithWedgeAntilles = films.filter(film =>
    film.characters.includes(`people/${characterId}`)
  );

  console.log(moviesWithWedgeAntilles.length);
});
