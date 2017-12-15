Title: Leaflet for R 
Date: 2017-04-08 10:00
Category: R, Leaflet
Tags: Data Visualization, R
Slug: RLeaflet 
Author: Mohcine madkour
Illustration: background.jpg

#Introduction 
Leaflet is one of the most popular open-source JavaScript libraries for interactive maps. It’s used by websites ranging from The New York Times and The Washington Post to GitHub and Flickr, as well as GIS specialists like OpenStreetMap, Mapbox, and CartoDB.
This R package makes it easy to integrate and control Leaflet maps in R.

This R package makes it easy to integrate and control Leaflet maps in R.

#Installation

To install this R package, run this command at your R prompt:

    install.packages("leaflet")
    # to install the development version from Github, run
    # devtools::install_github("rstudio/leaflet")

Basic Usage

You create a Leaflet map with these basic steps:

1- Create a map widget by calling leaflet().
2- Add layers (i.e., features) to the map by using layer functions (e.g.  addTiles, addMarkers, addPolygons) to modify the map widget.
3- Repeat step 2 as desired.
4- Print the map widget to display it.

Here’s a basic example:

    library(leaflet)
    library(dplyr)
    m <- leaflet() %>%
      addTiles() %>%  # Add default OpenStreetMap map tiles
      addMarkers(lng=174.768, lat=-36.852, popup="The birthplace of R")
    m  # Print the map

#Leaflet Heat Maps

Create Map

We start by creating a map of the location.

    library(rMaps)
    L2 <- Leaflet$new()
    L2$setView(c(29.7632836,  -95.3632715), 10)
    L2$tileLayer(provider = "MapQuestOpen.OSM")
    L2

#Get Data

We will use the crime dataset from the ggmap package that contains a tidied up version of Houston crime data from January 2010 to August 2010.

    data(crime, package = 'ggmap')
    library(plyr)
    crime_dat = ddply(crime, .(lat, lon), summarise, count = length(address))
    crime_dat = toJSONArray2(na.omit(crime_dat), json = F, names = F)
    cat(rjson::toJSON(crime_dat[1:2]))

    [[27.5071143,-99.5055471,1],[29.4836146,-95.0618715,10]

    Add HeatMap

Now that we have the map and the data, the next step is to add the data to the map as a heatmap layer. Thanks to the Leaflet.heat plugin written by the Vladimir Agafonkin, the author of LeafletJS, this is really easy to do, with a little bit of custom javascript.

# Add leaflet-heat plugin. Thanks to Vladimir Agafonkin
L2$addAssets(jshead = c(
  "http://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"
))

# Add javascript to modify underlying chart
L2$setTemplate(afterScript = sprintf("
<script>
  var addressPoints = %s
  var heat = L.heatLayer(addressPoints).addTo(map)           
</script>
", rjson::toJSON(crime_dat)
))

L2