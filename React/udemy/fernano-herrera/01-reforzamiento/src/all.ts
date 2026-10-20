// Objetos literales
const ironman = {
  firstName: "Fernando",
  lastName: "Herrera",
  age: 35,
};

const spiderman = { ...ironman, addres: "New York" };

ironman.firstName = "Tony";
ironman.lastName = "Stark";
ironman.age = 45;

console.log(ironman);
console.log(spiderman);

// functions

const getUser2 = () => ({
  uid: "ABC123",
  username: "fernandoherrera",
});

console.log(getUser2());

// destructuración de objetos

interface Hero {
  key: string;
  name: string;
  age: number;
  rank: number;
}

const useContext = ({ key, name, age, rank }: Hero) => {
  return {
    keyName: key,
    user: {
        name,
        age,
    },
    rank: rank,
  };
};
const newHero: Hero = {
    key: "ABC123",
    name: "Fernando Herrera",
    age: 35,
    rank: 1,
} 

const { keyName, user, rank } = useContext(newHero);
console.log(keyName, user.age, rank);