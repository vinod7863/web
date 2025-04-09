<?php
// Get the requested route
$route = isset($_GET['route']) ? $_GET['route'] : '/';

// Define routes
$routes = [
    '/' => 'home',
    'about' => 'about',
    'contact' => 'contact',
];

// Check if the route exists
if (array_key_exists($route, $routes)) {
    call_user_func($routes[$route]); // Call the function dynamically
} else {
    echo "404 - Page not found";
}

// Controller functions
function home() {
    echo "<h1>Welcome to Home Page</h1>";
}

function about() {
    echo "<h1>About Us</h1>";
}

function contact() {
    echo "<h1>Contact Us</h1>";
}
?>
