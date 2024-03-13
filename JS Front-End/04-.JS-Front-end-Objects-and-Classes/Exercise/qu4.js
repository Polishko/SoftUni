

function addMovies(processesArray) {
    class Movie {     // can be solved without using class for the object 
        constructor(name, director, date) {
            this.name = name;
            this.director = director;
            this.date = date;
        }
    }

    let movies = [];
    for (let process of processesArray) {
        if (process.includes('addMovie')) {
            let movieName = process.replace('addMovie ', '').trim();
            let movie = new Movie(movieName, '', '');
            movies.push(movie);            
        } else if (process.includes('directedBy')) {
            let [movieName, movieDirector] = process.split(' directedBy ');
            const movie = movies.find((movie) => movie.name === movieName);

            if (movie) {
                movie.director = movieDirector;
            }            
        } else {
            let [movieName, movieDate] = process.split(' onDate ');

            const movie = movies.find((movie) => movie.name === movieName);

            if (movie) {
                movie.date = movieDate;
            }

        }
    }
    
    for (let movie of movies) {
        if (movie.name && movie.director && movie.date) {  // can use filter 
            console.log(JSON.stringify(movie));
        }
    }
}


// addMovies([
//     'addMovie Fast and Furious',
//     'addMovie Godfather',
//     'Inception directedBy Christopher Nolan',
//     'Godfather directedBy Francis Ford Coppola',
//     'Godfather onDate 29.07.2018',
//     'Fast and Furious onDate 30.07.2018',
//     'Batman onDate 01.08.2018',
//     'Fast and Furious directedBy Rob Cohen'
//     ]
//     );

addMovies([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ]
    );
