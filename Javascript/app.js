// app.js
import MathOperations from "./MathOperations.js"; // Ensure this file exists in the same directory

// Create an instance
const math = new MathOperations();

// Get the result
const sumResult = `Sum: ${math.add(5, 3)}`;
const diffResult = `Difference: ${math.subtract(9, 4)}`;

// Display on the webpage
document.getElementById("output").innerHTML = `<p>${sumResult}</p><p>${diffResult}</p>`;
