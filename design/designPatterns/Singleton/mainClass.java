import org.graalvm.compiler.nodes.memory.MemoryCheckpoint.Single;

public class mainClass {
    public static void main(String[] args) {
        singletonClass singletonObject = singletonClass.getInstance();
        singletonObject.simpleMethod();

        singletonClass singletonObject2 = singletonClass.getInstance();
        singletonObject2.simpleMethod();
    }
}
