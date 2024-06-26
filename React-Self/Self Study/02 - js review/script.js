const data = [
  {
    id: 1,
    title: "The Lord of the Rings",
    publicationDate: "1954-07-29",
    author: "J. R. R. Tolkien",
    genres: [
      "fantasy",
      "high-fantasy",
      "adventure",
      "fiction",
      "novels",
      "literature",
    ],
    hasMovieAdaptation: true,
    pages: 1216,
    translations: {
      spanish: "El señor de los anillos",
      chinese: "魔戒",
      french: "Le Seigneur des anneaux",
    },
    reviews: {
      goodreads: {
        rating: 4.52,
        ratingsCount: 630994,
        reviewsCount: 13417,
      },
      librarything: {
        rating: 4.53,
        ratingsCount: 47166,
        reviewsCount: 452,
      },
    },
  },
  {
    id: 2,
    title: "The Cyberiad",
    publicationDate: "1965-01-01",
    author: "Stanislaw Lem",
    genres: [
      "science fiction",
      "humor",
      "speculative fiction",
      "short stories",
      "fantasy",
    ],
    hasMovieAdaptation: false,
    pages: 295,
    translations: {},
    reviews: {
      goodreads: {
        rating: 4.16,
        ratingsCount: 11663,
        reviewsCount: 812,
      },
      librarything: {
        rating: 4.13,
        ratingsCount: 2434,
        reviewsCount: 0,
      },
    },
  },
  {
    id: 3,
    title: "Dune",
    publicationDate: "1965-01-01",
    author: "Frank Herbert",
    genres: ["science fiction", "novel", "adventure"],
    hasMovieAdaptation: true,
    pages: 658,
    translations: {
      spanish: "",
    },
    reviews: {
      goodreads: {
        rating: 4.25,
        ratingsCount: 1142893,
        reviewsCount: 49701,
      },
    },
  },
  {
    id: 4,
    title: "Harry Potter and the Philosopher's Stone",
    publicationDate: "1997-06-26",
    author: "J. K. Rowling",
    genres: ["fantasy", "adventure"],
    hasMovieAdaptation: true,
    pages: 223,
    translations: {
      spanish: "Harry Potter y la piedra filosofal",
      korean: "해리 포터와 마법사의 돌",
      bengali: "হ্যারি পটার এন্ড দ্য ফিলোসফার্স স্টোন",
      portuguese: "Harry Potter e a Pedra Filosofal",
    },
    reviews: {
      goodreads: {
        rating: 4.47,
        ratingsCount: 8910059,
        reviewsCount: 140625,
      },
      librarything: {
        rating: 4.29,
        ratingsCount: 120941,
        reviewsCount: 1960,
      },
    },
  },
  {
    id: 5,
    title: "A Game of Thrones",
    publicationDate: "1996-08-01",
    author: "George R. R. Martin",
    genres: ["fantasy", "high-fantasy", "novel", "fantasy fiction"],
    hasMovieAdaptation: true,
    pages: 835,
    translations: {
      korean: "왕좌의 게임",
      polish: "Gra o tron",
      portuguese: "A Guerra dos Tronos",
      spanish: "Juego de tronos",
    },
    reviews: {
      goodreads: {
        rating: 4.44,
        ratingsCount: 2295233,
        reviewsCount: 59058,
      },
      librarything: {
        rating: 4.36,
        ratingsCount: 38358,
        reviewsCount: 1095,
      },
    },
  },
];

function getBooks() {
  return data;
}

function getBook(id) {
  return data.find((d) => d.id === id);
}

const book = getBook(2);
// const title = book.title;
// title;

// Destructuring, rest, spread opearators
const { title, author, pages, publicationDate, genres, hasMovieAdaptation } =
  book;
book;
const [primaryGenres, secondaryGenres, ...otherGenres] = genres; // deconstructor with rest operator
primaryGenres;
secondaryGenres;
otherGenres;

const newGenres = [...genres, "epic fantacy"];
newGenres;

const book1 = getBook(1);
const updatedBook = {
  ...book,
  moveiPublicationDate: "2001-12-19",
  pages: 1210,
};
updatedBook;

// Template literal
const summary = `${title} was written by ${author} in ${
  publicationDate.split("-")[0]
}.`;
summary;

