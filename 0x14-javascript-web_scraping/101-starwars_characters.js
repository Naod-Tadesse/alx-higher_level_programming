#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const printCharacters = (index) => {
    if (index === characters.length) {
      return;
    }

    const characterUrl = characters[index];
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Failed to fetch character data: ${charResponse.statusCode}`);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
      printCharacters(index + 1);
    });
  };

  printCharacters(0);
});
