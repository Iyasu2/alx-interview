#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  try {
    const response = await request(endpoint);
    const filmData = JSON.parse(response.body);
    const characters = filmData.characters;

    for (let i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      try {
        const characterResponse = await request(urlCharacter);
        const character = JSON.parse(characterResponse.body);
        console.log(character.name);
      } catch (characterError) {
        console.error(`Error fetching character: ${characterError.message}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching film data: ${error.message}`);
  }
}

starwarsCharacters(filmID);
