// Improvements made after watching the lecture

// `https://api.frankfurter.app/latest?amount=100&from=EUR&to=USD`

import { useState, useEffect } from "react";

export default function App() {
  const [inputValue, setInputValue] = useState(1);
  const [inputCurr, setInputCurr] = useState("EUR");
  const [outputCurr, setOutputCurr] = useState("USD");
  const [outputValue, setOutputValue] = useState("");
  const [error, setError] = useState("");
  const [wrongInputMessage, setWrongInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  useEffect(
    function () {
      const controller = new AbortController();

      async function fetchOutput() {
        if (!inputValue) return;

        try {
          setIsLoading(true);
          setError("");
          const res = await fetch(
            `https://api.frankfurter.app/latest?amount=${inputValue}&from=${inputCurr}&to=${outputCurr}, {signal: controller.signal}`
          );
          if (!res.ok) {
            throw new Error("Something went wrong");
          }
          const data = await res.json();
          if (!data.rates || !data.rates[outputCurr]) {
            throw new Error("Invalid response data");
          }
          const newValue = data.rates[outputCurr];
          setOutputValue(newValue);
        } catch (err) {
          if (err.name !== "AbortError") {
            setError(err.message);
          }
        } finally {
          setIsLoading(false);
        }
      }

      if (inputCurr === outputCurr) {
        return setOutputValue(inputValue);
      }

      fetchOutput();
      return function () {
        controller.abort();
      };
    },
    [inputValue, inputCurr, outputCurr]
  );

  function handleInput(value) {
    if (!isNaN(value) && value.trim() !== "") {
      setInputValue(value);
    }
  }

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => handleInput(e.target.value)}
        // disabled={isLoading} //But this actually prevents me adding new digits
      />
      <select
        value={inputCurr}
        onChange={(e) => setInputCurr(e.target.value)}
        disabled={isLoading}
      >
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="CAD">CAD</option>
        <option value="INR">INR</option>
      </select>
      <select
        value={outputCurr}
        onChange={(e) => setOutputCurr(e.target.value)}
        disabled={isLoading}
      >
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="CAD">CAD</option>
        <option value="INR">INR</option>
      </select>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <>
          {wrongInputMessage && <p>{wrongInputMessage}</p>}
          {error && <p>{error}</p>}
          {outputValue !== 0 && !wrongInputMessage && !error && (
            <p>
              {outputValue} {outputCurr}
            </p>
          )}
        </>
      )}
    </div>
  );
}

// Pre-lecture solution

// // `https://api.frankfurter.app/latest?amount=100&from=EUR&to=USD`

// import { useState, useEffect } from "react";

// export default function App() {
//   const [inputValue, setInputValue] = useState("");
//   const [inputCurr, setInputCurr] = useState("EUR");
//   const [outputCurr, setOutputCurr] = useState("USD");
//   const [outputValue, setOutputValue] = useState("");
//   const [error, setError] = useState("");
//   const [wrongInputMessage, setWrongInputMessage] = useState("");

//   useEffect(
//     function () {
//       const controller = new AbortController();

//       async function fetchOutput() {
//         if (inputValue !== "" && typeof inputValue !== "number") {
//           setWrongInputMessage("Please enter valid input");
//           return;
//         }
//         try {
//           setError("");
//           const res = await fetch(
//             `https://api.frankfurter.app/latest?amount=${inputValue}&from=${inputCurr}&to=${outputCurr}, {signal: controller.signal}`
//           );
//           if (!res.ok) {
//             throw new Error("Something went wrong");
//           }
//           const data = await res.json();
//           if (inputValue !== "" && (!data.rates || !data.rates[outputCurr])) {
//             throw new Error("Invalid response data");
//           }
//           const newValue = data.rates[outputCurr];
//           setOutputValue(newValue);
//         } catch (err) {
//           if (err.name !== "AbortError") {
//             setError(err.message);
//           }
//         }
//       }
//       fetchOutput();
//       return function () {
//         controller.abort();
//       };
//     },
//     [inputValue, inputCurr, outputCurr]
//   );

//   return (
//     <div>
//       <input
//         type="text"
//         value={inputValue}
//         onChange={(e) => setInputValue(Number(e.target.value))}
//       />
//       <select value={inputCurr} onChange={(e) => setInputCurr(e.target.value)}>
//         <option value="USD">USD</option>
//         <option value="EUR">EUR</option>
//         <option value="CAD">CAD</option>
//         <option value="INR">INR</option>
//       </select>
//       <select
//         value={outputCurr}
//         onChange={(e) => setOutputCurr(e.target.value)}
//       >
//         <option value="USD">USD</option>
//         <option value="EUR">EUR</option>
//         <option value="CAD">CAD</option>
//         <option value="INR">INR</option>
//       </select>
//       {wrongInputMessage && <p>{wrongInputMessage}</p>}
//       {error && <p>{error}</p>}
//       {outputValue !== 0 && !wrongInputMessage && !error && (
//         <p>{outputValue}</p>
//       )}
//     </div>
//   );
// }
