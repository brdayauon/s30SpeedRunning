public class director {
    
    private builder builder;

    public director(builder  builderType){
        this.builder = builderType;
    }

    public home getComplexObjectOfHome()
    {
        return this.builder.getComplexHomeObject();
    }

    public void manageRequiredHomeConstruction(){
        this.builder.buildFloor();
        this.builder.buildWalls();
        this.builder.buildTerrace();
    }
}
