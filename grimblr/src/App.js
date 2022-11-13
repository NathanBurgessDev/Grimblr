import logo from './logo.png';
import './App.css';
import { useState } from 'react';
import APIService from './APIService';

function FormSubmit () {
  const [username, setUsername] = useState("");

  return (
    <div>
      <input
        class="inputs"
        type="text"
        value={username}
        onChange={(e) => { setUsername(e.target.value) }}
      />
      <br></br>
      <button class="buttons" onClick={() => APIService.InsertName(username)}>Submit</button>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p> Enter your twitter handle below! </p>
        <FormSubmit />
      </header>
    </div>
  );
}

export default App;
