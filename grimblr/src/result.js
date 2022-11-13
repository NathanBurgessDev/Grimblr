import './App.css';
import logo from './logo.png';

function Result(data) {
    const [name, setData] = useState("");
    data = data.json
    return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>hello: {data}</p>
          </header>
        </div>
      );
}

export default Result;