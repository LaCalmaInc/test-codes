import "./App.css";
import { pizzaData } from "./data";
import { Pizza } from "./components";
function App() {
  const pizza1 = pizzaData[0];
  return (
    <>
      <h1>Fast React Pizza Co.</h1>
      <h2>Our Menu</h2>
      <Pizza {...pizza1} />
    </>
  );
}

export default App;
