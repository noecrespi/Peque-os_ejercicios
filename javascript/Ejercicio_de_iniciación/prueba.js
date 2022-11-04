
    let palabras = [true, 5, false, "hola", "madagascar", "adios", 2];
    let isBoolean = [];
    
    // mete los booleanos en el array isBoolean
    for (i in palabras) {
        if(typeof palabras[i]=== "boolean"){
            isBoolean.push(palabras[i])
        }
    }
    
    console.log(isBoolean)


    // Cambia el valor del booleano por su contrario
    for(i in isBoolean) {
        if(isBoolean[i] === false){
            isBoolean[i] = true
        } 
        else {
            isBoolean[i] = false
        }
    } 
    
    console.log(isBoolean)
    document.getElementById("resulConversion").innerHTML = isBoolean;


    // console.log("suma " + suma)
    // console.log("resta " + resta)
    // console.log("multiplicar " +  multiplicar)
    // console.log("dividir " +  dividir)
    
    // document.getElementById("resulConversion").innerHTML = "suma " + suma;
    // document.getElementById("resulConversion").innerHTML = "resta " + resta;
    // document.getElementById("resulConversion").innerHTML = "multiplicar " +  multiplicar;
    // document.getElementById("resulConversion").innerHTML = "dividir " +  dividir;
