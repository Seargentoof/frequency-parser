# frequency-parser

This is the Frequency Parser program programmed by Dawson Lin, designed to detect Retract-and-Reorder (RAR) errors in the 
Electronic Health Record by making comparisons between clinical expressions of frequencies. 

## Language
This project was written in Python 3. 

## How it works
Frequency Parsers's frequencies_are_equal method compares two frequency expressions at a time. 

The input frequency expressions are looked up in a previously created database (a Microsoft Excel spreadsheet). The 
spreadsheet consists of two columns: one with frequency expressions (e.g. bid, q12hr) and the other with hour equivalents (e.g. 12).

If the hour equivalents are equal, the expressions are determined to be equal. Otherwise, they are not. 

## How to use this program
Use the frequencies_are_equal method to make comparisons for equality between medical frequency expressions. 

The Excel database is meant to be user-friendly and easy to understand, edit, and expand. However, it needs to be as well-standardized as possible. To achieve this, please observe the following conventions:
1. One hour equivalent per frequency expression. 
2. Keep the letter case consistent within a frequency expression.
3. Refrain from adding frequency expressions that are equal in a case-insensitive context to prevent duplicate rows.
4. Try to make decimal number Values as precise as possible, as to minimize floating point error when comparing for equality.
5. Write notes in the dedicated "Notes" column only.
