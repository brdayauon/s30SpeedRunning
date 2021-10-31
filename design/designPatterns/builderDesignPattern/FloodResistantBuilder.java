public class FloodResistantBuilder implements builder{

    private home floodResistantHome = new home(); 
    
    @Override
    public void buildFloor(){
        floodResistantHome.floor = "10 feet above the ground";
    }
    @Override
    public void buildWalls(){
        floodResistantHome.walls = "Water resistant walls";
    }
    @Override
    public void buildTerrace(){
        floodResistantHome.terrace = "Water leakage resistant terrace";
    }
    @Override
    public home getComplexHomeObject(){
        return this.floodResistantHome;
    }
}
