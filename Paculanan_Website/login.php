<!doctype html>
<html lang="en">
<head>
    <title>Website ni Paculanan - Login</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="design.css">
    <?php include('header.php'); ?>
    <?php include('nav.php'); ?>
</head>
<body>
<div id="container">

    <div id="content">
        <h3>Login</h3>
        <?php
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            require('mysqli_connect.php');

            // Validate email input
            if (!empty($_POST['email'])) {
                $e = mysqli_real_escape_string($dbcon, $_POST['email']);
            } else {
                echo '<p class="error">Please enter your email address.</p>';
                $e = NULL;
            }

            // Validate password input
            if (!empty($_POST['psword'])) {
                $p = $_POST['psword']; // Don't hash the password here
            } else {
                echo '<p class="error">Please enter your password.</p>';
                $p = NULL;
            }

            // Proceed if both email and password are provided
            if ($e && $p) {
                // Query the database to check for the email and retrieve the user data
                $q = "SELECT user_id, fname, user_level, psword FROM users WHERE email = '$e'";
                $result = mysqli_query($dbcon, $q);

                if (mysqli_num_rows($result) == 1) {
                    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);

                    // Verify the password using password_verify() function
                    if (password_verify($p, $row['psword'])) {
                        session_start();
                        $_SESSION = $row;
                        $_SESSION['user_level'] = (int)$_SESSION['user_level'];

                        // Redirect based on user level
                        $url = ($_SESSION['user_level'] === 1) ? 'admin.php' : 'members_page.php';
                        header('Location: ' . $url);
                        exit();
                    } else {
                        echo '<p class="error">Invalid email or password. Please try again.</p>';
                    }
                } else {
                    echo '<p class="error">Invalid email or password. Please try again.</p>';
                }

                mysqli_free_result($result);
            } else {
                echo '<p class="error">Please enter both email and password.</p>';
            }

            mysqli_close($dbcon);
        }
        ?>

        <!-- Simple login form -->
        <form action="login.php" method="post">
            <p><label for="email">Email Address:</label>
                <input type="text" name="email" size="30" maxlength="50" value="<?php if (isset($_POST['email'])) echo $_POST['email']; ?>"></p>
            <p><label for="psword">Password:</label>
                <input type="password" name="psword" size="20" maxlength="20"></p>
            <div class="button-container">
                <input type="submit" name="submit" value="Login">
            </div>
        </form>
    </div>
</div>
<?php include('side-bar.php'); ?>
<?php include('footer.php'); ?>
</body>
</html>