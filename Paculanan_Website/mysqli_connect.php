<?php
$dbcon = @mysqli_connect('localhost', 'Paculanan', 'paculanan', 'members_paculanan') #(server, username, psword, db name)
OR die('Could not connect to my SQL Server'. mysqli_connect_error());
mysqli_set_charset($dbcon, 'utf8');
?>