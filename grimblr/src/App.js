import logo from './logo.svg';
import './App.css';

var handle = ""

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <input type="text" onChange={(e)=>setHandle(e.target.value)}/>
        <button onclick={onSubmit}> Submit</button>
      </header>
    </div>
  );
}

function onSubmit() {
  // send handle to api call
}

function setHandle(text) {
  handle = text
}
export default App;
