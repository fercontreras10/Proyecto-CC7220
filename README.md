# Project Group 10
Conversion of data about trending videos and the most subscribed channels on YouTube to RDF using Tarql to make queries in SPARQL to obtain more information on the categories of the videos from the channels, their rankings, etc.

# Tarql: SPARQL for Tables
Using tarql

Tarql is a command-line tool for converting CSV files to RDF using SPARQL 1.1 syntax. It's written in Java and based on Apache ARQ.

**See http://tarql.github.io/ for documentation.**

## Building

Get the code from GitHub: http://github.com/tarql/tarql

Tarql uses Maven. To create executable scripts for Windows and Unix in `/target/appassembler/bin/tarql`:

    mvn package appassembler:assemble

Otherwise it's standard Maven.

## Queries

The querys where done by using rdflib (https://rdflib.readthedocs.io/en/stable/) on python 3.10

# Datasets
Most Subscribed YouTube Channels <br/>
Source: https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data <br/>
To mapping: sh bin/tarql --ntriples PATH/mappingMost.sparql PATH/MostSubscribedYoutubeChannels.csv

YouTube Trending Video Dataset (updated daily) (only US) <br/>
Source: https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=DE_youtube_trending_data.csv <br/>
To mapping: sh bin/tarql --ntriples PATH/mappingUS.sparql PATH/USYoutubeTrendingData.csv <br/>
ttl(cause > 100MB): https://drive.google.com/file/d/13T55LARtAxQ9SmvA0Ti7IPgVZbZAvdCZ/view?usp=share_link

Used dataset (US + most) <br/>
xd.ttl(cause > 100MB): https://drive.google.com/file/d/1ggoG_qhAiovrFVlPJb29LwyUBNP8UMlO/view?usp=sharing
