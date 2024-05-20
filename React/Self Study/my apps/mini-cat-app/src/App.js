import { useState, useEffect } from "react";

const initialCats = [
  {
    id: 118836,
    name: "Gizmo",
    image: "https://cataas.com/cat?u=118836",
    hunger: 0,
    litterDirtyness: 0,
  },

  {
    id: 245672,
    name: "Kaju",
    image: "https://cataas.com/cat?u=933372",
    hunger: 0,
    litterDirtyness: 0,
  },

  {
    id: 499476,
    name: "Polen",
    image: "https://cataas.com/cat?u=499476",
    hunger: 0,
    litterDirtyness: 0,
  },
];

export default function App() {
  const [cats, setCats] = useState(initialCats);
  const [showAddCat, setShowAddCat] = useState(false);
  const [selectedCat, setSelectedCat] = useState(null);
  const [adopted, setAdopted] = useState(0);

  function handleShowAddCat() {
    setShowAddCat((show) => !show);
  }

  function handleAddCat(cat) {
    setCats((cats) => [...cats, cat]);
  }

  useEffect(() => {
    const hungerTimer = setInterval(() => {
      setCats((prevCats) =>
        prevCats.map((cat) => {
          const newHunger = cat.hunger + 1.5;
          if (newHunger >= 100) {
            return { ...cat, hunger: 100 };
          } else {
            return { ...cat, hunger: newHunger };
          }
        })
      );
    }, 10000);

    return () => clearInterval(hungerTimer);
  }, []);

  useEffect(() => {
    const dirdinessTimer = setInterval(() => {
      setCats((prevCats) =>
        prevCats.map((cat) => {
          const newDirdiness = cat.litterDirtyness + 0.5;
          if (newDirdiness >= 100) {
            return { ...cat, litterDirtyness: 100 };
          } else {
            return { ...cat, litterDirtyness: newDirdiness };
          }
        })
      );
    }, 30000);

    return () => clearInterval(dirdinessTimer);
  }, []);

  useEffect(
    function () {
      if (cats?.length === 0) setAdopted(0);
    },
    [cats]
  );

  function handleFeed(currCat) {
    setCats((prevCats) =>
      prevCats.map((cat) =>
        cat.id === currCat.id ? { ...cat, hunger: 0 } : cat
      )
    );
  }

  function handleCleanLitter(currCat) {
    setCats((prevCats) =>
      prevCats.map((cat) =>
        cat.id === currCat.id ? { ...cat, litterDirtyness: 0 } : cat
      )
    );
  }

  function handleSelection(cat) {
    setSelectedCat(cat);
  }

  function handleCloseSelected() {
    setSelectedCat(null);
  }

  function handleAdoptCat() {
    setAdopted((curr) => curr + 1);
    setCats((cats) => cats.filter((cat) => cat.id !== selectedCat.id));
    setSelectedCat(null);
  }

  return (
    <div className="app">
      <div className="shelter-cats">
        <CatList
          cats={cats}
          onFeed={handleFeed}
          onLitterClean={handleCleanLitter}
          onSelection={handleSelection}
          showAddCat={showAddCat}
          selectedCat={selectedCat}
        />

        {!selectedCat && (
          <ToggleAddCloseButton
            showAddCat={showAddCat}
            handleShowAddCat={handleShowAddCat}
          />
        )}

        {showAddCat && <AddNewCat onAddCat={handleAddCat} />}

        <ShelterStats cats={cats} adopted={adopted} setAdopted={setAdopted} />
      </div>

      {selectedCat && (
        <ManageCat
          selectedCat={selectedCat}
          onFeed={handleFeed}
          onLitterClean={handleCleanLitter}
          onCloseSelected={handleCloseSelected}
          onAdoptCat={handleAdoptCat}
        />
      )}
    </div>
  );
}

function CatList({ cats, onSelection, showAddCat, selectedCat }) {
  return (
    <ul className="cat-list">
      {cats.map((cat) => (
        <Cat
          cat={cat}
          key={cat.id}
          onSelection={onSelection}
          showAddCat={showAddCat}
          selectedCat={selectedCat}
        />
      ))}
    </ul>
  );
}

