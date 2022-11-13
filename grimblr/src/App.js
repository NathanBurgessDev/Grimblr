import logo from './logo.png';
import React from 'react';
import './index.css';
import './App.css';
import Result from './result'
import { useState } from 'react';
import { InsertName } from './APIService';
import root from './index'

function DisplayData(data) {
  root.render(
    <React.StrictMode>
      <Result>{data}</Result>
    </React.StrictMode>,
  );
  
}

let parseResponse = (response) => {
  return response.json().then((json => {
    if (!response.ok) {
      return Promise.reject(json);
    }
    console.log(typeof(json))
    DisplayData(json);
  }))
}

function FormSubmit() {
  const [username, setUsername] = useState("");

  return (
    <div>
      <input
        className="inputs"
        type="text"
        value={username}
        onChange={(e) => { setUsername(e.target.value) }}
      />
      <br></br>
      <button className="buttons" onClick={() => InsertName(username).then(parseResponse)}>Submit</button>
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
