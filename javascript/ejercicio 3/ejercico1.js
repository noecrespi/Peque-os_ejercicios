var equip_ciclista = {
    team: "alfa-lum-1983",
    ciclistes: [
        {
            nom: "Juan Alonso",
            born: "08/01/1958",
            height: 1.92,
            tours: 0,
            wins: 12,
        }, {
            nom: "Josh Pantono",
            born: "25/10/2000",
            height: 1.84,
            tours: 3,
            wins: 12,
        }, {
            nom: "Bid Seville",
            born: "12/07/1993",
            height: 1.88,
            tours: 3,
            wins: 3,
        }, {
            nom: "Zolz Brucker",
            born: "08/09/1984",
            height: 1.72,
            tours: 0,
            wins: 1,
        }, {
            nom: "Otto Verdes",
            born: "19/02/1979",
            height: 1.92,
            tours: 0,
            wins: 12,
        }, {
            nom: "Bert Poel",
            born: "03/06/1995",
            height: 1.99,
            tours: 1,
            wins: 2,
        }, 
    ]
}

var ciclistes = equip_ciclista.ciclistes

// Año actual
let ActualYear = new Date().getFullYear()


// 1. Imprime nombres: Imprime los nombres de los ciclistas, según el orden natural del array.

function names(){
    let names = "";

    for (let i = 0 ; i < equip_ciclista.ciclistes.length; i++){
        names += equip_ciclista.ciclistes[i].nom + ", ";
        // console.log(equip_ciclista.ciclistes[i].nom);
    }
    console.log(names.slice(0, -2));
}

//names();



// 2. Imprime nombres ordenados alfabéticamente: Imprime los nombres de los ciclistas ordenados alfabéticamente.

function namesAlphabetically(){
    let names = []

    // mete los nombres en un array
    for (let i = 0 ; i < equip_ciclista.ciclistes.length; i++){
        names.push(equip_ciclista.ciclistes[i].nom);
    }
    // ordenar alfabeticamente
    names.sort();
    // imprimir sin que se vea como una lista
    names = names.join(", ");

    console.log(names);
}

//namesAlphabetically()



// 3. Imprime nombres ordenados por altura y luego saca la lista de los nombres ordenada por altura, de los más altos a los más bajos.

function orderHeight(){
    // var height = {}

    // prueba 1
    // ordenar la liata de ciclistas por altura
    var h = equip_ciclista.ciclistes.sort(function(a,b){
        return b.height - a.height
    })

    // imprime los nombres 
    ordenHeight = "";
    h.forEach(function(a){
        ordenHeight += a.nom + ", "
        console.log()
    })
    // imprime en pantalla 
    // quitamos los dos últimos caracteres del string 
    console.log(ordenHeight.slice(0,-2))



    // prueba 1 
    // for (let i = 0; i < equip_ciclista.ciclistes.length; i++){
    //     // height.push(equip_ciclista.ciclistes[i].height)
    //     height[equip_ciclista.ciclistes[i].nom] = equip_ciclista.ciclistes[i].height;
        
    //     // console.log(height)
    // }

    
    // que hace el objeto keys: https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Object/keys

    // var key = Object.keys(height);
    // console.log(Object.keys(height).sort().reverse());


    // ordenar las claves de mayor a menor
    // key.sort(function(a, b){return b-a});
    // console.log(key)
    // for (let i = 0; i < key.length; i++){
    //     // console.log(height[key[i]]);
    // }

    
    
    //console.log(height)
    // height.sort()
    //console.log(key)

}

//orderHeight()



// 4. Imprime nombres de ciclistas de mejor a peor: Ordena de mejor a peor, teniendo en cuenta que el mejor ciclista es el que tiene más tours, y si empatan a tours, es mejor el que tiene más wins. Imprime los nombres ordenados y también el número de tours y de wins.

function betterCiclistas(){

    // ordenar de mejor a peor cicliatas por los tours 
    let order = equip_ciclista.ciclistes.sort(function(a,b){
        return b.tours - a.tours
    }) 
    
    // si hay empate en tours, ordenar por wins
    for(let i = 0; i < (order.length)-1 ; i++){
        if(order[i].tours == order[i+1].tours){
            console.log("empate")
            console.log(order)
            if(order[i].wins < order[i+1].wins){
                // guarda la variable siguiente para no perderla
                let aux = order[i+1];

                order[i+1] = order[i]
                order[i] = aux
            // si es la ultima posicion y hay empate en tours, ordenar por wins
            console.log(order[i])
            }
        }
    }
    console.log(order)
}

// betterCiclistas()



// 5. Utiliza map() para añadir un tour a todos los ciclistas.
function moreTour(){
    let moreTour = []

    //  Utiliza map() para añadir un tour a todos los ciclistas.
    moreTour = equip_ciclista.ciclistes.map(function(ciclista){
        ciclista.tours += 1;
        return ciclista;
        console.log(ciclista)
    })
    
    console.log(moreTour)
}

