# Push

Using your Pushover account you can send notifications from a program without needing a network resource.

#### Installation

Backup your ISY before installation please.

Manual:

    cd .polyglot/nodeservers
    git clone https://github.com/markv58/UDI-Push.git
    cd UDI-Push
    chmod +x install.sh
    ./install.sh

Add Push to a node slot.

Restart the Admin Console.

Enter your <user_key> and <api_key> from your Pushover account in the custom configuration parameters. Enter the things and
you are ready to send notifications.

