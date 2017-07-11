# How to run

## Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system.

## Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

## VM configuration
Unzip the `fsnd-virtual-machine.zip` file 
Change to this directory in your terminal with cd. Inside, you will find another directory called `vagrant`. Change directory to the `vagrant` directory and run `vagrant up` command:

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

## Database file
You will need to unzip this file `newsdata.sql.zip`  The file inside is called `newsdata.sql`. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, use the command `psql -d news -f newsdata.sql`.

## myApp.py file
Now put your `myApp.py` file also in `vagrant` folder

##Run the program
Now run the program by `python myApp.py` to see the out put in ternminal

when you are running this command you need to complete all the steps described above and you sould be using virtual machine
