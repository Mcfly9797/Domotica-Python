<?php
$path = "data.json";
if (!file_exists($path))
    exit("File not found");
$data = file_get_contents($path);
echo $data;
?>