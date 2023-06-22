
# -In this rep i will upload Simple Data science projects in python using pandas & numpy in order to enhace my skills for the data prepretion phase, which is the most important phase in the data science cycle.-




# File1: Sales related problems
This file contain 4 sale related problems and i solved them in the file and explaned each step via the markdown cells

## Task1:
### What month has the best Sales?
    - i solved it by  creating a month column from the date column. Then for each month, i will get multiply the quanty by price
    -This is the resulting plot


![Screenshot (13)](https://github.com/iLawFD/simple-data-science-projects/assets/88871860/74c2520f-a106-45ea-9c9d-d873e03c20a5)

## Task2:
### Finding the city with highes sales
  1 - I will create a city column based on the adress column
 2- For each city multiply the price column by the quanity column

 This is the result (all the cities with their sales)
 
![Screenshot (15)](https://github.com/iLawFD/simple-data-science-projects/assets/88871860/43ed1910-4931-4b75-b306-26f5e9d0bc44)

## Task3:
### Generate a column of the prodcuts sold togther
- Just using the order ID column. If it is duplicated and for diffrent product then it means the same person baught at least two diffrent products and thats we intressted in
- This is the column
- ![Screenshot (17)](https://github.com/iLawFD/simple-data-science-projects/assets/88871860/1daf487b-f300-47e7-9596-c05015612b2e)

## Task4:
### What product has been sold the most?
  - first clean the neccry columns to be able to convert then to numric
  - second create a sale column and then order it
  - third show the product column based on order of sales
  - ![Screenshot (15)](https://github.com/iLawFD/simple-data-science-projects/assets/88871860/5e7af2fc-8618-47d0-b6f2-e626c89604e3)


(advice: never hesitate to add a column to your data frame because it might makes work much easier)

# File2: AnimeSuggestions:
- Input : the user has to select a genre(e.g Drama) and select wether they want animes or movies
- output: Top 5 animes or moives of the desired genre based on the rating column 



