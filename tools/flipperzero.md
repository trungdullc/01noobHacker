# Flipper Zero

```
Description: cybersecurity tool to explore access control system, NFC, RFID, infrared, radio protocols, and debug hardware using GPIO pins
Bought: $ 120

Can be replicated w/ Arduino or Raspberry Pi

Hacker Contests:
   https://defcon.org/?mob=1
```
# Step 1: Update Firmware
```
32-64gb microSD card base 10

Update Method:                                      https://flipperzero.one/downloads
    iPhone w/ Bluetooth         or                  PC w/ usb cable
       Flipper Mobile App                               DL qFlipper
          Pair with smartphone
    Flipper: Setting > Bluetooth > ON               Setting > Development > UPDATE

    UPDATE                                          Exit qFlipper
                                                    DL: Unoffical custom firmware
    App (To download extra offical Apps)            https://momentum-fw.dev/
                                                    Install
                                                    Select Firmware Channel > Dev

                                                    From Desktop:
                                                    https://github.com/skizzophrenic/Ubers-SD-Files
                                                    git clone https://github.com/skizzophrenic/Ubers-SD-Files.git

                                                    From SD card connected to adapter (faster transfer)
                                                    Copy to current folder
```

# Feature: Apps
```
Uses: Flash Wifi Developer Board

How to Use:
   GPIO
      ESP (put ESP board in sockets)
      (ESP) ESP Flasher
         Quick Flash
            Flipper Wifi Dev Board
               Maurauder (has Evil Portal)
```

<img src="https://images.archbee.com/3StCFqarJkJQZV-7N79yY/iWJNVsM0quT9-4IdFRVEq_monosnap-miro-2023-07-14-13-19-38.jpg?format=webp&width=1280">

# Feature: Sub-gigahertz transceiver
```
Documentation: https://docs.flipper.net/zero/sub-ghz
Uses: Gas Station Prices, Locks/Gates, Walgreens Customer Service, open car door, garage door, wireless alarm systems (RING),  89 sub-GHz radio protocols (walkie-talkies)
CC1101 transceiver: $ 5-10 on Amazon/Ebay

Fix: Rolling code system: Key Hash + Counter generated each action vs same password
Tip: Don't mess with car keys or original not work

Bypass: HackRF One from Great Scott Gadgets is a Software Defined Radio peripheral capable of transmission or reception of radio signals from 1 MHz to 6 GHz. Can be used to beat rolling code system

How to use:
   Read Raw                     Send
      Stop
      Save
```

# Feature: Low-Frequency RFID (Radio Frequency Identification)
```
Documentation: https://docs.flipper.net/zero/rfid
Uses: plastic cards, apartment access cards, key fobs, copy tags, wristbands, and animal microchips (raw data to find owner)
Note: Passport RFID is encrypted
   Key is passport number (9 alphanumeric char), date of birth, expiry date of passport
125 kHz and 13.56 MHz

Fix: add encryption to keys and RFID blocking sleeves
App: https://awesome-flipper.com/application/lab.flipper.net/tools/nfc_rfid_detector/
```

<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Data_Networks_classification_by_spatial_scope.svg/330px-Data_Networks_classification_by_spatial_scope.svg.png" width="200" height="200"></center>

# Feature: NFC (Near-Field Communications)
```
Documentation: https://docs.flipper.net/zero/nfc
Uses: public transport smart cards, access cards or tags, NTAG215 NFC Blank Cards, digital business cards, tap to pay credit cards (need card holder, zip code, CVV), subway transit cards (UID only), nintendo switch emulate Amiibo code, bad usb like Hak5 Rubber Ducky(keyboard)

Rubber Ducky Payloads: https://github.com/hak5/usbrubberducky-payloads

Flipper Zero controlled remotely(phone/pc/steam deck): https://github.com/flipperdevices/qFlipper

App: https://github.com/jaylikesbunda/Flipper-NFC-Maker

How to Use:
   Read
```

# Feature: IR (Infrared)
```
Documentation: https://docs.flipper.net/zero/infrared
GitHub: https://github.com/Lucaslhm/Flipper-IRDB
Uses: remote controls, AC

App: https://github.com/kala13x/flipper-xremote

How to Use:
   Universal Remote
      TV
   Learn New Remotes
```

# Feature: GPIO (General-purpose input/output)
```
Documentation: https://docs.flipper.net/zero/gpio-and-modules
Dev Board: https://developer.flipper.net/flipperzero/doxygen/dev_board.html
Uses: logitech 2.4 gigahertz RF signal
replaces ST-Link Debugger
```

# Feature: Bluetooth
```
Uses: sniff bluetooth traffic
```

# Feature: Wifi
```
Uses: test security of wifi network
Wifi packet scanner

FindMyFlipper: https://github.com/MatthewKuKanich/FindMyFlipper
App: https://github.com/justcallmekoko/ESP32Marauder/wiki/flipper-zero
```

# Feature: RF
```
Uses: RF jamming

Disable connect with weaponized drones or robots (military)
Disable RF communications (medical)
```

# Feature: Barcode
```
Uses: Supermarket

App: https://github.com/Kingal1337/flipper-barcode-generator
```

# Feature: USB
```
Uses: Delivery Payloads, Bootable Image

App: https://github.com/ThatGamerBlue/flipper-zero-mass-storage
```

# Feature: Math
```
Uses: Converter (faster on computer)

App: https://awesome-flipper.com/application/lab.flipper.net/tools/multi_converter/
App: https://github.com/shalebridge/flipper-resistor-calculator
```

# Feature: JS Script
```
Documentation: https://developer.flipper.net/flipperzero/doxygen/js.html

Save .js script to SD Card/apps/Scripts
// Example script to toggle an LED
if (doesSdkSupport(["gpio"])) {
let ledPin = 13;                        // Define the GPIO pin for the LED
gpio.setMode(ledPin, gpio.OUTPUT);      // Set the pin mode to output

// Function to toggle the LED
function toggleLED() {
let state = gpio.read(ledPin);
gpio.write(ledPin, !state);
console.log("LED state: " + !state);
}

// Toggle the LED every second
setInterval(toggleLED, 1000);
} else {
console.log("GPIO not supported on this firmware.");
}

How to use:                                     // Note: Support for JS features depending on firmware
    Main Menu > Apps > Scripts                  // Momentum, Unleashed, RogueMaster
    Select .js file

// Hello.js (Another Example)                               // shorter version
let widget = require("widget");                             // print("Hello Hackers");

// Add text to display
widget.addText(10, 10, "Primary", "Hello Hackers");         // coordinates
// Show widget
widget.show();
delay(5000);
```

# Feature: Python Script
```
GitHub:
   https://github.com/0d1nss0n/Python_on_Flipper_Zero
   https://ofabel.github.io/mp-flipper/
```

# Features: Others
```
Geiger counter is an electronic instrument for detecting and measuring ionizing radiation
Light Meters
Sonar Detectors

scripts vs Plugins:
    scripts: temporary code to run
    Plugin: perm changes to Flipper Zero

GitHubs:
   https://github.com/djsime1/awesome-flipperzero
   https://github.com/w0lfzk1n/Flipper-Zero-NFC-Trolls

Youtube:
   https://www.youtube.com/playlist?list=PLM1cyTMe-PYJaMQ6TWeK1mAWxORdjYJZ5
```

## Back to README.md
[BACK](../README.md)