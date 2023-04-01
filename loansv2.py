#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:31:21 2023

@author: giannidiarbi

 Gianni Diarbi
 DS2000
 Spring 2023
 HW 3 Problem 2
 loansv2.py
"""
LOAN_FILE = "debt_vs_tuition2.txt"

TUITION_CONVERTER = 4

import matplotlib.pyplot as plt

def main():
    
    # Gather data -- read in the file contents and initialize variables
    sum_tuitions = 0
    sum_debts = 0
    
    with open (LOAN_FILE, "r") as infile:
        while True:
            name = infile.readline()
            debt = infile.readline()
            yearly_tuition = infile.readline()
            
            if name == "":
                break
         
            # Computations - convert to ints
            debt = int(debt)
            yearly_tuition = int(yearly_tuition)
            
            sum_tuitions = int(sum_tuitions)
            sum_debts = int(sum_debts)
                
            # Compute the total four-year tuition cost of each school
            full_tuition = yearly_tuition * TUITION_CONVERTER
            
            # Compute the debt-to-tuition ratio of reach school
            individual_ratio = debt / full_tuition
          
            # Sum the total tuition and debt costs of each school
            sum_tuitions = sum_tuitions + yearly_tuition
            sum_debts = sum_debts + debt
                   
            # Compute the average debt-to-tuition ratio across schools using sums
            avg_ratio = sum_debts / ( sum_tuitions * TUITION_CONVERTER )
           

    # Re-open the file and read in the data
    with open (LOAN_FILE, "r") as infile:
        while True:
            name = infile.readline()
            debt = infile.readline()
            yearly_tuition = infile.readline()
            
            if name == "":
                break
         
            # Computations - Re-compute the ratio values
            # Convert floats to to ints
            debt = int(debt)
            yearly_tuition = int(yearly_tuition)
            
            sum_tuitions = int(sum_tuitions)
            sum_debts = int(sum_debts)
                
            # Compute the total tuition of each school
            full_tuition = yearly_tuition * TUITION_CONVERTER
            
            # Compute the debt-to-tuition ratio for reach school
            individual_ratio = debt / full_tuition
          
            # Differentiate the point colors, depending on if their debt-to-tuition 
            # fraction falls above or below the average
            if individual_ratio < avg_ratio:
                   point_color = "lime"
            elif individual_ratio > avg_ratio:
                   point_color = "slateblue"
            
            # Plot the points, add a title, and add labels to the axes
            plt.plot(yearly_tuition, individual_ratio, "o", color = point_color)
            plt.xlabel("Yearly Tuition Cost ($)")
            plt.ylabel("Debt-to-Tuition Ratio")
            plt.title("Yearly Tuition ($) vs Debt-to-Tuition Ratio")
            
            # Adjust the x and y limits
            plt.xlim(54000, 64000)
            plt.ylim(0.06, 0.12)
               
         # Plot a horizontal line representing the overall avg debt fraction and 
         # label it in a legend
        plt.axhline(avg_ratio, color = "magenta", 
                    label = "avg debt-to-tuition")
        plt.legend()
        
main()