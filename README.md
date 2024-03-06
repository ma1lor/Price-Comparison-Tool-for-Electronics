#  Price Comparison Tool for Electronics

## Introduction
The Price Comparison Tool for Electronics is a freelance project aimed at assisting users in comparing prices of electronic products between SharafDG and competitors in Oman. Leveraging web scraping techniques and Selenium automation, this tool fetches real-time pricing information for specified product models and their counterparts from competitor stores. The collected data is then presented in an organized manner for users to analyze price differentials conveniently.

## Technologies
- **Python:** The core programming language used for scripting the web scraping tool.
- **Selenium:** Employed for automating web browser interactions to navigate through the SharafDG website and extract pricing data.
- **Pandas:** Utilized for structuring and processing the extracted data into a tabular format.
- **Excel:** The final output is saved as an Excel spreadsheet for easy access and analysis.

## Usage
Users can input a list of product codes along with their corresponding competitor model codes. The tool then searches for these products on the SharafDG website and retrieves their prices. Simultaneously, it fetches the prices of competitor models. Once the data collection process is complete, the tool calculates the percentage difference in prices between the specified product and its competitor counterpart. Finally, the results are compiled into an Excel spreadsheet named "scraped_data.xlsx" for further examination.

This tool serves as a valuable resource for consumers and businesses alike, enabling them to make informed purchasing decisions by identifying the best deals available in the market for electronic products.

**Note:** This project is a freelance endeavor, developed with the intention of providing users with a convenient means of comparing prices across different retailers in Oman's electronics market.
