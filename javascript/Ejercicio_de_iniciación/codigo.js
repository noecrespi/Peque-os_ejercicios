
var mensaje = "Hola Mundo! \nQué facil es incluir 'comillas simples' y \"comillas dobles\" "

// Todo el código JavaScript se encuentre en un archivo externo llamado
// codigo.js y el script siga funcionando de la misma manera.
alert(mensaje);

// Después del primer mensaje, se debe mostrar otro mensaje que diga "Soy el
// primer script"
// Muestra el segundo mensaje 
alert("Soy el primer script")


//3
// imprime los meses del año en un alert
function printMeses() {
    let meses = ["Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre"]

    alert(meses)
}


//4
function frase() {

    //     1. Determinar cuál de los dos elementos de texto es mayor
    //      2. Utilizando exclusivamente los dos valores booleanos del array, determinar los
    // operadores necesarios para obtener un resultado true y otro resultado false
    // 3. Determinar el resultado de las cinco operaciones matemáticas realizadas con los
    // dos elementos numéricos

    let valores = [true, 5, false, "hola", "adios", 2];
}

function whatGigString() {

    
    // let palabras = true, 5 , false, "hola", "adios", 2
    // //document.getElementById('words')
    // //let palabra = ""
    
    // for(i in palabras){
    //     if(typeof i === 'string' || palabras instanceof String){
    //         console.log(i)
    //     }
    
    // }

    // //for (var i = 0 ; condición; actualización)
    // for (var i = 0; typeof palabras === 'string' || palabras instanceof String; palabra + 1)
    //     console.log(palabras)
    //     if (typeof palabras === 'string' || palabras instanceof String) {
    //         //it is string
    //         alert(palabras);
    //     } else {
    //         //it is not string
    //         alert(palabras);
       //}
}

function matteoperation() {
    //let words = document.getElementById("words")
    let word = [true, 5, false, "hola", "adios", 2]

    for (word = 0; Number.isInteger(word) === true ; word++) {
        console.log(word)
        // if (Number.isInteger(word)) {
        //     console.log(word) ;
        //     }
        // else{
        //     console.log('Uno');
        // }
        }
        
        
    }

//5
//Completar las condiciones de los if del siguiente script para que los mensajes de los alert() se muestren siempre de forma correcta:
function condiciones(){
    var numero1 = 5;
    var numero2 = 8;
    
    if(numero1 ) {
    alert("numero1 no es mayor que numero2");
    } if(numero2 > 0) {
    alert("numero2 es positivo");
    } if(numero1 >= 0) {
    alert("numero1 es negativo o distinto de cero");
    } if(numero1 ++ < numero2) {
    alert("Incrementar en 1 unidad el valor de numero1 no lo hace mayor o igual que numero2");
    }
}

//6
//El cálculo de la letra del Documento Nacional de Identidad (DNI)
function calcLetraDni(){
    let letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
        'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T'];
    
    let numDNI = prompt("Escribe los numeros de tu DNI")
    let letraDNI = prompt("Escribe la letra del dni que has metido anteriorente").toUpperCase()
    
    if(numDNI.length < 8 ){
        let mensaje = "El número proporcionado no es válido"
        document.getElementById("resulConversion").innerHTML = mensaje;
    } else {
        let posicionLetra = numDNI % 23
        let letra = letras[posicionLetra]
        
        if(letra == letraDNI){
            alert("El numero de la letra del DNI es correcto: " + numDNI + letra)
        } else{
            alert("El número de la letra que has puesto es erronio, en realidad para el DNI " + numDNI + " debería ser " + letra)
        }

    }
}

//B1 
// Calcular el peso de la luna
function whatPesoLuna(){
    let pesoTierra = prompt("Dime cuanto pesa en kilos")

    let pesoLuna = pesoTierra * 0.165

    document.getElementById("resulConversion").innerHTML = pesoLuna + " kg";
}

