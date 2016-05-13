Three types of patterns:

1)  Creational
    Creational patterns are ones that create objects for you, rather than having you instantiate objects directly. This gives your program more flexibility in deciding which objects need to be created for a given case.
      i) Abstract factory pattern groups object factories that have a common theme.
     ii) Builder pattern constructs complex objects by separating construction and representation.
    iii) Factory method pattern creates objects without specifying the exact class to create.
     iv) Prototype pattern creates objects by cloning an existing object.
      v) Singleton pattern restricts object creation for a class to only one instance.

2)  Structural:
    These concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionality.

      i) Adapter allows classes with incompatible interfaces to work together by wrapping its own interface around that of an already existing class.
     ii) Bridge decouples an abstraction from its implementation so that the two can vary independently.
    iii) Composite composes zero-or-more similar objects so that they can be manipulated as one object.
     iv) Decorator dynamically adds/overrides behaviour in an existing method of an object.
      v) Facade provides a simplified interface to a large body of code.
     vi) Flyweight reduces the cost of creating and manipulating a large number of similar objects.
    vii) Proxy provides a placeholder for another object to control access, reduce cost, and reduce complexity.


3)  Behavioral
    Most of these design patterns are specifically concerned with communication between objects.

      i) Chain of responsibility delegates commands to a chain of processing objects.
     ii) Command creates objects which encapsulate actions and parameters.
    iii) Interpreter implements a specialized language.
     iv) Iterator accesses the elements of an object sequentially without exposing its underlying representation.
      v) Mediator allows loose coupling between classes by being the only class that has detailed knowledge of their methods.
     vi) Memento provides the ability to restore an object to its previous state (undo).
    vii) Observer is a publish/subscribe pattern which allows a number of observer objects to see an event.
   viii) State allows an object to alter its behavior when its internal state changes.
     ix) Strategy allows one of a family of algorithms to be selected on-the-fly at runtime.
      x) Template method defines the skeleton of an algorithm as an abstract class, allowing its subclasses to provide concrete behavior.
     xi) Visitor separates an algorithm from an object structure by moving the hierarchy of methods into one object.
