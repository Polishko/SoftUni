import { useState } from "react";

const initialCats = [
  {
    id: 118836,
    name: "Gizmo",
    image: "https://cataas.com/cat?u=118836",
    happiness: 100,
  },

  {
    id: 245672,
    name: "Kaju",
    image: "https://cataas.com/cat?u=933372",
    happiness: 50,
  },

  {
    id: 499476,
    name: "Polen",
    image: "https://cataas.com/cat?u=499476",
    happiness: 30,
  },
];

function Button({ children, className, onClick }) {
  return (
    <button className={className} onClick={onClick}>
      {children}
    </button>
  );
}

export default function App() {
  const [cats, setCats] = useState(initialCats);
  const [showAddCat, setShowAddCat] = useState(false);

  function handleShowAddCat() {
    setShowAddCat((show) => !show);
  }

  function handleAddCat(cat) {
    setCats((cats) => [...cats, cat]);
  }

  return (
    <div className="app">
      <div className="container-1">
        <CatList cats={cats} />

        {showAddCat && <AddNewCat onAddCat={handleAddCat} />}

        <Button
          className={!showAddCat ? "button add pink" : "button add blue"}
          onClick={handleShowAddCat}
        >
          {!showAddCat ? "Add cat" : "Close"}
        </Button>
      </div>
    </div>
  );
}

function CatList({ cats }) {
  return (
    <ul className="cat-list">
      {cats.map((cat) => (
        <Cat cat={cat} key={cat.id} />
      ))}
    </ul>
  );
}

function Cat({ cat }) {
  return (
    <li className="cat">
      <div className="cat-img">
        <img src={cat.image} alt={cat.name} />
      </div>
      <div className="cat-info">
        <h3>{cat.name}</h3>
        <p>
          {cat.name}'s happiness level is {cat.happiness}
        </p>
      </div>
      <Button className="button feed green">Feed</Button>
      <Button className="button clean-litter blue">Clean litter</Button>
    </li>
  );
}

function AddNewCat({ onAddCat }) {
  const [name, setName] = useState("");
  const [image, setImage] = useState("https://cataas.com/cat");

  const id = crypto.randomUUID();

  const newCat = {
    id,
    name,
    image: `${image}?u=${id}`,
    happiness: 100,
  };

  function handleAddCat(e) {
    e.preventDefault();

    if (!name || !image) return;

    onAddCat(newCat);

    setName("");
    setImage("https://cataas.com/cat");
  }

  return (
    <form className="add-cat" onSubmit={handleAddCat}>
      <label>Cat name</label>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <label>Cat image</label>
      <input
        type="text"
        value={image}
        onChange={(e) => setImage(e.target.value)}
      />
      <Button className="button add pink">Add</Button>
    </form>
  );
}
