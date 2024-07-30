#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    const characterNames = [];

    const getCharacterName = (url, index) => {
      request(url, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          characterNames[index] = JSON.parse(body).name;
          if (characterNames.length === characters.length && !characterNames.includes(undefined)) {
            characterNames.forEach(name => {
              console.log(name);
            });
          }
        }
      });
    };

    characters.forEach((characterUrl, index) => {
      getCharacterName(characterUrl, index);
    });
  }
});