//moreTour()

// 6. Utiliza filter() para eliminar todos los ciclistas menores de 30 años

function deleteCiclistas(){

    let ageDelete = 30
        

    let years = equip_ciclista.ciclistes
    // console.log(years);

    // elimina los ciclistas menores de 30 años con el find()
    let contar = 0 

    cyclingDelete = []



    ciclistes1 = ciclistes.find(element => {
        let born = element.born.split("/")[2]
        let age = element.born
        let name = element.nom
        let ageCycling = ActualYear - born
        //console.log(ageCycling);
        
        if (ageCycling < ageDelete){
            //console.log(element)
            cyclingDelete.push(element)
            //return element.nom
        }
        
    })
    

    for(let i = 0; i < ciclistes.length; i++){
        for(let j = 0; j < cyclingDelete.length; j++){
            if(ciclistes[i].nom == cyclingDelete[j].nom){
                ciclistes.splice(i,1)
            }
        }
    }


    console.log(ciclistes)

    function findYear(year, ageDelete, contar){
        // let born =  years[contar].born
        let born =  years[element].born
        // console.log(born);
        let bornYear = born.split("/")[2]
        // console.log(bornYear);
        let age = year - bornYear
        age = parseInt(age);
        console.log(age);

        // elimina los ciclistas menores de 30 años
        if ( age > ageDelete){
            years.splice(contar)
        }
        contar += 1
}
//  no entiendo porque no funciona el find
    // for (let i = 0; i < years.length; i++){
    //     console.log(years.find(element  =>{
    //         let born =  element.born
    //         // console.log(born);
    //         let bornYear = born.split("/")[2]
    //         // console.log(bornYear);
    //         let age = year - bornYear
    //         age = parseInt(age);
    //         console.log(age);
    
    //         // elimina los ciclistas menores de 30 años
    //         if ( age > ageDelete){
    //             years.splice(element)
    //         }
    //         i += 1
    //     }))
    // }





    // console.log(years.find(element  =>{
    //     let born =  element.born
    //     // console.log(born);
    //     let bornYear = born.split("/")[2]
    //     // console.log(bornYear);
    //     let age = year - bornYear
    //     age = parseInt(age);
    //     console.log(age);

    //     // elimina los ciclistas menores de 30 años
    //     if ( age > ageDelete){
    //         years.splice(element)
    //     }
    //     element += 1
    // }))




    // hace un filtro muy raro, no me funciona
    // for (let i = 0 ; i <= years.length; i++){
    //     // coge la fecha de nacimiento
    //     let born =  years[i].born
    //     // coge el año de nacimiento
    //     let bornYear = born.split("/")[2]
    //     // calcula la edad
    //     let age = year - bornYear
    //     console.log(year);
    //     console.log(bornYear);
    //     console.log(age);

    //     age = parseInt(age);
    //     // elimina los ciclistas menores de 30 años
    //     if ( age > ageDelete){
    //         years.splice(i,1)
    // }}
    

    // let bornYear = years.born.split("/")[2]
    // let age = year - bornYear

    // let lista = [];
    // for(let i = 1; i < years.length; i++){
    //     let born =  years[i].born
    //     let bornYear = born.split("/")[2]
    //     console.log(bornYear)
    //     let age = year - bornYear
    //     console.log(age)

        // elimina los ciclistas menores de 30 años
        

        // no me va el filter
        //let lista = years.filter((age) => age !== age > ageDelete)
        
        
    // }


}
 

//deleteCiclistas();




// 7. Utiliza find() para encontrar el primer ciclista que tiene más de 30 años.

function findBigCycling(){

    let ageMax = 30
    
    // console.log(born);
    ciclistes.find(element => {
        let born = element.born.split("/")[2]
        let ageCycling = ActualYear - born
        //console.log(ageCycling);
        // return ageCycling > ageMax
        
        if (ageCycling > ageMax){
            console.log(element.nom)
            return element.nom
            
    }})
}

//findBigCycling()



// 8. Añade un ciclista a la posición 2 con los siguientes datos:

    // nom: "Josh Pantano",
    // born: "30/11/1995",
    // height: 1.88,
    // tours: 2,
    // wins: 9


function addCycling(){
    
        let newCycling = {
            nom: "Josh Pantano",
            born: "30/11/1995",
            height: 1.88,
            tours: 2,
            wins: 9
        }
    
        ciclistes.splice(2, 0, newCycling)
        console.log(ciclistes)
}

//addCycling()

// 9. Imprime nombres ordenados por edad: de más jóvenes a más viejos.

function orderAge(){
    
    let born = ciclistes.sort(function(a,b){
        return parseInt(b.born.split("/")[2]) - parseInt(a.born.split("/")[2])
    })
    //console.log(born)

    ordenHeight = "";
    born.forEach(function(a){
        ordenHeight += a.nom + ", "
    })

    console.log(ordenHeight.slice(0,-2))
}

orderAge()
