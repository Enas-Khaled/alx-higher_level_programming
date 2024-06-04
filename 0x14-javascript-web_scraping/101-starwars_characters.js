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

      // Function to fetch character names in order
      function fetchCharacterName(url, callback) {
        request(url, (error, response, body) => {
          if (error) {
            console.error('Error fetching character details:', error);
            callback(null);
            return;
          }

          if (response.statusCode === 200) {
            const character = JSON.parse(body);
            callback(character.name);
          } else {
            console.error('Failed to fetch character details:', response.statusCode);
            callback(null);
          }
        });
      }

      // Fetch all characters in order
      let completedRequests = 0;
      const characterNames = Array(characterUrls.length).fill(null);

      characterUrls.forEach((characterUrl, index) => {
        fetchCharacterName(characterUrl, (name) => {
          characterNames[index] = name;
          completedRequests++;

          // Print all character names once all requests are complete
          if (completedRequests === characterUrls.length) {
            characterNames.forEach((characterName) => {
              if (characterName) {
                console.log(characterName);
              }
            });
          }
        });
      });
    } else {
      console.error('Failed to fetch movie details:', response.statusCode);
    }
  });
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
} else {
  getMovieCharacters(movieId);
}

