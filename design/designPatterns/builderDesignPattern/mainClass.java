public class mainClass {
    public static void main(String[] args){

        EarthQuakeResistantBuilder earthQuakeResistantBuilder = new EarthQuakeResistantBuilder();

        director director = new director(earthQuakeResistantBuilder);

        director.manageRequiredHomeConstruction();

        home homeConstructedAtTheEnd = director.getComplexObjectOfHome();
        
        System.out.println(homeConstructedAtTheEnd);
        System.out.println(homeConstructedAtTheEnd.floor);
    }
    
}
