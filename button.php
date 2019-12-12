<?php
$path = "data.json";
$file = fopen($path, "w+");
$archivo = file_get_contents($path);
$json = json_decode($archivo, True);
switch(True)
{
    case isset($_POST['enchufe1on']):
      $json["rele1"] = 1;
    break;
    case isset($_POST['enchufe1off']):
      $json["rele1"] = 0;
    break;
}
$json = json_encode($json, JSON_NUMERIC_CHECK);
fwrite($file, $json);
fclose($file);
header("location: URL DE MI PAGINA WEB");
?>