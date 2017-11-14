# Common Business Entities (CBE)

[![Licence](https://img.shields.io/github/license/semprini/cbe.svg)](https://github.com/Semprini/cbe/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/semprini%2Fcbe.svg)](https://badge.fury.io/gh/semprini%2Fcbe)
[![Build Status](https://img.shields.io/circleci/project/github/Semprini/cbe.svg)](https://circleci.com/gh/Semprini/cbe)
[![Coverage Status](https://coveralls.io/repos/github/Semprini/cbe/badge.svg?branch=master)](https://coveralls.io/github/Semprini/cbe?branch=master)
[![cdaf version](automation/badge.png)](http://cdaf.io)

The CBE projects goal is to provide practical data governance via a generic schema/API/persistence layer which can be used for all the common functions in an enterprise and extended for each industry/business. CBE can be used to underpin micro-service, SOA, EDA or MDM architecture. In the same area as SAP MDG, CBE provides domain-specific master data governance to centrally create, change and distribute or to consolidate master data across your complete enterprise system landscape.

CBE provides RESTful CRUD and administration for common business entities persisted on relational DBs and (coming soon) NoSQL DBs. This polyglot persistence model forms the backbone of an organisations master data governance. The rationale is discussed in the [Wiki](https://github.com/Semprini/cbe/wiki). 

Industry Specific Extension Projects
 - [Retail](https://github.com/Semprini/cbe-retail)
 - [Utilities (Telco/Energy/Media)](https://github.com/Semprini/cbe-utilities)
 - [Sport](https://github.com/Semprini/cbe-sport)

Sources: TM Fourum SID (Telco), IBM IFW (Finance/Banking), IAA (Insurance)

## To run

```shell
git clone https://github.com/Semprini/cbe.git
cd cbe
pip install -r requirements.txt
python manage.py migrate (will use a default sqllite db)
python manage.py createsuperuser <username> <email> <password>
python manage.py runserver
browse to http://localhost:8000/admin for the admin interface
browse to http://localhost:8000/api for the api interface
```

# How is this different to an API from a product?

It is the role of CBE to express relationships and provide consistent schema for use in multiple contexts. A product will rightly store data for it's own purpose and expose it's data through product oriented APIs, we then use integration architectures like SOA to expose and adjust the semantics for different contexts. 
The CBE persistence layer provides a loosely coupled and practical realization of the data model rather than through a transformation layer. This greatly reduces the impact of product version changes and speeds new feature delivery.

Entity Domains:
- Party - Entities relating to individuals, organizations, how to contact them and the roles they play
- Location - Entities for addresses and places
- Business interaction - Entities for how parties interact in the business
- Customer - The parties that a business sells products or services to
- Trouble - Tracking problems and issues

Coming soon to a data model near you:
- More roles for PartyRole and BusinessInteraction
- Product


The data model is designed to be extended for each industry. In Party, the PartyRole class is the main abstract entity from which concrete classes like Customer or Supplier should be derived.

Check the [Wiki](https://github.com/Semprini/cbe/wiki) for more info. The data model is held in the Docs folder as a Sparx EA model

# Virtual Desktop Environment

To use a virtual environment requires VirtualBox and Vagrant, from the workspace run:

    vagrant up

If you have Docker for Windows installed, swaitch to Windows Containers and run delivery emulation:

    ./automation/cdEmulate.bat

Note: If Docker is not available, the emulation will fall back to using native Python on the host

## Direct PowerShell Access

To access the buildserver using native remote PowerShell.
Allow credential delegation, one-off step needed on the host when using VirtualBox/Vagrant. 

    ./automation/provisioning/runner.bat CredSSP.ps1 client

Once delegation configured, the build emulation can be executed.

    $securePassword = ConvertTo-SecureString 'vagrant' -asplaintext -force
    $cred = New-Object System.Management.Automation.PSCredential ('vagrant', $securePassword)
    enter-pssession 127.0.0.1 -port 15985 -Auth CredSSP -credential $cred
    cd C:\vagrant
	.\automation\cdEmulate.bat

# Make your own fork

    git clone https://github.com/cdaf/cbe.git
    cd cbe
    git remote add upstream https://github.com/Semprini/cbe.git

Once established, use the following to synchronise

    git fetch upstream
    git pull upstream master
