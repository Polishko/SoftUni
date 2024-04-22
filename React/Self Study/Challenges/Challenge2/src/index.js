import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const allSkills = [
    {
        name: "Python",
        icon: "💪",
        color: "#B9D7A3",
    },
    {
        name: "HTML+CSS",
        icon: "👌",
        color: "#1F55E5",
    },
    {
        name: "JavaScript",
        icon: "👌",
        color: "#EBD314",
    },
    {
        name: "GitHub",
        icon: "👍",
        color: "#ED4329",
    },
    {
        name: "React",
        icon: "👶",
        color: "#ED4329",
    },
];

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
    const skills = allSkills;
    const skillCount = skills.length;
    // const skillCount = 0

    if (skillCount === 0) {
        return "Acquiring new skills!";
    }

    return (
        <ul className="skill-list">
            {skills.map((skill) => (
                <Skill skillObj={skill} key={skill.name} />
            ))}
        </ul>
    );
}

function Skill({ skillObj }) {
    return (
        <li className="skill" style={{ backgroundColor: skillObj.color }}>
            <p>{skillObj.name}</p>
            <span>{skillObj.icon}</span>
        </li>
    );
}

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
    <StrictMode>
        <App />
    </StrictMode>
);
