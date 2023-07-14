<?php
    $comment = $_POST['comment'];

    // ouvrir un fichier
    $fichier = fopen('comment.txt' ,'w');

    // écrire le commentaire dans le fichier
    fwrite($fichier, $comment);
    fclose($fichier);

    $command = escapeshellcmd('python3 prediction.pkl');
    $output = shell_exec($command);

    echo "Le commentaire que vous avez entré est ". $output. ".";
?>