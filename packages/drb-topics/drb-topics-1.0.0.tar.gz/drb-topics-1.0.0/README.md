# topics

# DRB Topics
**_drb-topics_** is a Python plugin for **DRB**, to help the installations
of drb topics.

## Installation
```shell
pip install drb-topics[OPTIONAL]
```

## Topic
Here the list of all the topics downloadable with this project.

| name       | category | package              |
|:-----------|:---------|:---------------------|
| safe       | SENTINEL | drb-topic-safe       |
| sentinel1  | SENTINEL | drb-topic-sentinel1  |
| sentinel2  | SENTINEL | drb-topic-sentinel2  |
| sentinel3  | SENTINEL | drb-topic-sentinel3  |
| sentinel5p | SENTINEL | drb-topic-sentinel5p |
| landsat8   | NONE     | drb-topic-landsat8   |
| geojson    | NONE     | drb-topic-geojson    |

You can download a topic with his name like:
```shell
pip install drb-topics[geojson]
```
to only download the topic geojson

To download all the sentinel topic:
```shell
pip install drb-topics[sentinel]
```

To download all the topics:
```shell
pip install drb-topics[all]
```