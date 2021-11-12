import {useState, useEffect} from "react";
import style from "./App.module.css";

function App() {
  const [bright, setBright] = useState(false);
  useEffect(() => {
    console.log("I run when 'bright' changes.");    
  },[bright]);
  const onClick = () => setBright((prev) => !prev);
  return (       
    <div className = {bright ? style.color : null}>      
      <button onClick = {onClick}>{bright ? "Bright" : "Dark"}</button>
      <h1>React</h1>
      <p>
        React is a JavaScript library for building user interfaces.
      </p>
    </div>
  );
}

export default App;
