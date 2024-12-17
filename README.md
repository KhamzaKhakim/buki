# Tutor Parser Documentation

## Overview

This Python script parses tutor profiles from a web page, extracting comprehensive information about personal tutors using web scraping techniques with CSS and XPath selectors.

## Parsed Fields

### 1. Tutor Name

- **Field**: `name`
- **Description**: Full name of the tutor
- **Data Type**: String
- **Extraction**: Extracted from user name span element

### 2. Subjects

- **Field**: `subjects`
- **Description**: List of academic subjects or skills the tutor can teach
- **Data Type**: List of Strings
- **Extraction**: Gathered from lesson item spans

### 3. Educational Degree

- **Field**: `degree`
- **Description**: Academic or professional qualification of the tutor
- **Data Type**: String
- **Extraction**: Extracted from education span element

### 4. Professional Experience

- **Field**: `experience`
- **Description**: Total years of professional teaching or field experience
- **Data Type**: String
- **Extraction**: Cleaned by removing "Опыт: " prefix
- **Note**: May be `None` if no experience is specified

### 5. City

- **Field**: `city`
- **Description**: Geographical location of the tutor
- **Data Type**: String
- **Extraction**: Retrieved from location link text

### 6. Pricing

- **Field**: `price`
- **Description**: Hourly or session rate for tutoring
- **Data Type**: Integer
- **Extraction**: Filtered to include only numeric characters
- **Default**: 0 if no price is found

### 7. Online Teaching Capability

- **Field**: `canWorkOnline`
- **Description**: Indicates if the tutor offers online tutoring
- **Data Type**: Boolean
- **Extraction**: Presence of online work indicator element

### 8. Short Description

- **Field**: `shortDescription`
- **Description**: Brief overview of the tutor's teaching approach or specialties
- **Data Type**: String
- **Extraction**: Extracted from description span element

### 9. Rating

- **Field**: `rating`
- **Description**: Average user rating of the tutor
- **Data Type**: Float
- **Extraction**: Parsed from review block using regex
- **Range**: Typically 0.0 to 5.0

### 10. Review Count

- **Field**: `reviewCount`
- **Description**: Total number of reviews received by the tutor
- **Data Type**: Integer
- **Extraction**: Extracted from review count element using regex

## Parsing Method

The script uses a combination of CSS and XPath selectors to extract information from each tutor card, providing a robust method for gathering comprehensive tutor profiles.

## Dependencies

- Web scraping library (likely Scrapy or Similar)
- CSS and XPath selector support

## Example Usage

```python
# Pseudo-code for parsing tutors
for tutor_data in parser.parse(response):
    print(f"Tutor: {tutor_data['name']}")
    print(f"Subjects: {tutor_data['subjects']}")
    # Additional processing as needed
```

## Notes

- Some fields may be `None` if the information is not available
- Prices are converted to integers by removing non-numeric characters
- Online teaching capability is a boolean flag
