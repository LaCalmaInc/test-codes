import  s from "./App.module.css";
import { pizzaData } from "./data";
import { Pizza } from "./components";
function App() {
  const pizza1 = pizzaData[0];
  return (
    <>
      <div className={s.header}>
        <h1 >Fast React Pizza Co.</h1>
        <h2>Our Menu</h2>
      </div>
      <Pizza {...pizza1} />
    </>
  );
}

export default App;
