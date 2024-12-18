<!DOCTYPE html>
<html lang="en">
<head>
    <title>Website ni Paculanan - REG</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="design.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
    <?php include('header.php'); ?>
    <?php include('navadmin_view.php'); ?>
</head>
<body>
    <div id="container">
        <div id='content'>
            <main class="content-view">
            <h2>Registerd Users</h2>
            <p>
                <?php
                    // connect sa database
                    require("mysqli_connect.php");
                    // query to get db
                    $q = "SELECT user_id, fname, lname, email, psword, DATE_FORMAT(registration_date, 
                    '%M %d, %Y') AS regdat from users 
                    ORDER BY user_id ASC";
                    $result = @mysqli_query($dbcon, $q);
                    // if query is successful //edit[51] //delete[52]
                    if ($result) {
                        echo '<table><tr>
                            <td><strong>Full name </strong></td>
                            <td><strong> Email </strong></td>
                            <td><strong>Registered Date </strong></td>
                            <td colspan="2"><strong>Actions </strong></td>
                            </tr>';
                              while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                                echo '<tr>
                                <td>'.$row['fname'].' '.$row['lname'].'</td>
                                <td>'.$row['email'].'</td>
                                <td>'.$row['regdat'].'</td>
                                <td><a href="edit-user.php?user_id='.$row['user_id'].'"><i class="fa-solid fa-pencil"></i></a></td>            
                                <td><a href="delete-user.php?user_id='.$row['user_id'].'"><i class="fa-solid fa-trash-can"></i></i></a></td> 
                                </tr>';

                            }
                            echo '</table>';
                            mysqli_free_result($result);

                    } else {
                        echo '<h2>System Error</h2>
                            <p class="error">The current users could not be retrieved. Contact the system administration</p>'; 
                            echo '<p>' . mysqli_error($dbcon) . '</p>'; // Display the MySQL error.
                        }
                
                        mysqli_close($dbcon) 
                ?>
            </p>
            </main>
        </div>
    </div>
    <?php include('side-bar.php'); ?>
    <?php include('footer.php'); ?>
</body>
</html>
