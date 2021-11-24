import { useState } from "react";
import { useEffect } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [value, setValue] = useState("");
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
    .then((response) => response.json())
    .then((json) => {
      setCoins(json);
      setLoading(false);
    })
  },[])
  const onChange = (event) => setValue(event.target.value);
  return (       
    <div>
      <h1>The Coins! {loading ? "" : `(${coins.length})`}</h1>
      {loading ? <b>loading...</b> 
        :
        <div>
          <input
          type = "number" 
          placeholder = "Write the USD"
          value = {value}
          onChange = {onChange}
        />
          <select>
            {coins.map((coin) =>        
              <option key = {coin.id}>
                {coin.name} ({coin.symbol}) {value? (coin.quotes.USD.price / value) : 0}
              </option>
            )}
          </select>
        </div>        
      }  
    </div>
  );
}

export default App;
