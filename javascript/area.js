// Area of tringle, circle, square & rectangle

class Area {
  // Triangle
  triangle(base, height) {
    return 0.5 * base * height;
  }

  // Circle
  circle(radius) {
    // Todo: Write a function to reaturn the area of a circle

    return radius * Math.PI.toFixed(3);
  }

  // Square
  square(side) {
    // Todo: Write a function to reaturn the area of a square

    return side * side;

  }

  // Rectangle
  rectangle(length, breadth) {
    // Todo: Write a function to reaturn the area of a circle
    return length * breadth;

  }
}

var tr_area = new Area().triangle(3, 5);
console.log(`Area of triangle: ${tr_area}`);

var cr_area = new Area().circle(5);
console.log(`Area of circle: ${cr_area}`);

var sq_area = new Area().square(5);
console.log(`Area of square: ${sq_area}`);

var rc_area = new Area().rectangle(3, 5);
console.log(`Area of rectangle: ${rc_area}`);
