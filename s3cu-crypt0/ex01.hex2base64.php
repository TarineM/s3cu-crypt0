<?php 

/**
 * H means that the format of the data is hexa (H),
 * * means that compact each letter until the end of the data
 */
function hex_to_base64($hex)
{
  return base64_encode(pack('H*',$hex));
}


$test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

$test = hex_to_base64($test);

echo $test;
?>