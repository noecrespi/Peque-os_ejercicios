//Escribe un programa que muestre una tabla de multiplicar como la siguiente:


function tabla(){


    // OPCION 1-> largo
    // fila = "";

    // // for (i= 0; i <= Range(10); i++){
    // //     fila1 = fila1 + "|" + (i + 1) + "\t";
    // // }

    // // 1 linea
    // for (i= 0; i < 10; i++){
    //     fila = fila + (i + 1) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 2 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 2) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 3 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 3) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 4 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 4) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 5 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 5) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 6 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 6) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 7 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 7) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 8 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 8) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 9 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 9) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // // 10 linea
    // for (i= 1; i < 11; i++){
    //     fila = fila + (i * 10) + "\t";
    // }
    // // punto a parte
    // fila = fila + "\n";

    // console.log(fila);




    // OPCION 2 -> corto
    fila = "";

    multiplicar = [1,2,3,4,5,6,7,8,9,10];

    for (i= 0; i < multiplicar.length; i++){
        for (j= 1; j < 11; j++){
            fila = fila + (j * multiplicar[i]) + "\t";
        }
        // punto a parte
        fila = fila + "\n";
    }

    console.log(fila);

}

tabla();


