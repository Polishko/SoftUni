const initialCats = [
  {
    id: 118836,
    name: "Gizmo",
    image: "https://cataas.com/cat?u=118836",
    happiness: 100,
  },

  {
    id: 118836,
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

function Button({ children, className }) {
  return <button className={className}>{children}</button>;
}

export default function App() {
  const cats = initialCats;
  return (
    <div className="app">
      <CatList cats={cats} />
    </div>
  );
}

function CatList({ cats }) {
  return (
    <ul>
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
      <Button className="button feed">Feed</Button>
      <Button className="button clean-litter">Clean litter</Button>
    </li>
  );
}

function AddNewCat() {
  <form></form>;
}
