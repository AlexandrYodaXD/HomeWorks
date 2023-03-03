/*
Реализуйте очередь с помощью LinkedList со следующими методами:
enqueue() - помещает элемент в конец очереди,
dequeue() - возвращает первый элемент из очереди и удаляет его,
first() - возвращает первый элемент из очереди, не удаляя.
 */
public class Task_2 {
    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.enqueue( 1);
        myQueue.enqueue( 2);
        myQueue.enqueue( 3);

        System.out.println(myQueue.first()); // 1
        myQueue.dequeue();
        System.out.println(myQueue.first()); // 2
        myQueue.dequeue();
        System.out.println(myQueue.first()); // 3
        myQueue.dequeue();
//        System.out.println(myQueue.first()); // exception
    }
}
