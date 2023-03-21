WALL-E Unity3d Game with AI
===========================

WALL-E is a Unity3d game developed to promote waste management and sustainability. The game features an AI robot, WALL-E, that helps manage garbage in a world where waste has overtaken the planet. The objective of the game is to gather information about waste in the surrounding area, identify sources of waste, develop a waste management plan, implement the plan, monitor progress, make adjustments, deal with unexpected challenges, and achieve successful waste management.

The game is built using Unity3d and features an API developed using Flask that can be used to train an AI model with the data collected during gameplay. The environment of the game is editable and can be customized according to the user's needs.

Installation
------------

To run the API, you will need to install the following dependencies:

-   Python 3.6 or higher
-   Flask
-   NumPy

You can install these dependencies by running the following command:

bashCopy code

`pip install -r API/requirements.txt`

Usage
-----

To use the API, follow these steps:

1.  Start the API by running the following command in the `API` folder:

    bashCopy code

    `python walleaiapi.py`

2.  Launch the WALL-E Unity3d game.

3.  Play the game and collect data.

4.  Use the API to train an AI model with the collected data.

    bashCopy code

    `# Example command to train the model
    curl -X POST -H "Content-Type: application/json" -d @WALL-E_Data/data.json http://localhost:5000/train`

    Note: You will need to replace `WALL-E_Data/data.json` with the path to the data file that you collected during gameplay.

5.  Use the trained AI model to predict and improve waste management in the game.
