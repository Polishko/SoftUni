import "./styles.css";
import { useState } from "react";

export default function App() {
  return (
    <div className="App">
      <Counter />
    </div>
  );
}

function Counter() {
  const [step, setStep] = useState(1);
  const [count, setCount] = useState(0);

  const days = step * count;

  const currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + days);
  const formattedDate = currentDate.toDateString();

  let message = `Today is ${formattedDate}`;
  if (count < 0) message = `${Math.abs(days)} ago was ${formattedDate}`;
  if (count > 0) message = `${days} days from today is ${formattedDate}`;

  return (
    <>
      <p className="step">
        <button
          onClick={() => {
            if (step > 1) setStep((s) => s - 1);
          }}
        >
          -
        </button>
        {`Step: ${step}`}
        <button onClick={() => setStep((s) => s + 1)}>+</button>
      </p>
      <p className="count">
        <button onClick={() => setCount((s) => s - 1)}>-</button>
        {`Count: ${count}`}
        <button onClick={() => setCount((s) => s + 1)}>+</button>
      </p>
      <p className="result">{message}</p>
    </>
  );
}
