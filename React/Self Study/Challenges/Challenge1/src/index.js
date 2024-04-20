import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

function App() {
  return (
    <div className="card">
      <Avatar photoName="/avatar.png" name="avatar" />
      <div className="data">
        <Intro
          name="Niya Mateeva Yondzhju"
          information="Learning Python and JS Front-End at SoftUni; Independent localization professional; Academic background; Cat human; Loves hiking and playing the flute."
        />
        <SkillList />
      </div>
    </div>
  );
}

function Avatar(props) {
  return <img className="avatar" src={props.photoName} alt={props.name}></img>;
}

function Intro(props) {
  return (
    <div>
      <h1>{props.name}</h1>
      <p>{props.information}</p>
    </div>
  );
}

function SkillList() {
  return (
    <div className="skill-list ">
      <Skill name="Python" icon="💪" color="#B9D7A3" />
      <Skill name="HTML+CSS" icon="👌" color="#1F55E5" />
      <Skill name="JavaScript" icon="👌" color="#EBD314" />
      <Skill name="GitHub" icon="👍" color="#ED4329" />
      <Skill name="React" icon="👶" color="#ED4329" />
    </div>
  );
}

function Skill(props) {
  return (
    <div className="skill" style={{ backgroundColor: props.color }}>
      <p>{props.name}</p>
      <span>{props.icon}</span>
    </div>
  );
}

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
