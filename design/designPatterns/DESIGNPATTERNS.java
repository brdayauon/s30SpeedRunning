// public class DESIGNPATTERNS {
    
// }
/*
Well documented and understood by software architects,designers,developers, application within a specific solution will be understood. 

Patterns give a software dev an array of tried and tested solutions to common problems, reducing the technical risk to the project by not having to employ a new and untested
design, this saves time and effort during implementation stage of the software development lifecycle.

Language neutral and can be applied to any language that supports OOP.
*/

//Creational Patterns? 
- way of creating objects. 

Divided into five parts.. factory method/abstract factory/ builder/ prototype/ singleton 


Factory Pattern - 

Main Class -> Factory Class -> Profession that branches into (engineer, doctor, teacher)
Don't expose the creation logic to the client and refer the created object using a standard interface. 
AKA VIRTUAL CONSTRUCTOR.  

Steps 
0) Create main class that calls Factory class
1) Create interface.
2) Create sub classes of profession
3) Create factory for it. 

'
Abstract Factory Pattern - 
Factory is aka  factory of factories. 
Abstract factory lets a class returns a factory of classes.  

Steps
1) Create main class which call factory of factory class. 
2) Factory of Factory/Factory producer creates instance of factory class. 
3) Factory class returns required class instance .

Single Pattern - 
Pattern involves a single class which is responsible to create an object while making sure
that only single object gets created. 
Provies a way to access its only object which can be accessed directly without 
need to instantiate the object of the class.

Steps 
1) Private static new keyword once only
2) private constructor
3) Getter no setter 

Prototype Design Pattern - 

Main Class -> load cache 

Builder Design Pattern - 

Complex Object .. home class 
Complex Object - Home (complex object which will generate with builder design pattern)

Steps:
-Create complex class home
-Create Builder Interface/Abstract class which has definitions
-Create concrete Builder class that has implementations 
-Create director that will have responsibility to call correct concrete builder and then return
final object 
-Create main class that will initialize directory, and call method of directory finally
which will in turn return complex object instance required.