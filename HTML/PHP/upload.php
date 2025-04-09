<?php
if (isset($_POST["submit"])) {
    $targetDir = "uploads/"; // Directory where files will be saved
    if (!is_dir($targetDir)) {
        mkdir($targetDir, 0777, true); // Create directory if not exists
    }

    $fileName = basename($_FILES["file"]["name"]);
    $targetFilePath = $targetDir . $fileName;
    $fileType = strtolower(pathinfo($targetFilePath, PATHINFO_EXTENSION));

    // Allowed file types
    $allowedTypes = array("jpg", "jpeg", "png", "gif", "pdf", "docx");

    if (in_array($fileType, $allowedTypes)) {
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFilePath)) {
            echo "The file <b>" . htmlspecialchars($fileName) . "</b> has been uploaded successfully.";
        } else {
            echo "Error uploading the file.";
        }
    } else {
        echo "Only JPG, PNG, GIF, PDF, and DOCX files are allowed.";
    }
} else {
    echo "No file uploaded.";
}
?>
