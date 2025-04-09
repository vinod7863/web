<?php
if (isset($_GET['name']) && isset($_GET['age'])) {
    $name = $_GET['name']; 
    $age = $_GET['age'];

    echo "<h2>Received Data:</h2>";
    echo "Name: " . $name . "<br>";
    echo "Age: " . $age . "<br>";
} else {
    echo "No data received.";
}
?>
<br>
<a href="index.php">Go Back</a>
