import { useState } from "react";

function App() {
  const [toDo, setToDo] = useState("");
  const [toDos, setToDos] = useState([]);
  const onChange = (event) => setToDo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (toDo === "") {
      return;
    }
    setToDos((currentArray) => [toDo, ...currentArray]);
    setToDo("");
  };
  
  return (       
    <div>
      <h1>To Do List ({toDos.length})</h1>
      <form onSubmit = {onSubmit}>
        <input
          value = {toDo}
          onChange = {onChange}
          placeholder = "Write your toDo"
        />
        <button>Add</button>
      </form>
      <hr />
      <ul>
        {toDos.map((item, index) => <li key = {index}>{item}</li>)}
      </ul>
    </div>
  );
}

export default App;
