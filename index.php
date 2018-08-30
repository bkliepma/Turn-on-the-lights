<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8" />
        <title>Bedroom Lights</title>
    </head>
    
	<body>
	<a href="/cgi-bin/on.py">On</a> <br>
	<a href="cgi-bin/off.py">Off</a> <br>
    	<a href="/cgi-bin/Sunrise.py">Sunrise</a> <br>
	<a href="cgi-bin/Sunset.py">Sunset</a> <br>
    	<a href="/cgi-bin/reset.py">Reset</a> <br>
	<a href="cgi-bin/pause.py">Pause</a> <br>
	#https://stackoverflow.com/questions/39671105/have-link-appear-only-if-href-file-exists
	<?php
	echo '<ul>';
	$pausefile = 'PauseFile.txt';
                if (file_exists($pausefile)) {
                $file_clean = explode('.', $pausefile);
                $file_clean = str_replace('-', ' ', $pausefile_clean[0]);
                $file_clean = ucfirst($file_clean);
                echo '<li><a class="button" href="' . $pausefile . '">' . $file_clean . '</a></li>';
                }
            }
	echo '</ul>';
	?>
	</body>
</html>

