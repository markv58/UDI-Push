# Push

Using your Pushover account you can send notifications from a program without needing a network resource.

This great for sending short pre-programed messages about your things, like doors, windows, leaks, alarms, lights, motion, low batteries, etc, etc.

#### Installation

Backup your ISY before installation please.

Manual:

    cd .polyglot/nodeservers
    git clone https://github.com/markv58/UDI-Push.git
    cd UDI-Push
    chmod +x install.sh
    ./install.sh

Install from the NodeServer Store.

Add Push to a node slot.

Restart the Admin Console.

Enter your <user_key> and <api_key> from your Pushover account in the custom configuration parameters. Enter the things and
you are ready to send notifications.

