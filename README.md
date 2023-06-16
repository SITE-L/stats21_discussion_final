# STATS21Discussion_Final

## Introduction
The "Stats21Discussion_Final" application is a powerful data exploration and visualization tool developed using Python and Streamlit. Its main purpose is to provide users with an interactive and user-friendly interface to analyze and visualize their datasets. With features like file upload, data summary, column selection, and customized visualizations, this application simplifies the process of understanding and gaining insights from data.

## Features

### File Upload
Users can easily upload their dataset in CSV format using the file upload functionality. Streamlit's `file_uploader` function is employed to handle the file selection and upload process seamlessly.

### Data Display
Once a file is uploaded, the application reads it into a pandas DataFrame and presents the data within the Streamlit application itself. This allows users to conveniently view their data and get an initial overview of its structure and contents.

### Data Summary
The application provides a comprehensive summary of the uploaded dataset. It displays fundamental information such as the number of rows and columns in the dataset, the names of the columns, and the frequency of each data type present. This summary provides users with a quick grasp of their data's basic characteristics.

### Column Selection
Users have the flexibility to select a specific column of interest from a dropdown menu. The dropdown menu is populated dynamically with the available column names from the dataset. This feature allows users to focus their analysis on a specific aspect of their data.

### Data Inspection
Upon selecting a column, the application displays the unique values present in that column. This helps users gain a better understanding of the categorical or numerical categories or levels within their data.

### Data Analysis and Visualization
The application performs tailored analysis and visualization based on the selected column's data type.

- Numerical Columns: For numerical columns, the application generates a comprehensive five-number summary (minimum, first quartile, median, third quartile, and maximum) and creates a distribution plot using matplotlib and seaborn. The customized distribution plot enables users to explore the distribution and statistical properties of their numerical data easily.

- Categorical Columns: For categorical columns, the application presents the proportions of each category level and generates an aesthetically pleasing bar plot. The bar plot helps users visualize the frequencies of different categories within their dataset, facilitating better comprehension and comparison.

## Conclusion
The "Stats21Discussion_Final" application offers an intuitive and efficient solution for data exploration, analysis, and visualization. By providing essential features like file upload, data summary, column selection, and customized visualizations, it empowers users to extract meaningful insights from their datasets. Whether users are looking to understand the distribution of numerical variables or the proportions of categorical variables, this application simplifies the process, making data exploration an engaging and insightful experience.

