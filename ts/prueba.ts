interface character {
    id: number;
    name: string;
    status: string;
    species: string;
    type: string;
    gender: string;
    origin: {
        name: string;
        url: string;
    };
    location: {
        name: string;
        url: string;
    };
    image: string;
    episode: string[];
    url: string;
    //created: string;
}

const wait = async(seconds: number) => {
    return new Promise((resolve) => {
        setTimeout(resolve, seconds * 1000);
    });
}

const getchar = async():Promise<character> => {
    await wait(2);
    const response = await fetch('https://rickandmortyapi.com/api/character/2')
    const resolve = await response.json();
    //console.log(resolve);
    return resolve;
}

const getCharacterName = async() =>{
    const pj = await getchar();
    return pj.name;
}

const mensaje = async() =>{
    const nombre = await getCharacterName();
    console.log(`Hola a todos mi nombre es ${nombre}`);
}

mensaje();

//-----------------------------

async function getchar2():Promise<character>{
    await wait(4);
    const response = await fetch('https://rickandmortyapi.com/api/character/5')
    const resolve = await response.json();
    return resolve;
}

const p2 = getchar2().then((pj)=>{
    console.log('El nombre del personaje es:', pj.name);
})

