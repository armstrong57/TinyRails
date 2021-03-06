# TinyRails

## Constant Values
    Resource demands and all upgrade costs according to station size.

## Startup
On startup, load the files with all station and cargo data. Save all this data in the program.

***TODO***: Would stations be better represented as class objects? Likely easier to access fields, but how to effectively store?

Stations are stored as a dictionary in the following fashion:

-   **key** = station name, string. When multiple stations have the same name, the second station has the region name appended.
   ***TODO***: In this case, how to determine which is the correct station when accessing later?
-   **value** = class object 
Cargo is also stored as a dictionary with key = resource, value = tuple: (train, depot, demand), all ints

## Menu
Once all data is loaded, the menu window is loaded. Menu options are as follows:
-    *All Stations*: All locked, completed, and in-progress stations.
-    *Current Stations*: In-progress stations, whether due to remaining market demand or upgrades.
-    *Locked Stations*: Stations in locked regions OR stations in current regions that need to be built
-    *Completed Stations*: Stations with completed market demands AND fully upgraded
-    *Cargo*: Cargo on train and in depot, and market demand remaining

Each option opens a new window with the corresponding information.

## Finish
On finish, want to write all current data to the files loaded at startup to avoid having to redo all progress.
