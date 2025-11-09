# Astrophysical app and MCP server

This app relies on [ssd.jpl.nasa.gov](https://ssd.jpl.nasa.gov/) api to get the latest ephemerides of astrophysical bodies.

## App

The app consist of an OpenAI app that can answer questions about the position of astrophysical bodies.

## MCP server

The MCP server is responsible for fetching the latest ephemerides from [ssd.jpl.nasa.gov](https://ssd.jpl.nasa.gov/) and serving them to the app.

### Example

Below is an example of a curl command to get the ephemerides of Voyager 1 for the date 2025-11-08 to 2025-11-09:

`curl "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&EPHEM_TYPE=OBSERVER&CENTER=g@399&START_TIME=2025-11-08&STOP_TIME=2025-11-09&STEP_SIZE=1d&COMMAND=-31"`

`EPHEM_TYPE=OBSERVER` indicates that we want the ephemerides as seen from a specific location.

`CENTER=g@399` corresponds to the geocenter (Earth).

`START_TIME` and `STOP_TIME` define the time range for the ephemerides.

`STEP_SIZE=1d` indicates that we want the ephemerides at 1 day intervals.

`COMMAND=-31` is the code for Voyager 1.