// ternary operator
const pagesRange = pages > 1000 ? "over a thousand" : "less than a thousand";
pagesRange;

// Arrow functions
// function getYear(str) {
//   return str.split("-")[0];
// }  // function declaration

// const getYear(str) {
//   return str.split("-")[0];
// };

const getYear = (str) => str.split("-")[0]; // function expression, no function block no return
console.log(getYear(publicationDate));

// Short circuiting and logical operators
console.log(true && "some value"); // short circuits to second value
console.log(false && "some value"); // doesnt check the second value, returns false

// falsy values: 0, '', null, undefined
console.log("nalan" && "some string"); // some string

console.log(true || "some value"); // short circuits to true
console.log(false || "some value"); // returns the second value

// we can use this to set default values
console.log(book.translations.spanish);
const spanishTranslation = book.translations.spanish || "NOT TRANSLATED";
spanishTranslation;
// Be careful though, 0 is not a no value! but since its falsy it can shortcircuit to a wrong result
// Use Nullish coalescing operator (??) instead
const count = book.reviews.librarything.reviewsCount ?? "no reviews";
count;

// Optional chaining
function getTotalReviewCount(book) {
  const goodReads = book.reviews?.goodreads?.reviewsCount ?? 0; // ? skips undefined values ?? returns 0 if undefined/non existent
  const librarything = book.reviews?.librarything?.reviewsCount ?? 0;
  return goodReads + librarything;
}

console.log(getTotalReviewCount(book));

// Functional array methods (don't mutate te array): map, filter, reduce
const myBooks = getBooks();
// Using map -> expects a callback fnct that will be used on each element of collection the map is applied
const titles = myBooks.map((book) => book.title);
titles;

const essentialData = myBooks.map((book) => ({
  title: book.title,
  author: book.author,
  reviewsCount: getTotalReviewCount(book),
}));
essentialData;

const longBooks = myBooks
  .filter((book) => book.pages > 500)
  .filter((book) => book.hasMovieAdaptation);
longBooks;

const adventureBooks = myBooks
  .filter((book) => book.genres.includes("adventure"))
  .map((book) => book.title);
adventureBooks;

// reduce method: takes 2 args: a callback to execute on each element and a starter value => purpose: boil entire array to one value
const pagesAllBooks = myBooks.reduce((acc, book) => acc + book.pages, 0); //acc: current val of final val we want to boil down the array to
pagesAllBooks;

// Sort method
const arr = [1, 2, 3, 4, 5];
// const sortedAsc = arr.sort((a, b) => a - b); // ascending
const sortedDesc = arr.sort((a, b) => b - a); // descending
arr; //also sorted and thus mutaed
sortedDesc;

const arr2 = [1, 2, 3, 4, 5];
const sortedDesc2 = arr2.slice().sort((a, b) => b - a);
arr2;
sortedDesc2;

const sortedByPages = myBooks
  .slice()
  .sort((a, b) => a.pages - b.pages)
  .map((book) => ({
    title: book.title,
    pages: book.pages,
  }));
sortedByPages;

// Immutable arrays
// 1. Add a book obj
const newBook = {
  id: 6,
  title: "Some Title",
  author: "Some Author",
};
const booksAfterAdd = [...myBooks, newBook];
booksAfterAdd;

// 2. Delete a book obj
const booksAfterDelete = booksAfterAdd.filter((book) => book.id != 3);
booksAfterDelete;

// 3. Update a book obj
const booksAfterUpdate = booksAfterDelete.map((book) =>
  book.id === 1 ? { ...book, pages: 1210 } : book
);
booksAfterUpdate;

// Async JS: Promises
// google JSON placeholder
//Promise: pending, rejected, fulfilled
fetch("https://jsonplaceholder.typicode.com/todos") // this will take time, it returns a promise, we may want to wait for its completion
  .then((res) => res.json()) //called after initial promise is fulfilled and returns another promise, also takes time
  .then((data) => console.log(data));

console.log("Hi");
// gets printed out before the fetch is executed because JS doesnt wait the fetch

// Async Await: we can await the fetch that takes time and store its result
async function getToDos() {
  const res = await fetch("https://jsonplaceholder.typicode.com/todos");
  const data = await res.json();
  console.log(data);
  return data;
}

const toDos = getToDos();
console.log(toDos); // this is logged as pending
console.log("something"); //Again will get printed then
