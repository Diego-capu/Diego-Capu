# Module Average Calculator for Coders

## Description

This is a simple Python console application designed to calculate weighted averages for coding students across different modules. The program collects grades from three subjects (English, Socio-emotional Skills, and Development), applies specific weights, determines the student's performance category, and keeps track of statistics for a group of exactly 5 students.

Main features:
- Weighted average calculation (20% English + 20% Socio-emotional + 60% Development)
- Performance classification: Reprobado (<49), Regular (50–78), Excelente (≥80)
- Basic input validation (numeric values and maximum score of 100)
- Summary statistics after processing 5 valid student entries

## How it Works

1. The program displays a welcome message: "Calcula tu promedio".
2. It initializes counters for failed students (`reprobados`), regular students (`regulares`), excellent students (`excelentes`), and total valid entries (`coder`).
3. It enters a loop that continues until exactly 5 students have been successfully processed (`while contador < 5`).
4. For each student, it requests:
   - Module number (integer)
   - Student's name (string)
   - Grades for English, Socio-emotional, and Development (floating-point numbers)
5. It validates that all grades are between 0 and 100 
6. If the grades are valid:
   - Calculates the weighted average:  
     `resultado = (ingles × 0.20) + (socio × 0.20) + (desarrollo × 0.60)`
   - Displays the module and the calculated average
   - Classifies the performance and updates the corresponding counters
   - Increments the student counter (`contador`)
7. If invalid data is entered (non-numeric values or grades > 100), it shows an error message and continues without counting that attempt.
8. After exactly 5 valid students have been processed, the program displays the final statistics:
   - Number of reprobados (failed)
   - Number of regulares
   - Number of excelentes
   - Total number of registered coders

## Status

> Current status: Functional prototype with basic error handling  
> The program works correctly when users enter valid data.  
> Known limitations :
> - No formatting of decimal places in the average display
> - Messages are in Spanish (could be internationalized)
> - No option to restart or save results to a file
