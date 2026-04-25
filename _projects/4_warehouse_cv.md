---
layout: page
title: Warehouse Computer Vision System
description: Real-time forklift and pallet tracking system using YOLOv8 + ByteTrack with QR code identification (pyzbar). Supports RTSP, local video, and webcam feeds. Generates CSV movement logs for WMS integration.
img: assets/img/projects/warehouse_cv.png
importance: 2
category: computer-vision
tags: [YOLOv8, ByteTrack, Computer Vision, Python, OpenCV]
github: https://github.com/mohcinemadkour
---

## Overview

A production-ready **warehouse computer vision system** for real-time tracking of forklifts and pallets across warehouse environments. Built to integrate directly with Warehouse Management Systems (WMS) via CSV movement logs.

## Features

- **Multi-object tracking** — YOLOv8 detection + ByteTrack for persistent object IDs across frames
- **QR code identification** — `pyzbar` integration for reading pallet and forklift QR codes in motion
- **Flexible input** — supports RTSP camera streams, local video files, and webcam
- **WMS-ready output** — CSV logs of object ID, location, timestamp, and movement events for direct WMS ingestion
- **Real-time visualization** — annotated video feed with bounding boxes, track IDs, and QR data overlay

## Architecture

```
Camera Feed (RTSP/file/webcam)
        ↓
YOLOv8 Object Detection (forklift, pallet classes)
        ↓
ByteTrack Multi-Object Tracker (persistent IDs)
        ↓
pyzbar QR Decoder (identity resolution)
        ↓
Movement Event Logger (CSV) → WMS Integration
```

## Use Cases

- Inventory movement tracking without manual scanning
- Forklift path analysis for safety compliance
- Real-time zone occupancy for dynamic slotting
- Audit trail generation for warehouse operations

## Tech Stack

`Python` · `YOLOv8 (Ultralytics)` · `ByteTrack` · `pyzbar` · `OpenCV` · `NumPy` · `Pandas`
