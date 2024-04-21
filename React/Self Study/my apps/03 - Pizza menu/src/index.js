import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

// Data taken from data.js (deleted)-> later will be done using modules
const pizzaData = [
  {
    name: "Focaccia",
    ingredients: "Bread with italian olive oil and rosemary",
    price: 6,
    photoName: "pizzas/focaccia.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Margherita",
    ingredients: "Tomato and mozarella",
    price: 10,
    photoName: "pizzas/margherita.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Spinaci",
    ingredients: "Tomato, mozarella, spinach, and ricotta cheese",
    price: 12,
    photoName: "pizzas/spinaci.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Funghi",
    ingredients: "Tomato, mozarella, mushrooms, and onion",
    price: 12,
    photoName: "pizzas/funghi.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Salamino",
    ingredients: "Tomato, mozarella, and pepperoni",
    price: 15,
    photoName: "pizzas/salamino.jpg",
    soldOut: true,
  },
  {
    name: "Pizza Prosciutto",
    ingredients: "Tomato, mozarella, ham, aragula, and burrata cheese",
    price: 18,
    photoName: "pizzas/prosciutto.jpg",
    soldOut: false,
  },
];

// components
function App() {
  return (
    <div className="container">
      <Header />
      <Menu />
      <Footer />
    </div>
  );
}

function Header() {
  //   const style = { color: "red", fontSize: "48", textTransform: "uppercase" }; // inline example
  const style = {};

  return (
    <header className="header">
      <h1 style={style}>Fast React Pizza Co.</h1>
    </header>
  );
}

function Menu() {
  return (
    <main className="menu">
      <h2>Our menu</h2>
      <ul className="pizzas">
        {pizzaData.map((pizza) => (
          <Pizza pizzaObj={pizza} key={pizza.name} />
        ))}
        {/*so JS in { then in there we have markup for Pizza and in it another JS in {}} */}
      </ul>
      {/* <Pizza
        name="Pizza Spinaci"
        ingredients="Tomato, mozarella, spinach, and ricotta cheese"
        photoName="pizzas/spinaci.jpg"
        price={10} // to write them as num not str
      />
      <Pizza
        name="Pizza Funghi"
        ingredients="Tomato, mushrooms"
        price={12}
        photoName="pizzas/funghi.jpg"
      /> */}
    </main>
  );
}

function Pizza(props) {
  return (
    <li className="pizza">
      {" "}
      {/*Each pizza is li element of ul in menu */}
      <img src={props.pizzaObj.photoName} alt={props.pizzaObj.name}></img>
      <div>
        <h3>{props.pizzaObj.name}</h3>
        <p>{props.pizzaObj.ingredients}</p>
        <span>{props.pizzaObj.price + 3}</span>
      </div>
    </li>
  );
}

function Footer() {
  const hour = new Date().getHours();
  const openHour = 12;
  const closedHour = 22;
  const isOpen = hour >= openHour && hour <= closedHour;
  console.log(isOpen);

  //   if (hour >= openHour && hour <= closedHour) alert("We're currently open");
  //   else alert("Sorry, we're closed."); {} oprtional for single statement if

  return (
    <footer>{new Date().toLocaleDateString()}. We're currently open!</footer>
  );
  //   return React.createElement("footer", null, "We're currently open!"); //Demonstration no JSX null is props
}

// App component rendered as a root component
// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(<App />);

// renering using strict mode wrap: checks issues, errors
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
