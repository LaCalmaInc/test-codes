interface PizzaProps{
    name: string;
    ingredients: string;
    price: number;
    photoName: string;
    soldOut: boolean;
}

const Pizza = ({name, ingredients, price, photoName}: PizzaProps) =>{
    //const {name, ingredients, price, photoName} = props;
    return(
        <div>
            <img src={photoName} alt={name} />
            <h2>{name}</h2>
            <p>{ingredients}</p>
            <p>{price}</p>
        </div>
    )
}

export default Pizza;