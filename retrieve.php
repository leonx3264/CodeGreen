<html>
<head><title>Results</title></head>
<link rel="stylesheet" href="hacknjit2.css"/>
<body>
<header>
<img id="logo" src="logo.png">
</header>
<a id="homebutton" href="https://site.codegreen.space">Home</a>
<div>
	<ul>
	<?php
		$city = "{$_POST['city']}";
		$output = shell_exec("python3 findcity.py " . "'" . $city . "'");
		echo $output;
		if (strlen($output) == 0){
			echo "<li><h3>Oops</h3><p>There are no results..</p></li>";
		}
	?>
	</ul>
</div>
</body>
</html>
