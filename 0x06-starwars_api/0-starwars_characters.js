#!/usr/bin/node
const rp = require('request-promise');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the URL for the API request
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make the API request
rp({ uri: url, json: true })
  .then(film => {
    const characterUrls = film.characters;
    const characterPromises = characterUrls.map(url => rp({ uri: url, json: true }));
    return Promise.all(characterPromises);
  })
  .then(characters => {
    characters.forEach(character => console.log(character.name));
  })
  .catch(error => console.error(`Error: ${error}`));
