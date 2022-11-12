import logo from './logo.svg';
import './App.css';
import { useState } from 'react';


function handleInput(username) {
  alert(username);
}

function FormSubmit () {
  const [username, setUsername] = useState("");

  return (
    <div>
      <input
        type="text"
        value={username}
        onChange={(e) => { setUsername(e.target.value) }}
      />
      <button onClick={() => handleInput(username)}>Submit</button>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <FormSubmit />
      </header>
    </div>
  );
}

export default App;
