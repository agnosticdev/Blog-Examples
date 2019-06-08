package com.example.io2019security;

import android.app.Application;
import android.content.SharedPreferences;
import android.content.Context;
import java.util.Set;
import java.util.HashSet;
import java.io.File;
import java.io.FileInputStream;
import androidx.security.crypto.EncryptedFile;
import androidx.security.crypto.MasterKeys;

// Normally this file would be in a private package, but for sake of example this is just a Java class.
public class FileEncryption {

    private Context context;

    public FileEncryption(Context context) {
        context = context;
    }


    private void fileEncryptionRoutine() {
        // Create your actual private keys for file encryption/decryption.
        Set<String> key_set = new HashSet<String>();
        key_set.add("stringbasedencryptionkeyone");
        key_set.add("stringbasedencryptionkeytwo");

        String keySetReference = "secret_file_keys";

        // Store them in the shared pr
        SharedPreferences sharedPref = context.getSharedPreferences("com.private.context",
                context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPref.edit();
        editor.putStringSet(keySetReference, key_set);
        editor.commit();

        try {

            // Get a reference to the master keys
            String masterKeyAlias = MasterKeys.getOrCreate(MasterKeys.AES256_GCM_SPEC);

            // File to decrypt and read off disk
            String fileReference = "routing_numbers.txt";
            String stringBasedOutputStream;
            File secret_file = new File(context.getFilesDir(), fileReference);

            // Generate the encrypted file object with many constructor paramters:
            // 1) The secret file reference.
            // 2) The current application context.
            // 3) A master key alias for decrypting your keyset in the SharedPreferences.
            // 4) The FileEncryptionScheme (AES256_GCM_HKDF_4KB)
            // Note) The setKeysetAlias chained method call on the constructor call.
            //       This will set the SharedPreference key to the encryption keys in the SharedPreferences.
            EncryptedFile encrypted_file = new EncryptedFile.Builder(
                    secret_file,
                    context,
                    masterKeyAlias,
                    EncryptedFile.FileEncryptionScheme.AES256_GCM_HKDF_4KB
            ).setKeysetAlias(keySetReference)
                    .build();

            FileInputStream encryptedInputStream = encrypted_file.openFileInput();
            try {

                int buffer = encryptedInputStream.read();
                stringBasedOutputStream = "";
                while (buffer != -1) {
                    char charVal = (char)buffer;
                    stringBasedOutputStream += charVal;
                    buffer = encryptedInputStream.read();
                }
                // do something with the decrypted file (stringBasedOutputStream) here.
                // clean up all encrypted values held in memory right after to prevent security leak.

            } catch (Exception e) {
                // Handle Exception Here
                // Clear out:
                //   *encryptedInputStream
                //   *stringBasedOutputStream
                //   *encrypted_file
                //   to prevent security leakage.
            } finally {
                encryptedInputStream.close();
            }


        } catch (Exception e) {
            // Handle Exception Here
        }
    }
}
