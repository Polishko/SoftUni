// Solution after lecture
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
      <Accordion data={faqs} />
    </div>
  );
}

function Accordion({ data }) {
  return (
    <ul className="accordion">
      {data.map((el, i) => (
        <AccordionItem
          title={el.title}
          number={i}
          text={el.text}
          key={el.title}
        />
      ))}
    </ul>
  );
}

function AccordionItem({ title, text, number }) {
  const [isOpen, setIsOpen] = useState(false);

  function handleToggle() {
    setIsOpen((openStatus) => !openStatus);
  }

  return (
    <li className={`item ${isOpen ? "open" : ""}`} onClick={handleToggle}>
      <p className="number">{number < 9 ? `0${number + 1}` : number + 1}</p>
      <p className="text">{title}</p>
      <p className="icon">{isOpen ? "-" : "+"}</p>
      {isOpen && <div className="content-box">{text}</div>}
    </li>
  );
}


// Initial solution
// import "./styles.css";
// import { useState } from "react";

// const faqs = [
//   {
//     title: "Where are these chairs assembled?",
//     text: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Accusantium, quaerat temporibus quas dolore provident nisi ut aliquid ratione beatae sequi aspernatur veniam repellendus.",
//   },
//   {
//     title: "How long do I have to return my chair?",
//     text: "Pariatur recusandae dignissimos fuga voluptas unde optio nesciunt commodi beatae, explicabo natus.",
//   },
//   {
//     title: "Do you ship to countries outside the EU?",
//     text: "Excepturi velit laborum, perspiciatis nemo perferendis reiciendis aliquam possimus dolor sed! Dolore laborum ducimus veritatis facere molestias!",
//   },
// ];

// export default function App() {
//   return (
//     <div>
//       <Accordion />
//     </div>
//   );
// }

// function Accordion() {
//   return (
//     <div className="content-box">
//       <ul className="accordion">
//         {faqs.map((faq, index) => (
//           <Item item={faq} index={index} key={index} />
//         ))}
//       </ul>
//     </div>
//   );
// }

// function Item({ item, index }) {
//   const [openStatus, setOpenStatus] = useState(false);

//   function handleClick() {
//     setOpenStatus((openStatus) => !openStatus);
//   }

//   return (
//     <li className={`item ${openStatus ? "open" : ""}`}>
//       <span className="number">{`0${index + 1}`}</span>
//       <div>
//         <p className="title">{item.title}</p>
//         {openStatus === true && <p>{item.text}</p>}
//       </div>
//       <span className="icon" onClick={handleClick}>
//         {openStatus ? "-" : "+"}
//       </span>
//     </li>
//   );
// }
