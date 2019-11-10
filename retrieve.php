<html>
<head><title>Results</title></head>
<link rel="stylesheet" href="hacknjit2.css"/>
<body>
<header>
<img id="logo" src="logo.png">
</header>

<div>
	<ul>
	<?php
		$city = "{$_POST['city']}";
		$output = shell_exec("python3 findcity.py " . "'" . $city . "'");
		echo $output;
		if (strlen($output) == 0){
			echo "<p>There are no results</p>";
		}
	?>
	</ul>
</div>
</body>
</html>
