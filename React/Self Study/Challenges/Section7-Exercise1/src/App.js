import "./styles.css";
import { useState } from "react";

const faqs = [
  {
    title: "Where are these chairs assembled?",
    text: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Accusantium, quaerat temporibus quas dolore provident nisi ut aliquid ratione beatae sequi aspernatur veniam repellendus.",
  },
  {
    title: "How long do I have to return my chair?",
    text: "Pariatur recusandae dignissimos fuga voluptas unde optio nesciunt commodi beatae, explicabo natus.",
  },
  {
    title: "Do you ship to countries outside the EU?",
    text: "Excepturi velit laborum, perspiciatis nemo perferendis reiciendis aliquam possimus dolor sed! Dolore laborum ducimus veritatis facere molestias!",
  },
];

export default function App() {
  return (
    <div>
      <Accordion />
    </div>
  );
}

function Accordion() {
  return (
    <div className="content-box">
      <ul className="accordion">
        {faqs.map((faq, index) => (
          <Item item={faq} index={index} key={index} />
        ))}
      </ul>
    </div>
  );
}

function Item({ item, index }) {
  const [openStatus, setOpenStatus] = useState(false);

  function handleClick() {
    setOpenStatus((openStatus) => !openStatus);
  }

  return (
    <li className={`item ${openStatus ? "open" : ""}`}>
      <span className="number">{`0${index + 1}`}</span>
      <div>
        <p className="title">{item.title}</p>
        {openStatus === true && <p>{item.text}</p>}
      </div>
      <span className="icon" onClick={handleClick}>
        {openStatus ? "-" : "+"}
      </span>
    </li>
  );
}
