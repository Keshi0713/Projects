<?php
	session_start();
	//kung may sess id at kung admin siya 
	if (!isset(($_SESSION['user_level'])) or ($_SESSION['user_level'] != 1)){
		header("Location: login.php");
		exit();
	}
?>
<!doctype html!>
	<html lang="en">
	<head>
		<title>Website ni Paculanan</title>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="design.css">
		<?php include('header.php');?>
		<?php include('nav-admin.php');?>
	</head>
	<body>
		<div id="container">
			<div id='content'>
				<h2>Your Monthly Statistics</h2>
				<img id = "image1" src = "cat-dashboard.png">
			</div>
			
		</div>
		<?php include('side-bar.php'); ?>
		<?php include('footer.php'); ?>
	</body>
	</html>