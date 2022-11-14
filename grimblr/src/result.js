import './App.css';
import { useEffect, useState } from 'react';
import logo from './logo.png';

function Result(data) {
    data = data.json
    const [name, setName] = useState("");
    const changeName = () => setName(data);
    
    useEffect(() => {
        changeName();
    }, []);

    return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>hello: {name}</p>
          </header>
        </div>
      );
}

export default Result;