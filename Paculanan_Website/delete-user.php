<!DOCTYPE html>
<html lang="en">
<head>
    <title>Website ni Paculanan - Delete</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="design.css">
    <?php include('header.php'); ?>
    <?php include('navdel.php'); ?>
</head>
<body>
    <div id="container">

        <div id="content">
            <h3>Deleting Records</h3>
            <?php
            // Check if a valid user_id is provided in the URL
            if (isset($_GET['user_id']) && is_numeric($_GET['user_id'])) {
                $id = $_GET['user_id'];
            } elseif (isset($_POST['user_id']) && is_numeric($_POST['user_id'])) {
                $id = $_POST['user_id'];
            } else {
                echo '<p class="error">This page has been accessed by mistake.</p>';
                include('footer.php');
                exit();
            }

            // Debugging - check if the id is being passed correctly
            // echo "User ID: " . $id; // Uncomment this line to debug

            require('mysqli_connect.php');

            // Handle the form submission
            if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                if (isset($_POST['sure']) && $_POST['sure'] == 'Yes') {
                    // Prepared statement to delete the user
                    $q = "DELETE FROM users WHERE user_id = ? LIMIT 1";
                    $stmt = mysqli_prepare($dbcon, $q);

                    // Bind the user_id parameter and execute the query
                    mysqli_stmt_bind_param($stmt, 'i', $id);
                    $result = mysqli_stmt_execute($stmt);

                    if ($result && mysqli_stmt_affected_rows($stmt) == 1) {
                        echo '<h4>The record has been deleted.</h3>';
                    } else {
                        echo '<h3 class="error">The record could not be deleted. Please try again.</h3>';
                    }

                    mysqli_stmt_close($stmt);
                } else {
                    echo '<h4>Record deletion canceled.</h3>';
                }
            } else {
                // Display the confirmation form
                $q = "SELECT CONCAT(fname, ' ', lname) FROM users WHERE user_id = ?";
                $stmt = mysqli_prepare($dbcon, $q);

                // Bind the user_id parameter and execute the query
                mysqli_stmt_bind_param($stmt, 'i', $id);
                mysqli_stmt_execute($stmt);
                mysqli_stmt_bind_result($stmt, $fullName);

                // Fetch and check the result
                if (mysqli_stmt_fetch($stmt)) {
                    echo "<h4>Are you sure you want to permanently delete $fullName?</h3>";
                    echo '
                        <form action="delete-user.php" method="post">
                            <div class="button-container">
                                <input id="submit-yes" type="submit" name="sure" value="Yes">
                                <input id="submit-no" type="submit" name="sure" value="No">
                            </div>
                            <input type="hidden" name="user_id" value="' . $id . '">
                        </form>
                    ';
                } else {
                    echo '<p class="error">No such user found.</p>';
                }

                mysqli_stmt_close($stmt);
            }

            mysqli_close($dbcon);
            ?>
        </div>
    </div>
    <?php include('side-bar.php'); ?>
	<?php include('footer.php'); ?>
</body>
</html>