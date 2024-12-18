<?php
	session_start();
	//kung may sess id at kung admin siya 
	if (!isset(($_SESSION['user_level'])) or ($_SESSION['user_level'] != 0)){
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
		<?php include('nav_members.php');?>
	</head>
	<body>
		<div id="container">
			
			<div id='content'>
				<h2>Our Members</h2>
				<img id="image3" S src = "cat1.jpg">
				<img id="image3" S src = "cat2.png">
				<img id="image3" S src = "cat3.png">
				<img id="image3" S src = "cat4.png">
				<img id="image3" S src = "cat5.png">

			</div>
			
		</div>
		<?php include('side-bar.php'); ?>
		<?php include('footer.php'); ?>
	</body>
	</html>