//B2
//Calcula tu Índice de Masa Corporal (IMC) 
function calcMasaCorpoarl(){
    let peso = prompt("¿Cúanto pesa? Pon el peso en kilogramos")
    let estatura = prompt("¿Cúal es tu estatuara? Pon el resultado en metros")

    let imc = peso / (Math.pow(estatura,2))

    if(imc < 18){
        document.getElementById("resulConversion").innerHTML = imc + "Peso bajo. Necesario valorar signos de desnutrición";
    } else if (imc >= 18 && imc <= 24.9) {
        document.getElementById("resulConversion").innerHTML = imc + "Normal";
    } else if (imc >= 25 && imc <= 26.9) {
        document.getElementById("resulConversion").innerHTML = imc + "Sobrepeso";
    } else if (imc >= 27 && imc <= 29.9) {
            document.getElementById("resulConversion").innerHTML = imc + "Obesidad grado I. Riesgo relativo alto para desarrollar enfermedades cardiovasculares";
    } else if (imc >= 30 && imc <= 39.9) {
        document.getElementById("resulConversion").innerHTML = imc + "Obesidad grado II. Riesgo relativo muy alto para el desarrollo de enfermedades cardiovasculares";
    } else {
        document.getElementById("resulConversion").innerHTML = imc + "Obesidad grado III Extrema o Mórbida. Riesgo relativo extremadamente alto para el desarrollo de enfermedades cardiovasculares";
    }

}


//B3
//Elabora un programa que solicite la medida en Pies y realice la conversión a pulgadas.
function piesAPulgadas(){
    let num = prompt("Introduce el número en pies")
    let resultado = num * 12

    document.getElementById("resulConversion").innerHTML = resultado + " pulgadas";
}

//B4
//El    abora un programa que solicite la medida en pulgadas y realice la conversión a cm y metros.

function pulgadasACm(){
    let num = prompt("Introduce el número en pulgadas")
    let resultado = num * 2.54

    document.getElementById("resulConversion").innerHTML = resultado + " cm";
}

//B5

function notaMediaClase(){
    let notaCiencia = 7
    let notaHistoria = 5.5
    let notaMatemáticas = 8
    let notaEducación = 5 

    let notas = []
    
    notas.push(notaCiencia, notaHistoria, notaMatemáticas,notaEducación)

    let sum = 0;

        for (let i = 0; i < notas.length; i += 1) {
            sum += notas[i];
        }
        
        document.getElementById("resulConversion").innerHTML = sum ;

}

//B6
//Realiza un programa para calcular salario semanal si el precio/hora es 10, hora extra a 15. El trabajador hora un total de 40 horas semanales y 4 horas extras.
function calcSalario(){
    let precioHora = prompt("Dime cuanto te pagan por hora") //10
    let precioHoraExtra = prompt("Dime cuanto te pagan por la hora extra") //15
    let horasContrato = prompt("¿Cuantas horas haces a la semana?") //40
    let horasExtras= prompt("¿Cuantas horas extras has hecho esta semana?") //4

    let resultado  = (horasContrato * precioHora) + (horasExtras * precioHoraExtra)

    document.getElementById("resulConversion").innerHTML = resultado
}

//B7
//Realizar programa en el que el ordenador “piensa” en un número al azar entre 1-50 y lo muestra por pantalla. Consulta la siguiente web para realizar la operación RANDOM para el número al azar. Usa la función .toFixed() para redondear o para convertirlo a enteros.   
function numRandom(){
    let numAlAzar = (Math.random() * 50) + 1
    let redondearNum = numAlAzar.toFixed()

    document.getElementById("demo").innerHTML = redondearNum
}


//B8
function organize2Num(){
    let num1 = prompt("Introduce un número")
    let num2 = prompt("Otro número un número")

    let nums = []

    nums.push(num1, num2)
    var ordenNum = nums.sort()
    document.getElementById("demo").innerHTML = ordenNum[0];
}    


function organize3Num(){
    let num1 = prompt("Introduce un número")
    let num2 = prompt("Otro número un número")
    let num3 = prompt("Otro número un número")

    let nums = []

    nums.push(num1, num2, num3)
    var ordenNum = nums.sort()
    document.getElementById("demo").innerHTML = ordenNum[0];
}