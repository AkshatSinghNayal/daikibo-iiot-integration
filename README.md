# Daikibo IIoT Data Integration

**Date: 2025-08-07 15:20:37 UTC**  
**Author: AkshatSinghNayal**

## Project Overview

This repository contains a solution for integrating two different IIoT telemetry data formats used by Daikibo Industrials into a unified format. The solution provides converters for normalizing data from legacy and new IIoT devices into a standardized structure for analytics and monitoring.

## Problem Statement

Daikibo Industrials is integrating IIoT (industrial internet of things) devices to monitor, measure, and analyze their manufacturing processes. Currently, their infrastructure uses devices streaming telemetry data in two different formats:
- Format 1: Uses ISO timestamp format with specific field naming conventions
- Format 2: Uses millisecond timestamp format with different field naming conventions

This solution combines both formats into a unified standard for consistent data processing.

## Repository Structure

- `main.py`: Contains the implementation of the data format converters
- `data-1.json`: Sample data in format 1
- `data-2.json`: Sample data in format 2
- `data-result.json`: Expected unified data format
- `test_solution.py`: Tests to validate the format converters

## Implementation Details

The solution implements two key functions:
1. `convert_format_1()`: Converts from format 1 to the unified format
2. `convert_format_2()`: Converts from format 2 to the unified format

Key challenges addressed include timestamp normalization and field name standardization.

## Running the Solution

1. Clone this repository
2. Run `python main.py` to execute the code and run tests
3. Examine the test results to ensure all conversions are performed correctly