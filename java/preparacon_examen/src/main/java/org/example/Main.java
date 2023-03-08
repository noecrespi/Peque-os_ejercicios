package org.example;

public class Main {


    // C

    public void main(String[] args){
        // crear un objeto computerl
        Computer computer1 = new Computer("1", "Aula 1", 16, 500, 4);

        // muestra por pantalla el id y la clasificación de la calse computerl.
        System.out.println("Computer1 : id: " + computer1.getId() + " clasificacion: " + computer1.clasifica());

        // Crear un objeto arrayComputers de la clase ArrayComputers.
        ArrayComputers arrayComputers = new ArrayComputers();

        // Añadir el objeto computerl al Objeto computers.
        arrayComputers.addComputer(computer1);

        //Mostrar por pantalla la media de Ram de el aula "info1" de objeto computers.
        System.out.println("Media de Ram de el aula info1: " + arrayComputers.calculaMitjanaRamAula("info1"));
    }
    public class Computer {
        private String id;
        private String aula;
        private int ram;
        private int hd;
        private int speed;




        public Computer(String id, String aula, int ram, int hd, int speed) {
            this.id = id;
            this.aula = aula;
            this.ram = ram;
            this.hd = hd;
            this.speed = speed;

            // super(id, aula, ram, hd, speed);
        }
        public String getId() {
            return id;
        }

        public int getRam() {
            return ram;
        }

        public void setRam(int ram) {
            this.ram = ram;
        }

        public String clasifica() {
            String clasificacion;
            if (speed > 3 && ram > 16){
                clasificacion = "ultimate";
            } else {
                clasificacion = "normal";
            }
            return clasificacion;

        }

        public String getAula() {
            return aula;
        }
    }


    public class ArrayComputers {
        //Completa la clase ArrayComputers para trabajar con un array con un máximo de 100 Computer

        private Computer[] computers;
        private int numComputers;
        private final int MAX_COMPUTERS = 100;
        public ArrayComputers() {
            computers = new Computer[MAX_COMPUTERS];
            numComputers = 0;
        }
        public boolean addComputer(Computer computer) {
            if (numComputers < MAX_COMPUTERS) {
                computers[numComputers++] = computer;
            }
            return (numComputers < MAX_COMPUTERS);
        }

        //B
        public double calculaMitjanaRamAula(String aula){
            double media = 0.0;
            int ordenadores = 0;
            for (int i = 0; i < numComputers; i++) {
                if (computers[i].getAula().equals(aula)) {
                    media += computers[i].getRam();
                    ordenadores++;
                }
            }
            return media / ordenadores;

        }
    }

}
