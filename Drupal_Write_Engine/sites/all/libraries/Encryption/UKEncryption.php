<?php

class UKEncryption
{
    //PHP
    //Resources on encryption
    //http://stackoverflow.com/questions/5244129/use-rsa-private-key-to-generate-public-key
    //https://rietta.com/blog/2012/01/27/openssl-generating-rsa-key-from-command/

    public $pubkey = '';
    private $fp = '';
    public $privkey = '';

    public function encrypt($data)
    {
        $this->fp = fopen("/var/www/html/drupal-7-uk/sites/all/libraries/Encryption/keys/key.pub", "r");
        $this->pubkey = fread($this->fp, 8192); 
        fclose($this->fp);

        if (openssl_public_encrypt($data, $encrypted, $this->pubkey))
            $data = base64_encode($encrypted);  
        else
            throw new Exception('Unable to encrypt data. Perhaps it is bigger than the key size?');

        return $data;
    }

    public function decrypt($data)
    {

        $this->fp = fopen("/var/www/html/drupal-7-uk/sites/all/libraries/Encryption/keys/private.pem", "r");
        $this->privkey = fread($this->fp, 8192); 
        fclose($this->fp);

        if (openssl_private_decrypt(base64_decode($data), $decrypted, $this->privkey))
            $data = $decrypted;
        else
            $data = '';

        return $data;
    }
}