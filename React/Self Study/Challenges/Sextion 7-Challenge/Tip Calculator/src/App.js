import { useState } from "react";
import "./styles.css";

export default function App() {
  const [bill, setBill] = useState(0);
  const [myTip, setMyTip] = useState(0);
  const [friendTip, setFriendTip] = useState(0);

  function handleChangeBill(e) {
    setBill(Number(e.target.value));
  }

  function handleChangeMyTip(e) {
    const calcValue = (Number(e.target.value) * bill) / 100;
    setMyTip(calcValue);
  }

  function handleChangeFriendTip(e) {
    const calcValue = (Number(e.target.value) * bill) / 100;
    setFriendTip(calcValue);
  }

  function handleReset() {
    setBill(0);
    setMyTip(0);
    setFriendTip(0);
  }

  return (
    <div className="App">
      <BillItem onChangeBill={handleChangeBill} bill={bill}>
        <span>How much was the bill?</span>
      </BillItem>
      <ServiceRating onChangeTip={handleChangeMyTip} tip={myTip}>
        <span>How did you like the service?</span>
      </ServiceRating>
      <ServiceRating onChangeTip={handleChangeFriendTip} tip={friendTip}>
        <span>How did your friend like the service?</span>
      </ServiceRating>
      <TotalPaid bill={bill} myTip={myTip} friendTip={friendTip} />
      <Reset onReset={handleReset} bill={bill} />
    </div>
  );
}

function BillItem({ onChangeBill, children, bill }) {
  return (
    <div>
      {children}
      <input type="text" value={bill} onChange={onChangeBill}></input>
    </div>
  );
}

function ServiceRating({ onChangeTip, children, tip }) {
  const satisfactionLevels = [
    { value: 0, text: "Dissatisfied (0%)" },
    { value: 5, text: "It was ok (5%)" },
    { value: 10, text: "It was good (10%)" },
    { value: 20, text: "Absolutely amazing (20%)" },
  ];
  return (
    <div>
      {children}
      <select value={tip} onChange={onChangeTip}>
        {satisfactionLevels.map((item) => (
          <option value={item.value} key={item.value}>
            {item.text}
          </option>
        ))}
      </select>
    </div>
  );
}

function TotalPaid({ bill, myTip, friendTip }) {
  if (!bill) return;

  const tipAverage = (myTip + friendTip) / 2;
  const totalPaid = bill + tipAverage;
  return (
    <p>
      You pay ${totalPaid} (${bill} + ${tipAverage} tip)
    </p>
  );
}

function Reset({ onReset, bill }) {
  if (!bill) return;
  return <button onClick={onReset}>Reset</button>;
}
