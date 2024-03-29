package figure.polygon;

import figure.Figure;

import java.util.ArrayList;
import java.util.List;

public abstract class Polygon extends Figure {
    protected List<Double> sides = new ArrayList<>();

    protected Polygon(double... sides) throws Exception {
        for (double side :
                sides) {
            if (side <= 0){
                throw new Exception("Многоугольник с такими сторонами не может существовать.");
            }
        }
    }

    public double perimeter(){
        double sum = 0;
        for (double side : this.sides) {
            sum += side;
        }
        return sum;
    }

    @Override
    public String toString() {
        return super.toString() +
                ", " + "Стороны: " + sides +
                ", " + "Периметр: " + this.perimeter();
    }
}
