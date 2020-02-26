# Push

#### NOTICE:

If you have duplicate nodes after an upgrade, delete all of the nodes except the Controller node then restart the nodeserver. Don't delete anything from the config page. Restart the nodeserver.

Using your Pushover account you can send notifications from a program without needing a network resource.

This great for sending short pre-programed messages about your things, like doors, windows, leaks, alarms, lights, motion, low batteries, etc, etc.

![Pushpic](https://github.com/markv58/github.io/blob/master/Pushpic.png)

![DBpic](https://github.com/markv58/github.io/blob/master/DBpic.png)

![PushConf](https://github.com/markv58/github.io/blob/master/PushConfigHelp.png)

#### Installation

Backup your ISY before installation please.

Install from the NodeServer Store.

Manual:

    cd .polyglot/nodeservers
    git clone https://github.com/markv58/UDI-Push.git
    cd UDI-Push
    chmod +x install.sh
    ./install.sh



Add Push to a node slot.

Restart the Admin Console.

Enter your <user_key> and <api_key> from your Pushover account in the custom configuration parameters. Enter the things and
you are ready to send notifications from your programs.

v1.0.2 Fixed blank message, added new messages.

v1.0.3 Fixed install to Polyglot Cloud

v1.0.4 Fixed bug that caused ghost nodes under certain circumstances.
