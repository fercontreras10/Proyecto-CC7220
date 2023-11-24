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

# Datasets
Most Subscribed YouTube Channels
Source: https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data
To mapping: sh bin/tarql --ntriples PATH/mappingMost.sparql PATH/MostSubscribedYoutubeChannels.csv

Global YouTube Statistics 2023
Source: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023
To mapìng: sh bin/tarql --ntriples PATH/mappingGlobal.sparql PATH//GlobalYouTubeStatistics.csv

YouTube Trending Video Dataset (updated daily) (only US)
Source: https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=DE_youtube_trending_data.csv
To mapping: sh bin/tarql --ntriples PATH/mappingUS.sparql PATH/USYoutubeTrendingData.csv
ttl(cause > 100MB): https://drive.google.com/file/d/13T55LARtAxQ9SmvA0Ti7IPgVZbZAvdCZ/view?usp=share_link

Used dataset (US + most)
xd.ttl(cause > 100MB): https://drive.google.com/file/d/1ggoG_qhAiovrFVlPJb29LwyUBNP8UMlO/view?usp=sharing
