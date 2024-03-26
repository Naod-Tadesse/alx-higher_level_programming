#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const getCharacter = (characterUrl) => {
    request.get(characterUrl, (cError, cResponse, cBody) => {
      if (cError) {
        console.error(cError);
      }

      const cha = JSON.parse(cBody);
      console.log(cha.name);
    });
  };

  characters.forEach(getCharacter);
});
