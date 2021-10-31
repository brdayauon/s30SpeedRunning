public class EarthQuakeResistantBuilder implements builder{
    
    private home earthQuakeResistantHome = new home(); 

    @Override
    public void buildFloor() {
        this.earthQuakeResistantHome.floor = "Wooden Floor";
    }
    @Override
    public void buildWalls() {
        this.earthQuakeResistantHome.walls = "Wooden Walls";
    }
    @Override
    public void buildTerrace(){
        this.earthQuakeResistantHome.terrace = "Wooden Terrace";
    }
    @Override
    public home getComplexHomeObject(){
        return this.earthQuakeResistantHome;
    }
}
