<h1 align="center"> Radiant MLHub Client</h1>
<p align="center">
    <a href="">
        <img alt="Lifecycle: experimental" src="https://img.shields.io/badge/lifecycle-experimental-orange.svg"></a>
    <a href="LICENSE" alt="License">
        <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" /></a>   
</p>

<p align="center"> The mlhub package aims at providing a toolbox for interracting with the Radiant MLhub API and accessing the Earth Observations training datasets hosted on the Radiant MLHub platform.
</p>

## Table Of Contents <!-- omit in toc -->

- [Radiant MLHub](#radiant-mlhub)
  - [Radiant MLHub API](#radiant-mlhub-api)
    - [Spatio-Temporal Asset Catalog](#spatio-temporal-asset-catalog)
    - [Radiant MLHub Datasets](#radiant-mlhub-datasets)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Authentication](#authentication)
  - [Usage](#usage)
- [Examples](#examples)
- [Alternatives](#alternatives)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Radiant MLHub 

The Radiant MLHub is an open library for geospatial training data to advance machine learning applications on Earth Observations. The training datasets include **pairs of imagery and labels** for different types of ML problems including **image classification**, **object detection**, and **semantic segmentation**. 

### Radiant MLHub API

The Radiant MLHub API gives access to the different datasets. You can access the full API documentation at [docs.mlhub.earth](docs.mlhub.earth) and check the [Radiant MLHub site](https://mlhub.earth). 

#### Spatio-Temporal Asset Catalog 

Datasets are stored as collections on Radiant MLHub catalog an each item in their collections is explained in json format compliant with [STAC](https://stacspec.org/) [label extension](https://github.com/radiantearth/stac-spec/tree/master/extensions/label) definition.

- **A collection** represents the top-most data level i.e. that data comes from the same source for the same geography and might include different years or sub-geographies. Additional fields to enable description of things like the spatial and temporal extent of the data, the license, keywords, providers, etc.

- **An item** represents an atomic collection of inseparable data and metadata (**assets**). A STAC Item is a GeoJSON feature and can be easily read by any modern GIS or geospatial library. The STAC Item JSON specification includes additional fields for:

    - **properties** property containing metadata (date of revisit)
    - **assets** property providing links to the described data
    - **links** property allowing users to traverse other related STAC Items.

- **An asset** is an object that that can be downloaded or streamed. The links to the assets associated with an Item are contained in the *assets* property of an item. Depending on the dataset asset can be:
  
  - One or several **GeoTIFF files** (representing the spectral bands)
  - GeoJSON files 
  - Documentation PDF files 
  
#### Radiant MLHub Datasets

![](https://miro.medium.com/max/1260/1*Ei8QLbju7wfssi7w7NBOUA.png)

Radiant MLHub datasets are split into two STAC collections: One contains STAC items for the source imagery and the other STAC items for the labels.

- **Label Items** are a JSON object with properties describing the type of label, possible label values, spatial and temporal extents, and links to the label assets to download.
  
- **Source imagery items** contain all information required to determine the location and time that the imagery was taken, as well as links to download either individual bands of the imagery or the multi-band files.
 
For more details see Kevin Booth article [Accessing and Downloading Training Data on the Radiant MLHub API ](https://medium.com/radiant-earth-insights/accessing-and-downloading-training-data-on-the-radiant-mlhub-api-f04dc635592f)


## Getting Started

### Requirements

-   Python 3.6 (or more recent)
-   [pip](https://pip.pypa.io/en/stable/)

### Installation 

```bash
pip install git+https://github.com/dataJSA/radiant-mlhub
```
### Authentication

 To get your access token, go to [dashboard.mlhub.earth](https://dashboard.mlhub.earth/). If you have not used Radiant MLHub before, you will need to sign up and create a new account. Otherwise, sign in. Under Usage, you'll see your access token, which you will need. Do not share your access token with others: your usage may be limited and sharing your access token is a security risk.

### Usage

```python
from mlhub import mlhub

API_TOKEN = 'YOUR-TOKEN'

client = mlhub.Client(api_token=API_TOKEN, 
                      collection_id='ref_landcovernet_v1_labels',
                      feature_id='ref_landcovernet_v1_labels_29NMG_12')
```
## Examples

A notebook demonstrating how to use the MLHub Client for downloading assets from the `LandCoverNet` dataset is provided as a reference. 

## Alternatives 

Otherwise, the Radiant Earth Foundation has published a series of [notebook tutorials](https://github.com/radiantearth/mlhub-tutorials) from which this project is derived. The notebook tutorials demonstrate how to interact with the MLHub API.

## Documentation

## Contributing

## Acknowledgements

This project is derived from the Radiant MLHub notebook tutorials and articles provided by the Radiant Earth Foundation and developed by Kevin Booth.