function Cat({ cat, onSelection, showAddCat, selectedCat }) {
  return (
    <li className={selectedCat?.id === cat.id ? "cat selected" : "cat"}>
      <div className="cat-img">
        <img src={cat.image} alt={cat.name} />
      </div>
      <div className="cat-info">
        <h3>{cat.name}</h3>
        <div>
          <p>
            {cat.name}'s hunger level is {Math.abs(cat.hunger)}%
          </p>
          <p>
            {cat.name}'s litter dirtiness level is{" "}
            {Math.abs(cat.litterDirtyness)}%
          </p>

          {cat.hunger === 100 && cat.litterDirtyness === 100 && (
            <p>{cat.name} is unhappy 😿! Feed cat and change litter!</p>
          )}

          {cat.hunger === 100 && cat.litterDirtyness < 100 && (
            <p>{cat.name} is unhappy 😿! Feed cat!</p>
          )}

          {cat.hunger < 100 && cat.litterDirtyness === 100 && (
            <p>{cat.name} is uhappy 😿! Change litter!</p>
          )}

          {cat.hunger < 100 && cat.litterDirtyness < 100 && (
            <p>{cat.name} is happy 😻!</p>
          )}
        </div>
      </div>

      <AddCatButton
        showAddCat={showAddCat}
        cat={cat}
        onSelection={onSelection}
      />
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
    hunger: 100,
    litterDirtyness: 0,
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
      <Button className="button add-close pink">Add</Button>
    </form>
  );
}

function ManageCat({
  selectedCat,
  onFeed,
  onLitterClean,
  onCloseSelected,
  onAdoptCat,
}) {
  return (
    <div className="manage-cat">
      <h3>{selectedCat?.name}</h3>

      <div className="manage-1">
        {/* Component composition example for the FeedButton but too much abstraction */}
        {/* <FeedButton>
          <Button
            className="button feed green"
            onClick={() => onFeed(selectedCat)}
          >
            Feed
          </Button>
        </FeedButton> */}
        <FeedButton onFeed={onFeed} selectedCat={selectedCat} />
        <CleanButton onLitterClean={onLitterClean} selectedCat={selectedCat} />
      </div>
      <div className="manage-2">
        <AdoptButton onAdoptCat={onAdoptCat} />
        <CloseButton onCloseSelected={onCloseSelected} />
      </div>
    </div>
  );
}

function ShelterStats({ cats, adopted }) {
  const countCats = cats?.length;

  if (!countCats)
    return (
      <p className="all-adopted">Congratulations! All cats are adopted!</p>
    );

  return (
    <div className="shelter-stats">
      <h3>Shelter information</h3>
      <p>Cats in shelter: {countCats}</p>
      <p>Adopted cats: {adopted}</p>
    </div>
  );
}

// New code starts
// All button components
function Button({ children, className, onClick }) {
  return (
    <button className={className} onClick={onClick}>
      {children}
    </button>
  );
}

function ToggleAddCloseButton({ showAddCat, handleShowAddCat }) {
  return (
    <Button
      className={
        !showAddCat ? "button add-close pink" : "button add-close blue"
      }
      onClick={handleShowAddCat}
    >
      {!showAddCat ? "Add cat" : "Close and manage cats"}
    </Button>
  );
}

function AddCatButton({ showAddCat, cat, onSelection }) {
  return (
    <Button
      className={showAddCat ? "button disabled no-hover" : "button blue"}
      onClick={(e) => {
        if (showAddCat) {
          e.preventDefault();
          e.stopPropagation();
        } else {
          onSelection(cat);
        }
      }}
    >
      Manage
    </Button>
  );
}

function FeedButton({ onFeed, selectedCat }) {
  return (
    <Button className="button feed green" onClick={() => onFeed(selectedCat)}>
      Feed
    </Button>
  );
}

// FeedButton with component composition
// function FeedButton({ children }) {
//   return children;
// }

function CleanButton({ onLitterClean, selectedCat }) {
  return (
    <Button
      className="button clean-litter blue"
      onClick={() => onLitterClean(selectedCat)}
    >
      Clean
    </Button>
  );
}

function AdoptButton({ onAdoptCat }) {
  return (
    <Button className="button adopt blue" onClick={onAdoptCat}>
      Adopt
    </Button>
  );
}

function CloseButton({ onCloseSelected }) {
  return (
    <Button className="button pink" onClick={onCloseSelected}>
      Close
    </Button>
  );
}

// New code ends
