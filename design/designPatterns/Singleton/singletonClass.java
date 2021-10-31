public class singletonClass {
    private static singletonClass singletonInstance = new singletonClass();

    private singletonClass() {

    }

    public static singletonClass getInstance(){
        return singletonInstance;
    }
    public void simpleMethod() {
        System.out.println("hashcode of singleton object" + singletonInstance);
    }
}
