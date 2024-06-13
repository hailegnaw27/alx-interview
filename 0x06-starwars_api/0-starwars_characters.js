#!/usr/bin/node

const request = require('request')

const movieId = process.argv[2]
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId
let characters = []
const characterNames = []

/**
* Fetches the list of character URLs from the film endpoint.
*/
const fetchCharacterUrls = async () = > {
    await new Promise(resolve= > {
        request(filmEndPoint, (err, res, body)=> {
            if (err | | res.statusCode !== 200) {
                console.error('Error:', err, '| StatusCode:', res.statusCode)
                resolve()
                return
            }
            const filmData=JSON.parse(body)
            characters=filmData.characters
            resolve()
        })
    })
}

/**
* Fetches the names of characters from the character URLs.
*/
const fetchCharacterNames = async () = > {
    if (characters.length > 0) {
        for (const characterUrl of characters) {
            await new Promise(resolve=> {
                request(characterUrl, (err, res, body)= > {
                    if (err | | res.statusCode != = 200) {
                        console.error(
                            'Error:', err, '| StatusCode:', res.statusCode)
                        resolve()
                        return
                    }
                    const characterData=JSON.parse(body)
                    characterNames.push(characterData.name)
                    resolve()
                })
            })
        }
    } else {
        console.error('Error: No characters found for this movie.')
    }
};

/**
* Main function to get character names and print them.
*/
const displayCharacterNames = async () = > {
    await fetchCharacterUrls()
    await fetchCharacterNames()

    characterNames.forEach((name, index)= > {
        if (index == = characterNames.length - 1) {
            process.stdout.write(name)
        } else {
            process.stdout.write(name + '\n')
        }
    })
}

displayCharacterNames()
