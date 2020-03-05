<?php

/** */
function exo2($s1, $s2)
{
    return bin2hex(pack('H*',$s1) ^ pack('H*',$s2));
}

$s1 = "1c0111001f010100061a024b53535009181c";

$s2 = "686974207468652062756c6c277320657965";

echo exo2($s1, $s2);


?>