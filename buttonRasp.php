<?php
$path = "data.json";
$file = fopen($path, "w+");
$json = json_encode($_POST, JSON_NUMERIC_CHECK);
fwrite($file, $json);
fclose($file);
echo "ok";
?>