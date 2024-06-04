#!/usr/bin/node
const request = require('request');

// Function to get movie details by ID
function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error);
      return;
    }
    
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error fetching character details:', error);
            return;
          }
          
          if (response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          } else {
            console.error('Failed to fetch character details:', response.statusCode);
          }
        });
      });
    } else {
      console.error('Failed to fetch movie details:', response.statusCode);
    }
  });
}

// Replace with the desired movie ID
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
} else {
  getMovieCharacters(movieId);
}

