#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the URL for the API request
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make the API request
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characterUrls = film.characters;
    characterUrls.forEach((url) => {
      request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
