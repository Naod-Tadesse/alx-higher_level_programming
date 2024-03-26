#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  film.characters.forEach(characterUrl => {
    request.get(characterUrl, (cError, cResponse, cBody) => {
      if (cError) {
        console.error(cError);
      }
      const character = JSON.parse(cBody);
      console.log(character.name);
    });
  });
});
